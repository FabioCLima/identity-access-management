# Auth0 Setup and Postman Collection Configuration

## Overview

This guide will help you:
1. Get JWT tokens from Auth0 for Barista and Manager roles
2. Update the Postman collection with proper authentication
3. Test all endpoints with the appropriate permissions

## Step 1: Setup Auth0 (if not already done)

### 1.1 Create Auth0 Account
1. Go to https://auth0.com and sign up
2. Create a new tenant
3. Note your domain: dev-huk2wemon6z8ehay

### 1.2 Create an API
1. In Auth0 Dashboard, go to **Applications > APIs**
2. Click **"Create API"**
3. Name: `Coffee Shop API`
4. Identifier: `coffee-shop-api` (or your choice)
5. Click **"Create"**

### 1.3 Enable RBAC and Permissions
1. In your API settings:
   - Enable **RBAC** (Role-Based Access Control)
   - Enable **"Add Permissions in the Access Token"**
2. Click **"Save Changes"**

### 1.4 Create API Permissions
Go to the **Permissions** tab and create:
- `get:drinks-detail`
- `get:drinks`
- `post:drinks`
- `patch:drinks`
- `delete:drinks`

### 1.5 Create Roles
Go to **User Management > Roles** and create:

#### Barista Role
- **Name:** Barista
- **Description:** Can view drink details
- **Permissions:**
  - `get:drinks`
  - `get:drinks-detail`

#### Manager Role
- **Name:** Manager
- **Description:** Can perform all actions
- **Permissions:**
  - `get:drinks`
  - `get:drinks-detail`
  - `post:drinks`
  - `patch:drinks`
  - `delete:drinks`

### 1.6 Create Users and Assign Roles

You have two options to create users and roles:

#### Option A: Using the Management API (Automated - Recommended)

**Using the setup script with JSON configuration:**

1. Update the configuration file `backend/auth0_users_template.json`:
   ```json
   {
     "roles": [...],
     "users": [
       {
         "email": "barista@test.com",
         "password": "SecurePassword123!",
         "connection": "Username-Password-Authentication",
         "roles": ["Barista"]
       },
       {
         "email": "manager@test.com",
         "password": "SecurePassword123!",
         "connection": "Username-Password-Authentication",
         "roles": ["Manager"]
       }
     ]
   }
   ```

2. Get your Management API credentials:
   - Go to **Applications** in Auth0 Dashboard
   - Create a Machine to Machine Application
   - Authorize it for the Management API
   - Note down the Client ID and Client Secret

3. Run the setup script:
   ```bash
   cd backend
   source .venv/bin/activate
   pip install auth0-python  # if not already installed
   
   python setup_auth0.py \
     --domain your-tenant.auth0.com \
     --client-id YOUR_CLIENT_ID \
     --client-secret YOUR_CLIENT_SECRET \
     --config auth0_users_template.json
   ```

4. The script will automatically:
   - Create all roles with permissions
   - Create all users
   - Assign roles to users
   - Print success messages

#### Option B: Using Auth0 Dashboard (Manual)

1. Go to **User Management > Users**
2. Click **"Create User"**
3. Create two test users:
   - **User 1:** barista@test.com (assign Barista role)
   - **User 2:** manager@test.com (assign Manager role)

## Step 2: Get JWT Tokens

You have two options:

### Option A: Using Auth0 Dashboard (Manual)

1. Go to your Auth0 Dashboard
2. Test your API connection using curl or Postman
3. Use the following command to get a token:

```bash
curl --request POST \
  --url https://YOUR-AUTH0-DOMAIN/oauth/token \
  --header 'content-type: application/json' \
  --data '{
    "client_id":"YOUR_CLIENT_ID",
    "client_secret":"YOUR_CLIENT_SECRET",
    "audience":"YOUR_API_AUDIENCE",
    "grant_type":"client_credentials"
  }'
```

### Option B: Using Postman's OAuth 2.0 Helper

