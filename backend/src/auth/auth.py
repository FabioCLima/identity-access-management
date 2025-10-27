"""
Authentication module for Coffee Shop API.

This module provides authentication and authorization functionality using Auth0 JWT tokens.
It includes decorators for protecting API endpoints and validating user permissions.

Environment Variables Required:
    AUTH0_DOMAIN: Your Auth0 domain (e.g., 'udacity-fsnd.auth0.com')
    AUTH0_ALGORITHM: JWT algorithm (default: 'RS256')
    AUTH0_API_AUDIENCE: Your Auth0 API audience identifier
"""

import json
import os
from functools import wraps
from urllib.request import urlopen

from flask import request
from jose import jwt

# Read Auth0 configuration from environment variables
AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN", "udacity-fsnd.auth0.com")
ALGORITHMS = os.environ.get("AUTH0_ALGORITHM", "RS256").split(",")
API_AUDIENCE = os.environ.get("AUTH0_API_AUDIENCE", "dev")


class AuthError(Exception):
    """AuthError Exception - A standardized way to communicate auth failure modes."""

    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header():
    """
    Get the Authorization header from the request and extract the token.

    Returns:
        str: The JWT token from the Authorization header

    Raises:
        AuthError: If the Authorization header is missing or malformed
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError(
            {
                "code": "authorization_header_missing",
                "description": "Authorization header is expected.",
            },
            401,
        )

    parts = auth.split()
    if parts[0].lower() != "bearer":
        raise AuthError(
            {
                "code": "invalid_header",
                "description": 'Authorization header must start with "Bearer".',
            },
            401,
        )

    elif len(parts) == 1:
        raise AuthError(
            {"code": "invalid_header", "description": "Token not found."},
            401,
        )

    elif len(parts) > 2:
        raise AuthError(
            {
                "code": "invalid_header",
                "description": "Authorization header must be bearer token.",
            },
            401,
        )

    token = parts[1]
    return token


def verify_decode_jwt(token):
    """
    Verify and decode a JWT token using Auth0's public keys.

    Args:
        token (str): The JWT token to verify and decode

    Returns:
        dict: The decoded JWT payload

    Raises:
        AuthError: If the token is invalid, expired, or claims are incorrect
    """
    jsonurl = urlopen(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json")  # noqa: S310
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    if "kid" not in unverified_header:
        raise AuthError(
            {"code": "invalid_header", "description": "Authorization malformed."},
            401,
        )

    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"],
            }

    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer="https://" + AUTH0_DOMAIN + "/",
            )

            return payload

        except jwt.ExpiredSignatureError as err:
            raise AuthError(
                {"code": "token_expired", "description": "Token expired."}, 401
            ) from err

        except jwt.JWTClaimsError as err:
            raise AuthError(
                {
                    "code": "invalid_claims",
                    "description": "Incorrect claims. Please, check the audience and issuer.",
                },
                401,
            ) from err

        except Exception as err:
            raise AuthError(
                {
                    "code": "invalid_header",
                    "description": "Unable to parse authentication token.",
                },
                400,
            ) from err

    raise AuthError(
        {"code": "invalid_header", "description": "Unable to find the appropriate key."},
        400,
    )


def check_permissions(permission, payload):
    """
    Check if the JWT payload contains the required permission.

    Args:
        permission (str): The required permission (e.g., 'post:drinks')
        payload (dict): The decoded JWT payload

    Returns:
        bool: True if the permission is present

    Raises:
        AuthError: If permissions are not included in the payload
        AuthError: If the requested permission is not in the payload permissions array
    """
    # Check if permissions exist in payload
    if "permissions" not in payload:
        raise AuthError(
            {
                "code": "invalid_claims",
                "description": "Permissions not included in JWT.",
            },
            400,
        )

    # Check if the specific permission is present
    if permission not in payload["permissions"]:
        raise AuthError(
            {
                "code": "invalid_claims",
                "description": "Permission not found in JWT.",
            },
            403,
        )

    return True


def requires_auth(permission=""):
    """
    Decorator to protect endpoints that require authentication and authorization.

    This decorator:
    1. Gets the JWT token from the Authorization header
    2. Verifies and decodes the JWT token
    3. Checks if the token contains the required permission
    4. Raises errors for invalid tokens, expired tokens, or missing permissions

    Args:
        permission (str): The required permission (e.g., 'post:drinks')

    Usage:
        @requires_auth('post:drinks')
        def create_drink(payload):
            # Create drink logic
            pass

    Raises:
        AuthError: If authentication or authorization fails
    """
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper

    return requires_auth_decorator
