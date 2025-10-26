#!/usr/bin/env python3
"""
Update Postman Collection with JWT Tokens

This script helps update the Postman collection with JWT tokens for Barista and Manager roles.

Usage:
    python update_postman_auth.py <collection_file> <barista_token> <manager_token>

Example:
    python update_postman_auth.py udacity-fsnd-udaspicelatte.postman_collection.json \
        <barista_jwt_token> <manager_jwt_token>
"""

import json
import sys
import os


def update_collection_auth(collection_file, barista_token, manager_token):
    """
    Update Postman collection with JWT tokens for Barista and Manager roles.
    
    Args:
        collection_file: Path to the Postman collection JSON file
        barista_token: JWT token for Barista role
        manager_token: JWT token for Manager role
    """
    # Read the collection file
    try:
        with open(collection_file, 'r') as f:
            collection = json.load(f)
    except FileNotFoundError:
        print(f"Error: Collection file '{collection_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in collection file: {e}")
        sys.exit(1)
    
    # Find and update barista and manager folders
    for folder in collection.get('item', []):
        folder_name = folder.get('name', '').lower()
        
        if folder_name == 'barista':
            update_folder_auth(folder, barista_token, 'Barista')
            print(f"✓ Updated Barista folder with token")
        
        elif folder_name == 'manager':
            update_folder_auth(folder, manager_token, 'Manager')
            print(f"✓ Updated Manager folder with token")
    
    # Write the updated collection back
    output_file = collection_file
    with open(output_file, 'w') as f:
        json.dump(collection, f, indent='\t')
    
    print(f"\n✓ Collection updated: {output_file}")
    print("\nNext steps:")
    print("1. Import the updated collection into Postman")
    print("2. Test the endpoints with the new tokens")
    print("3. Export the collection to share with the team")


def update_folder_auth(folder, token, role_name):
    """
    Update authorization for all requests in a folder.
    
    Args:
        folder: Postman collection folder object
        token: JWT token to use
        role_name: Name of the role (for display)
    """
    # Update folder-level auth if it exists
    if 'auth' not in folder:
        folder['auth'] = {}
    
    folder['auth'] = {
        'type': 'bearer',
        'bearer': [
            {
                'key': 'token',
                'value': token,
                'type': 'string'
            }
        ]
    }
    
    # Update individual requests in the folder
    for item in folder.get('item', []):
        if 'request' in item:
            if 'auth' not in item['request']:
                item['request']['auth'] = {}
            
            item['request']['auth'] = {
                'type': 'bearer',
                'bearer': [
                    {
                        'key': 'token',
                        'value': token,
                        'type': 'string'
                    }
                ]
            }


def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) != 4:
        print("Usage: python update_postman_auth.py <collection_file> <barista_token> <manager_token>")
        print("\nExample:")
        print("  python update_postman_auth.py udacity-fsnd-udaspicelatte.postman_collection.json \\")
        print("    eyJhbGci... <barista_token> \\")
        print("    eyJhbGci... <manager_token>")
        sys.exit(1)
    
    collection_file = sys.argv[1]
    barista_token = sys.argv[2]
    manager_token = sys.argv[3]
    
    # Validate tokens are provided
    if not barista_token or barista_token == 'YOUR_BARISTA_TOKEN':
        print("Error: Please provide a valid Barista JWT token")
        sys.exit(1)
    
    if not manager_token or manager_token == 'YOUR_MANAGER_TOKEN':
        print("Error: Please provide a valid Manager JWT token")
        sys.exit(1)
    
    update_collection_auth(collection_file, barista_token, manager_token)


if __name__ == '__main__':
    main()

