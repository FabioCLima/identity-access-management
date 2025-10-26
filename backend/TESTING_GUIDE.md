# Testing Guide - Coffee Shop API

## Quick Start

### 1. Start the Flask Server

```bash
cd ~/Workdir/udacity_projects/identity-access-management/coffee-shop/backend
source .venv/bin/activate
cd src
export FLASK_APP=api.py
flask run --reload
```

The server will start on `http://localhost:5000`

### 2. Test Public Endpoint (No Auth Required)

```bash
curl http://localhost:5000/drinks
```

Expected Response:
```json
{
  "success": true,
  "drinks": []
}
```

### 3. Get Auth0 JWT Tokens

#### Option A: Using the Helper Script

```bash
cd ~/Workdir/udacity_projects/identity-access-management/coffee-shop/backend
./get_auth0_token.sh
```

Follow the prompts to enter:
- Auth0 domain
- Client ID
- Client Secret
- API Audience

#### Option B: Manual Request

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

### 4. Update Postman Collection

Once you have the JWT tokens:

```bash
cd ~/Workdir/udacity_projects/identity-access-management/coffee-shop/backend

# Update the collection with your tokens
python update_postman_auth.py \
  udacity-fsnd-udaspicelatte.postman_collection.json \
  <barista_jwt_token> \
  <manager_jwt_token>
```

### 5. Import Collection into Postman

1. Open Postman
2. Click **Import**
3. Select the updated collection file
4. Click **Import**

### 6. Test Endpoints

#### Public Endpoint
- Folder: **public**
- Request: GET `/drinks`
- Expected: 200 OK with drinks array

#### Barista Endpoints
- Folder: **barista**
- Request: GET `/drinks`
- Request: GET `/drinks-detail`
- Expected: 200 OK with drinks array

#### Manager Endpoints
- Folder: **manager**
- Request: GET `/drinks`
- Request: GET `/drinks-detail`
- Request: POST `/drinks` (with body)
- Request: PATCH `/drinks/:id` (with body)
- Request: DELETE `/drinks/:id`
- Expected: 200 OK for all operations

## Manual Testing with cURL

### Test with Barista Token

```bash
TOKEN="your_barista_token_here"

# Get drinks detail (requires auth)
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:5000/drinks-detail
```

### Test with Manager Token

```bash
TOKEN="your_manager_token_here"

# Create a new drink
curl -X POST http://localhost:5000/drinks \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Espresso",
    "recipe": [
      {"name": "espresso", "color": "brown", "parts": 1}
    ]
  }'

# Update a drink
curl -X PATCH http://localhost:5000/drinks/1 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Espresso"
  }'

# Delete a drink
curl -X DELETE http://localhost:5000/drinks/1 \
  -H "Authorization: Bearer $TOKEN"
```

## Expected Test Results

### Success Cases

| Endpoint | Method | Auth | Expected Status |
|---------|--------|------|----------------|
| /drinks | GET | None | 200 OK |
| /drinks-detail | GET | Barista/Manager | 200 OK |
| /drinks | POST | Manager | 200 OK |
| /drinks/:id | PATCH | Manager | 200 OK |
| /drinks/:id | DELETE | Manager | 200 OK |

### Error Cases

| Scenario | Expected Status |
|----------|----------------|
| Missing auth on protected endpoint | 401 Unauthorized |
| Wrong permissions | 403 Forbidden |
| Invalid drink ID | 404 Not Found |
| Invalid request body | 400 Bad Request |
| Duplicate drink title | 422 Unprocessable |

## Postman Collection Test Scripts

The Postman collection includes automatic tests for each endpoint:

### Public Endpoint Tests
- Status code is 200
- Response contains drinks array

### Barista Endpoint Tests
- Status code is 200
- Response contains drinks array
- Drinks contain full recipe details

### Manager Endpoint Tests
- Status code is 200
- Response contains success field
- Created drink has correct data
- Updated drink has new data
- Deleted drink returns correct ID

## Running the Full Test Suite

### Using Postman Runner

1. In Postman, click on the collection
2. Click **"Run"** button
3. Select environment (if applicable)
4. Click **"Run udacity-fsnd-udaspicelatte"**
5. Review test results

### Using Newman (Command Line)

```bash
# Install Newman (if not installed)
npm install -g newman

# Run the collection
newman run udacity-fsnd-udaspicelatte.postman_collection.json \
  --environment local.json \
  --reporters cli,json,html
```

## Troubleshooting

### Server Not Running
```bash
# Check if Flask is running
curl http://localhost:5000/drinks

# If error, start the server
cd backend/src
export FLASK_APP=api.py
flask run --reload
```

### Token Expired
```bash
# Get a new token
./get_auth0_token.sh

# Update the collection
python update_postman_auth.py ...
```

### 401 Unauthorized
- Check token is correct
- Verify token hasn't expired
- Ensure correct permissions in Auth0

### 403 Forbidden
- Check user has correct role
- Verify permissions are enabled
- Ensure "Add Permissions in the Access Token" is enabled

### 422 Unprocessable
- Check request body format
- Verify required fields are present
- Check recipe structure matches expected format

## Test Data Examples

### Create Drink Request Body
```json
{
  "title": "Latte",
  "recipe": [
    {"name": "espresso", "color": "brown", "parts": 2},
    {"name": "steamed_milk", "color": "white", "parts": 3}
  ]
}
```

### Update Drink Request Body
```json
{
  "title": "Caffè Latte"
}
```

Or update recipe:
```json
{
  "recipe": [
    {"name": "espresso", "color": "brown", "parts": 1},
    {"name": "steamed_milk", "color": "white", "parts": 2}
  ]
}
```

