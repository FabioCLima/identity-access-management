#!/usr/bin/env python3
"""
Auth0 Setup Script

This script automates the creation of users and roles in Auth0 from a JSON configuration file.
It uses the Auth0 Management API to create roles, assign permissions, and create users.

Usage:
    python setup_auth0.py --domain your-tenant.auth0.com --client-id ID --client-secret SECRET

Requirements:
    pip install auth0-python requests
"""

import json
import argparse
import sys
import requests


# Removed duplicate functions - using requests directly in main()


def create_role(domain, headers, role_config):
    """Create a role in Auth0."""
    url = f'https://{domain}/api/v2/roles'
    
    # Prepare role payload (only allowed fields)
    role_data = {
        'name': role_config['name'],
        'description': role_config.get('description', '')
    }
    
    try:
        response = requests.post(url, json=role_data, headers=headers)
        if response.status_code == 201:
            print(f"✓ Created role: {role_config['name']}")
            return response.json()['id']
        elif response.status_code == 409:
            print(f"→ Role already exists: {role_config['name']}")
            # Get existing role
            get_url = f'https://{domain}/api/v2/roles'
            response = requests.get(get_url, headers=headers)
            roles = response.json()['roles']
            for r in roles:
                if r['name'] == role_config['name']:
                    return r['id']
            return None
        else:
            response.raise_for_status()
    except Exception as e:
        print(f"✗ Error creating role {role_config['name']}: {e}")
        if hasattr(e, 'response'):
            print(f"Response: {e.response.text}")
        return None


def assign_permissions_to_role(domain, headers, role_id, permissions):
    """Assign permissions to a role."""
    # First, get the API identifier
    url = f'https://{domain}/api/v2/roles/{role_id}/permissions'
    
    # Get all permissions
    get_url = f'https://{domain}/api/v2/resource-servers'
    try:
        response = requests.get(get_url, headers=headers)
        resource_servers = response.json()
        
        # Find the Coffee Shop API
        api_identifier = None
        for rs in resource_servers:
            if 'coffee' in rs.get('name', '').lower() or 'dev' in rs.get('identifier', '').lower():
                api_identifier = rs.get('identifier')
                break
        
        if not api_identifier:
            print("⚠ Could not find API identifier. You may need to assign permissions manually.")
            return
        
        # Get permissions for this API
        permissions_url = f'https://{domain}/api/v2/permissions'
        response = requests.get(permissions_url, headers=headers, params={'per_page': 100})
        all_permissions = response.json().get('permissions', [])
        
        # Filter permissions for our API
        permission_ids = []
        for perm_name in permissions:
            for perm in all_permissions:
                if perm['value'] == perm_name and perm.get('resource_server_identifier') == api_identifier:
                    permission_ids.append(perm['name'])
                    break
        
        if permission_ids:
            # Update role permissions
            update_url = f'https://{domain}/api/v2/roles/{role_id}/permissions'
            requests.put(update_url, json={'permissions': permission_ids}, headers=headers)
            print(f"  ✓ Assigned {len(permission_ids)} permission(s)")
        
    except Exception as e:
        print(f"  ✗ Error assigning permissions: {e}")


def create_user(domain, headers, user_config):
    """Create a user in Auth0."""
    url = f'https://{domain}/api/v2/users'
    
    # Prepare user payload
    user_data = {
        'email': user_config['email'],
        'password': user_config['password'],
        'connection': user_config['connection']
    }
    
    # Add verify_email if specified
    if 'verify_email' in user_config:
        user_data['verify_email'] = user_config['verify_email']
    
    try:
        response = requests.post(url, json=user_data, headers=headers)
        if response.status_code == 201:
            print(f"✓ Created user: {user_config['email']}")
            return response.json()['user_id']
        elif response.status_code == 409:
            print(f"→ User already exists: {user_config['email']}")
            # Get existing user
            get_url = f'https://{domain}/api/v2/users'
            response = requests.get(get_url, headers=headers, params={'q': f'email:"{user_config["email"]}"'})
            users = response.json()['users']
            if users:
                return users[0]['user_id']
            return None
        else:
            response.raise_for_status()
    except Exception as e:
        print(f"✗ Error creating user {user_config['email']}: {e}")
        if hasattr(e, 'response'):
            print(f"Response: {e.response.text}")
        return None


def assign_role_to_user(domain, headers, user_id, role_name):
    """Assign a role to a user."""
    try:
        # Get role by name
        url = f'https://{domain}/api/v2/roles'
        response = requests.get(url, headers=headers)
        roles = response.json()['roles']
        
        role_id = None
        for role in roles:
            if role['name'] == role_name:
                role_id = role['id']
                break
        
        if not role_id:
            print(f"  ✗ Role not found: {role_name}")
            return False
        
        # Assign role to user
        assign_url = f'https://{domain}/api/v2/users/{user_id}/roles'
        requests.post(assign_url, json={'roles': [role_id]}, headers=headers)
        print(f"  ✓ Assigned role '{role_name}' to user")
        return True
        
    except Exception as e:
        print(f"  ✗ Error assigning role {role_name}: {e}")
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
    except json.JSONDecodeError as e:
        print(f"✗ Invalid JSON in config file: {e}")
        return 1
    
    # Get Management API token
    print("Getting Management API access token...")
    try:
        url = f'https://{args.domain}/oauth/token'
        payload = {
            'client_id': args.client_id,
            'client_secret': args.client_secret,
            'audience': f'https://{args.domain}/api/v2/',
            'grant_type': 'client_credentials'
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        access_token = response.json()['access_token']
        
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        
    except Exception as e:
        print(f"✗ Error getting access token: {e}")
        return 1
    
    # Create roles
    print("\n=== Creating Roles ===")
    role_ids = {}
    
    for role_config in config.get('roles', []):
        role_id = create_role(args.domain, headers, role_config)
        if role_id:
            role_ids[role_config['name']] = role_id
        
            # Assign permissions to role
            if 'permissions' in role_config:
                print(f"  Assigning permissions to {role_config['name']}...")
                assign_permissions_to_role(args.domain, headers, role_id, role_config['permissions'])
    
    # Create users
    print("\n=== Creating Users ===")
    
    for user_config in config.get('users', []):
        user_id = create_user(args.domain, headers, user_config)
        
        if user_id:
            # Assign roles to user
            if 'roles' in user_config:
                print(f"  Assigning roles to {user_config['email']}...")
                for role_name in user_config['roles']:
                    assign_role_to_user(args.domain, headers, user_id, role_name)
    
    print("\n✓ Setup complete!")
    print("\nUsers created:")
    for user_config in config.get('users', []):
        print(f"  - {user_config['email']} (Password: {user_config.get('password', 'Check Auth0')})")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
