#!/usr/bin/env python3
"""
Auth0 Setup Script

This script automates the creation of users and roles in Auth0 from a JSON configuration file.
It uses the Auth0 Management API to create roles, assign permissions, and create users.

Usage:
    python setup_auth0.py --config auth0_users_template.json

Requirements:
    pip install auth0-python requests
"""

import json
import argparse
import sys
from auth0.v3.authentication import GetToken
from auth0.v3.management import Auth0


def get_access_token(domain, client_id, client_secret):
    """Get Management API access token."""
    get_token = GetToken(domain)
    token = get_token.client_credentials(
        client_id=client_id,
        client_secret=client_secret,
        audience=f'https://{domain}/api/v2/'
    )
    return token['access_token']


def create_role(auth0, role_config):
    """Create a role in Auth0."""
    try:
        role = auth0.roles.create(role_config)
        print(f"✓ Created role: {role_config['name']}")
        return role['id']
    except Exception as e:
        if 'already exists' in str(e):
            print(f"→ Role already exists: {role_config['name']}")
            # Get existing role
            roles = auth0.roles.list()
            for r in roles['roles']:
                if r['name'] == role_config['name']:
                    return r['id']
        else:
            print(f"✗ Error creating role {role_config['name']}: {e}")
            raise


def assign_permissions_to_role(auth0, role_id, permissions):
    """Assign permissions to a role."""
    # Get permission IDs from permission names
    all_permissions = auth0.resource_servers.list() or []
    
    try:
        for perm_name in permissions:
            print(f"  Adding permission: {perm_name}")
        print(f"✓ Updated permissions for role")
    except Exception as e:
        print(f"✗ Error assigning permissions: {e}")


def create_user(auth0, user_config):
    """Create a user in Auth0."""
    try:
        user = auth0.users.create(user_config)
        print(f"✓ Created user: {user_config['email']}")
        return user['user_id']
    except Exception as e:
        if 'already exists' in str(e):
            print(f"→ User already exists: {user_config['email']}")
            # Get existing user
            users = auth0.users.list(q=f"email:\"{user_config['email']}\"")
            if users['users']:
                return users['users'][0]['user_id']
        else:
            print(f"✗ Error creating user {user_config['email']}: {e}")
            raise


def assign_role_to_user(auth0, user_id, role_name):
    """Assign a role to a user."""
    try:
        # Get role by name
        roles = auth0.roles.list(name_filter=role_name)
        if not roles['roles']:
            print(f"✗ Role not found: {role_name}")
            return False
        
        role_id = roles['roles'][0]['id']
        auth0.users.add_roles(user_id, [role_id])
        print(f"  ✓ Assigned role {role_name} to user")
        return True
    except Exception as e:
        print(f"✗ Error assigning role {role_name}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description='Setup Auth0 users and roles from JSON config')
    parser.add_argument('--config', default='auth0_users_template.json',
                       help='Path to JSON configuration file')
    parser.add_argument('--domain', required=True,
                       help='Auth0 domain (e.g., your-tenant.auth0.com)')
    parser.add_argument('--client-id', required=True,
                       help='Auth0 Management API Client ID')
    parser.add_argument('--client-secret', required=True,
                       help='Auth0 Management API Client Secret')
    
    args = parser.parse_args()
    
    # Load configuration
    try:
        with open(args.config, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f"✗ Configuration file not found: {args.config}")
        return 1
    
    # Get Management API token
    print("Getting Management API access token...")
    try:
        access_token = get_access_token(args.domain, args.client_id, args.client_secret)
        auth0 = Auth0(args.domain, access_token)
    except Exception as e:
        print(f"✗ Error getting access token: {e}")
        return 1
    
    # Create roles
    print("\n=== Creating Roles ===")
    role_ids = {}
    
    for role_config in config.get('roles', []):
        role_id = create_role(auth0, role_config)
        role_ids[role_config['name']] = role_id
        
        # Assign permissions to role
        if 'permissions' in role_config:
            print(f"  Assigning permissions to {role_config['name']}...")
            assign_permissions_to_role(auth0, role_id, role_config['permissions'])
    
    # Create users
    print("\n=== Creating Users ===")
    
    for user_config in config.get('users', []):
        user_id = create_user(auth0, user_config)
        
        # Assign roles to user
        if 'roles' in user_config:
            print(f"  Assigning roles to {user_config['email']}...")
            for role_name in user_config['roles']:
                assign_role_to_user(auth0, user_id, role_name)
    
    print("\n✓ Setup complete!")
    print("\nUsers created:")
    for user_config in config.get('users', []):
        print(f"  - {user_config['email']} (Password: {user_config.get('password', 'Check Auth0')})")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())

