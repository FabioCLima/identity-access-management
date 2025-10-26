#!/bin/bash

# Get JWT Token from Auth0 for Testing
# This script helps you obtain a JWT token from Auth0 for testing purposes

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "Auth0 JWT Token Generator for Coffee Shop API"
echo "=============================================="
echo ""

# Prompt for Auth0 credentials
read -p "Enter your Auth0 domain (e.g., udacity-fsnd.auth0.com): " AUTH0_DOMAIN
read -p "Enter your Auth0 Client ID: " CLIENT_ID
read -p "Enter your Auth0 Client Secret: " CLIENT_SECRET
read -p "Enter your API Audience: " API_AUDIENCE
read -p "Enter grant type (authorization_code/password/client_credentials) [client_credentials]: " GRANT_TYPE
GRANT_TYPE=${GRANT_TYPE:-client_credentials}

echo ""
echo "Requesting token from Auth0..."
echo ""

# Make the request
RESPONSE=$(curl -s -X POST "https://${AUTH0_DOMAIN}/oauth/token" \
  -H "Content-Type: application/json" \
  -d "{
    \"client_id\": \"${CLIENT_ID}\",
    \"client_secret\": \"${CLIENT_SECRET}\",
    \"audience\": \"${API_AUDIENCE}\",
    \"grant_type\": \"${GRANT_TYPE}\"
  }")

# Check if request was successful
if echo "$RESPONSE" | grep -q "access_token"; then
    # Extract the token
    TOKEN=$(echo "$RESPONSE" | grep -o '"access_token":"[^"]*' | cut -d'"' -f4)
    
    echo -e "${GREEN}✓ Token obtained successfully!${NC}"
    echo ""
    echo "Your JWT Token:"
    echo "$TOKEN"
    echo ""
    echo -e "${YELLOW}Note: Save this token for use in Postman collection${NC}"
    echo ""
    echo "To use this token in the collection:"
    echo "  python update_postman_auth.py <collection_file> <barista_token> <manager_token>"
    
    # Save token to file
    echo "$TOKEN" > auth0_token.txt
    echo -e "${GREEN}Token saved to auth0_token.txt${NC}"
else
    echo -e "${RED}✗ Error obtaining token${NC}"
    echo ""
    echo "Response from Auth0:"
    echo "$RESPONSE"
    exit 1
fi

