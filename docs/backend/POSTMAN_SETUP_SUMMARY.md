# Postman Collection Setup - Quick Summary

## Overview

This guide helps you set up authentication for the Coffee Shop API Postman collection with real JWT tokens for Barista and Manager roles.

## Prerequisites

✅ Auth0 account created  
✅ API created in Auth0 with RBAC enabled  
✅ Roles created (Barista and Manager)  
✅ Users created and assigned to roles  
✅ Permissions configured  

## Step-by-Step Process

### 1. Get JWT Tokens from Auth0

You need to obtain JWT tokens for:
- **Barista role** user
- **Manager role** user

#### Option A: Using the Helper Script (Recommended)

```bash
cd ~/Workdir/udacity_projects/identity-access-management/coffee-shop/backend

# Run the interactive script
./get_auth0_token.sh
```

This will prompt you for:
- Auth0 domain
- Client ID
- Client Secret
- API Audience

It will generate and save the token to `auth0_token.txt`.

#### Option B: Manual cURL Request

```bash
curl -X POST https://YOUR-DOMAIN.auth0.com/oauth/token \
  -H "Content-Type: application/json" \
  -d '{
    "client_id":"YOUR_CLIENT_ID",
    "client_secret":"YOUR_CLIENT_SECRET",
    "audience":"YOUR_API_AUDIENCE",
    "grant_type":"client_credentials"
  }'
```

Repeat for both Barista and Manager users.

### 2. Update Postman Collection

Once you have both tokens, update the collection:

```bash
cd ~/Workdir/udacity_projects/identity-access-management/coffee-shop/backend

python update_postman_auth.py \
  udacity-fsnd-udaspicelatte.postman_collection.json \
  <barista_jwt_token> \
  <manager_jwt_token>
```

This will:
- Update the "barista" folder with Barista JWT
- Update the "manager" folder with Manager JWT
- Save the updated collection

### 3. Import Collection into Postman

1. Open Postman
2. Click **Import** button
3. Select `udacity-fsnd-udaspicelatte.postman_collection.json`
4. Click **Import**

### 4. Test the Endpoints

The collection has three main folders:

#### Public (No Auth)
- ✅ GET /drinks

#### Barista (Protected with JWT)
- ✅ GET /drinks
- ✅ GET /drinks-detail

#### Manager (Protected with JWT)
- ✅ GET /drinks
- ✅ GET /drinks-detail
- ✅ POST /drinks
- ✅ PATCH /drinks/:id
- ✅ DELETE /drinks/:id

## Expected Results

### Successful Tests
- All public endpoints return 200 OK
- All barista endpoints return 200 OK with drink details
- All manager endpoints return 200 OK with appropriate responses

### Error Handling
The collection should handle:
- 401 Unauthorized (invalid/missing token)
- 403 Forbidden (wrong permissions)
- 404 Not Found (invalid drink ID)
- 422 Unprocessable (validation errors)

## Quick Reference

### Start Flask Server
```bash
cd backend/src
source ../.venv/bin/activate
export FLASK_APP=api.py
flask run --reload
```

### Get Auth0 Token (Script)
```bash
./get_auth0_token.sh
```

### Update Postman Collection
```bash
python update_postman_auth.py collection.json barista_token manager_token
```

### Test Public Endpoint
```bash
curl http://localhost:5000/drinks
```

### Test Protected Endpoint
```bash
curl -H "Authorization: Bearer $TOKEN" http://localhost:5000/drinks-detail
```

## Troubleshooting

### Token Issues
- **401 Unauthorized**: Token expired or invalid. Get a new token.
- **403 Forbidden**: User doesn't have required permissions.

### Server Issues
- **Connection refused**: Flask server not running. Start it with `flask run`.
- **500 Internal Error**: Check server logs for details.

### Collection Issues
- **Not importing**: Make sure JSON format is valid.
- **Token not working**: Verify tokens are correctly added to folders.

## Documentation Files

- `AUTH0_SETUP.md` - Complete Auth0 setup guide
- `TESTING_GUIDE.md` - Comprehensive testing documentation
- `get_auth0_token.sh` - Helper script to get tokens
- `update_postman_auth.py` - Script to update collection with tokens

## Next Steps

After setting up the collection:

1. ✅ Test all public endpoints
2. ✅ Test all barista endpoints
3. ✅ Test all manager endpoints
4. ✅ Verify CRUD operations work
5. ✅ Export and save the updated collection

## Support

For issues or questions:
1. Check `AUTH0_SETUP.md` for Auth0 configuration
2. Check `TESTING_GUIDE.md` for testing examples
3. Review Flask server logs for errors
4. Verify Auth0 dashboard configuration

