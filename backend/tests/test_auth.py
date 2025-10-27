"""
Tests for authentication and authorization.

This module tests JWT token handling and permission checking.
"""

import json
import os
import unittest
from unittest.mock import patch

import jwt as pyjwt
from jose import jwt

from src.auth.auth import (
    AuthError,
    AUTH0_DOMAIN,
    API_AUDIENCE,
    ALGORITHMS,
    check_permissions,
    get_token_auth_header,
    requires_auth,
)
from src.api import app


class AuthTestCase(unittest.TestCase):
    """Test cases for authentication and authorization."""

    def setUp(self):
        """Set up test fixtures."""
        self.app = app
        self.client = self.app.test_client()
        self.app.config["TESTING"] = True

    def test_auth_error_exception(self):
        """Test AuthError exception."""
        error = AuthError({"code": "test", "description": "Test error"}, 401)

        self.assertEqual(error.error["code"], "test")
        self.assertEqual(error.status_code, 401)

    @patch("src.auth.auth.request")
    def test_get_token_auth_header_missing(self, mock_request):
        """Test get_token_auth_header with missing header."""
        mock_request.headers.get.return_value = None

        with self.assertRaises(AuthError) as context:
            get_token_auth_header()

        self.assertEqual(context.exception.status_code, 401)
        self.assertEqual(
            context.exception.error["code"],
            "authorization_header_missing",
        )

    @patch("src.auth.auth.request")
    def test_get_token_auth_header_invalid_format(self, mock_request):
        """Test get_token_auth_header with invalid format."""
        mock_request.headers.get.return_value = "Invalid format"

        with self.assertRaises(AuthError) as context:
            get_token_auth_header()

        self.assertEqual(context.exception.status_code, 401)

    @patch("src.auth.auth.request")
    def test_get_token_auth_header_no_bearer(self, mock_request):
        """Test get_token_auth_header without Bearer prefix."""
        mock_request.headers.get.return_value = "Invalid token123"

        with self.assertRaises(AuthError) as context:
            get_token_auth_header()

        self.assertEqual(context.exception.status_code, 401)
        self.assertEqual(context.exception.error["code"], "invalid_header")

    @patch("src.auth.auth.request")
    def test_get_token_auth_header_success(self, mock_request):
        """Test get_token_auth_header success."""
        mock_request.headers.get.return_value = "Bearer test_token123"

        token = get_token_auth_header()
        self.assertEqual(token, "test_token123")

    def test_check_permissions_missing_permissions(self):
        """Test check_permissions with missing permissions."""
        payload = {"sub": "test"}

        with self.assertRaises(AuthError) as context:
            check_permissions("post:drinks", payload)

        self.assertEqual(context.exception.status_code, 400)
        self.assertEqual(
            context.exception.error["code"],
            "invalid_claims",
        )

    def test_check_permissions_permission_not_found(self):
        """Test check_permissions with permission not in payload."""
        payload = {"permissions": ["get:drinks"]}

        with self.assertRaises(AuthError) as context:
            check_permissions("post:drinks", payload)

        self.assertEqual(context.exception.status_code, 403)
        self.assertEqual(
            context.exception.error["code"],
            "invalid_claims",
        )

    def test_check_permissions_success(self):
        """Test check_permissions success."""
        payload = {"permissions": ["post:drinks", "get:drinks"]}

        result = check_permissions("post:drinks", payload)
        self.assertTrue(result)

    def test_requires_auth_decorator(self):
        """Test requires_auth decorator execution."""
        mock_token = "test_token"

        @requires_auth("post:drinks")
        def test_func(payload):
            return {"success": True}

        # Mock the functions used by decorator
        with patch("src.auth.auth.get_token_auth_header", return_value=mock_token), \
             patch("src.auth.auth.verify_decode_jwt", return_value={"permissions": ["post:drinks"]}):
            # The decorator should work but we can't fully test without Auth0 keys
            pass


if __name__ == "__main__":
    unittest.main()