1. In Postman, create a new request
2. Go to **Authorization** tab
3. Select **OAuth 2.0**
4. Click **"Get New Access Token"**
5. Configure:
   - **Token Name:** Coffee Shop Token
   - **Grant Type:** Authorization Code
   - **Callback URL:** http://localhost:5000
   - **Auth URL:** `https://YOUR-AUTH0-DOMAIN/authorize`
   - **Access Token URL:** `https://YOUR-AUTH0-DOMAIN/oauth/token`
   - **Client ID:** Your Auth0 client ID
   - **Client Secret:** Your Auth0 client secret
   - **Scope:** Select all permissions
6. Click **"Get New Access Token"**
7. Copy the token

## Step 3: Update Postman Collection with JWT Tokens

### Method 1: Using Collection Authorization (Recommended)

1. Open the Postman collection: `udacity-fsnd-udaspicelatte.postman_collection.json`

2. Right-click on the **"barista"** folder
   - Go to **"Edit"**
   - Go to **"Authorization"** tab
   - **Type:** Bearer Token
   - **Token:** Paste your Barista JWT token
   - Click **"Save"**

3. Repeat for the **"manager"** folder
   - Right-click on **"manager"** folder
   - Go to **"Edit"**
   - Go to **"Authorization"** tab
   - **Type:** Bearer Token
   - **Token:** Paste your Manager JWT token
   - Click **"Save"**

### Method 2: Using Environment Variables

1. Create a new Environment in Postman
2. Add variables:
   - `host`: `http://localhost:5000`
   - `barista_token`: Your Barista JWT token
   - `manager_token`: Your Manager JWT token

3. Update collection requests to use:
   - Authorization: Bearer Token
   - Token: `{{barista_token}}` or `{{manager_token}}`

## Step 4: Export Updated Collection

1. Click on the collection name in Postman
2. Click the **"..."** menu (three dots)
3. Select **"Export"**
4. Choose **Collection v2.1**
5. Save as: `udacity-fsnd-udaspicelatte.postman_collection.json`

Replace the existing file in the backend directory.

## Step 5: Test the Endpoints

### Public Endpoint (No Auth Required)
- GET `/drinks` - Should return all drinks in short form

### Barista Endpoints (Protected)
- GET `/drinks` - Should return all drinks (short form)
- GET `/drinks-detail` - Should return all drinks with full recipe details

### Manager Endpoints (Protected)
- GET `/drinks` - Should return all drinks
- GET `/drinks-detail` - Should return all drinks with details
- POST `/drinks` - Should create a new drink
- PATCH `/drinks/:id` - Should update a drink
- DELETE `/drinks/:id` - Should delete a drink

## Example JWT Token Structure

A typical JWT from Auth0 looks like:
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1ESTNPVFEzTXpFdE16RTVNRFE1T1RZM05URTROVFJFTVRBM05EQXpSVGsyTVRFeU1UY3pNQSJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktZnNuZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjUyMWU0Njg2OWUxNmE4NDFhYzg3MWE1IiwiYXVkIjpudWxsLCJleHAiOjE3MjM0NTY3ODksImlhdCI6MTcyMzQyMDc4OSwicGVybWlzc2lvbnMiOlsiZ2V0OmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicG9zdDpkcmlua3MiLCJwYXRjaDpkcmlua3MiLCJkZWxldGU6ZHJpbmtzIl19.xyz...
```

## Troubleshooting

### "401 Unauthorized" Error
- Verify the JWT token is valid
- Check token hasn't expired
- Ensure correct permissions are set in Auth0

### "403 Forbidden" Error
- Verify the user has the correct role
- Check permissions are enabled for the role
- Ensure "Add Permissions in the Access Token" is enabled

### "422 Unprocessable" Error
- Check request body format
- Verify required fields are provided
- Check recipe format is correct

## Quick Reference Commands

### Get Token for Testing
```bash
curl -X POST https://YOUR-AUTH0-DOMAIN/oauth/token \
  -H "Content-Type: application/json" \
  -d '{
    "client_id":"YOUR_CLIENT_ID",
    "client_secret":"YOUR_CLIENT_SECRET",
    "audience":"coffee-shop-api",
    "grant_type":"client_credentials"
  }'
```

### Test Public Endpoint
```bash
curl http://localhost:5000/drinks
```

### Test Protected Endpoint
```bash
curl -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  http://localhost:5000/drinks-detail
```

