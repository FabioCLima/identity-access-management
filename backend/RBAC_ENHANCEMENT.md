# Advanced RBAC Implementation Guide

## Overview

Enhanced role-based access control with three levels:
- **Barista:** Read-only access to drink details
- **Manager:** Manage drinks and baristas
- **Administrator:** Full system access

## Current vs Enhanced Permissions

### Current Implementation (Simplified)

| Operation | Barista | Manager |
|-----------|-------|---------|
| View drinks | ✅ | ✅ |
| View details | ✅ | ✅ |
| Create drinks | ❌ | ✅ |
| Update drinks | ❌ | ✅ |
| Delete drinks | ❌ | ✅ |

### Enhanced Implementation (Realistic)

| Operation | Barista | Manager | Admin |
|-----------|---------|---------|-------|
| View drinks | ✅ | ✅ | ✅ |
| View details | ✅ | ✅ | ✅ |
| Create drinks | ❌ | ❌ | ✅ |
| Update drinks | ❌ | ✅ | ✅ |
| Delete drinks | ❌ | ✅ | ✅ |
| Manage baristas | ❌ | ✅ | ✅ |
| Manage managers | ❌ | ❌ | ✅ |
| System config | ❌ | ❌ | ✅ |

## Step 1: Update Auth0 Permissions

Go to Auth0 Dashboard → Your API → Permissions:

### New Permissions to Add

```
get:drinks              # All roles
get:drinks-detail        # All roles
post:drinks              # Admin only
patch:drinks             # Manager, Admin
delete:drinks            # Manager, Admin
manage:baristas          # Manager, Admin
manage:managers          # Admin only
system:configure         # Admin only
```

## Step 2: Update Auth0 Roles

### Barista Role
**Permissions:**
- `get:drinks`
- `get:drinks-detail`

### Manager Role
**Permissions:**
- `get:drinks`
- `get:drinks-detail`
- `patch:drinks`
- `delete:drinks`
- `manage:baristas`

### Administrator Role (New)
**Permissions:**
- All Manager permissions
- `post:drinks`
- `manage:managers`
- `system:configure`

## Step 3: Update Backend Endpoints

### Modified API Endpoints in `src/api.py`

```python
@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')  # Admin only
def create_drink(payload):
    # Only administrators can create drinks
    ...

@app.route('/drinks/<int:drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')  # Manager and Admin
def update_drink(payload, drink_id):
    # Managers and admins can update
    ...

@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')  # Manager and Admin
def delete_drink(payload, drink_id):
    # Managers and admins can delete
    ...
```

## Step 4: Add User Management Endpoints

Create new file: `backend/src/users.py`

```python
"""
User Management API

Endpoints for managing users, roles, and permissions.
Requires administrator access.
"""

from flask import Blueprint, request, jsonify, abort
from .auth.auth import AuthError, requires_auth
from authlib.integrations.requests_client import OAuth2Session
import os

users_bp = Blueprint('users', __name__)

# Auth0 Management API credentials
AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
AUTH0_CLIENT_ID = os.environ.get('AUTH0_MANAGEMENT_CLIENT_ID')
AUTH0_CLIENT_SECRET = os.environ.get('AUTH0_MANAGEMENT_CLIENT_SECRET')

def get_management_token():
    """Get access token for Auth0 Management API."""
    client = OAuth2Session(
        client_id=AUTH0_CLIENT_ID,
        client_secret=AUTH0_CLIENT_SECRET
    )
    token = client.fetch_token(
        f'https://{AUTH0_DOMAIN}/oauth/token',
        grant_type='client_credentials',
        audience=f'https://{AUTH0_DOMAIN}/api/v2/'
    )
    return token['access_token']


@users_bp.route('/users', methods=['GET'])
@requires_auth('system:configure')
def list_users(payload):
    """List all users (Admin only)."""
    try:
        token = get_management_token()
        # Use Auth0 Management API to list users
        # Implementation here
        return jsonify({"success": True, "users": []})
    except Exception as e:
        print(f"Error: {str(e)}")
        abort(500)


@users_bp.route('/users', methods=['POST'])
@requires_auth('system:configure')
def create_user(payload):
    """Create new user (Admin only)."""
    try:
        token = get_management_token()
        body = request.get_json()
        # Implementation here
        return jsonify({"success": True, "user": {}})
    except Exception as e:
        print(f"Error: {str(e)}")
        abort(500)


@users_bp.route('/users/<user_id>/roles', methods=['PATCH'])
@requires_auth('manage:baristas')  # Managers can manage baristas
def update_user_roles(payload, user_id):
    """Update user roles (Manager/Admin)."""
    try:
        token = get_management_token()
        body = request.get_json()
        # Implementation here
        return jsonify({"success": True, "user": {}})
    except Exception as e:
        print(f"Error: {str(e)}")
        abort(500)
```

## Step 5: Register User Management Blueprint

In `src/api.py`:

```python
from .users import users_bp

# Register blueprint
app.register_blueprint(users_bp, url_prefix='/api')
```

## Step 6: Environment Variables

Add to `backend/.env`:

```bash
# Auth0 Configuration (existing)
AUTH0_DOMAIN=your-domain.auth0.com
AUTH0_API_AUDIENCE=coffee-shop-api

# Auth0 Management API (new)
AUTH0_MANAGEMENT_CLIENT_ID=your_client_id
AUTH0_MANAGEMENT_CLIENT_SECRET=your_client_secret
```

## Step 7: Test the Implementation

### Test Cases

1. **Barista Access:**
   - ✅ Can GET /drinks
   - ✅ Can GET /drinks-detail
   - ❌ Cannot POST /drinks
   - ❌ Cannot PATCH /drinks/:id
   - ❌ Cannot DELETE /drinks/:id

2. **Manager Access:**
   - ✅ Can GET /drinks
   - ✅ Can GET /drinks-detail
   - ❌ Cannot POST /drinks
   - ✅ Can PATCH /drinks/:id
   - ✅ Can DELETE /drinks/:id
   - ✅ Can manage baristas

3. **Admin Access:**
   - ✅ All Manager permissions
   - ✅ Can POST /drinks
   - ✅ Can manage all users
   - ✅ Can configure system

## Step 8: Update Postman Collection

Add new requests for user management endpoints in a new "admin" folder.

## Benefits

1. **More Realistic:** Reflects actual business roles
2. **Better Security:** Principle of least privilege
3. **Demonstrates Expertise:** Shows understanding of IAM
4. **Scalable:** Easy to add more roles

## Estimated Time

- Setup: 2-3 hours
- Testing: 1 hour
- Documentation: 1 hour
- **Total: 4-5 hours**

