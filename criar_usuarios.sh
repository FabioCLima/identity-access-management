#!/bin/bash

# Script para criar usuários, roles e permissões no Auth0

AUTH0_DOMAIN="dev-huk2wemon6z8ehay.us.auth0.com"
CLIENT_ID="Etb0Gtox8fnGn0MO4RduJujS3f0QBDS6"
CLIENT_SECRET="HlJ-RQ349SHfASDYXA6uAjyemcgVDu-B6ioRqxXL2w1didLntU_c9Ky6MlcAb5ie"

echo "=================================================="
echo "CRIAR USUÁRIOS E ROLES NO AUTH0"
echo "=================================================="
echo

# 1. Obter Access Token
echo "1. Obtendo access token..."
TOKEN_RESPONSE=$(curl -s --request POST \
  --url https://${AUTH0_DOMAIN}/oauth/token \
  --header 'content-type: application/json' \
  --data "{
    \"client_id\":\"${CLIENT_ID}\",
    \"client_secret\":\"${CLIENT_SECRET}\",
    \"audience\":\"https://${AUTH0_DOMAIN}/api/v2/\",
    \"grant_type\":\"client_credentials\"
  }")

ACCESS_TOKEN=$(echo $TOKEN_RESPONSE | grep -o '"access_token":"[^"]*' | cut -d'"' -f4)

if [ -z "$ACCESS_TOKEN" ]; then
    echo "❌ Erro ao obter access token"
    echo "$TOKEN_RESPONSE"
    exit 1
fi

echo "✅ Access token obtido"
echo

# 2. Criar Usuário Barista
echo "2. Criando usuário barista..."
BARISTA_RESPONSE=$(curl -s --request POST \
  --url https://${AUTH0_DOMAIN}/api/v2/users \
  --header "authorization: Bearer ${ACCESS_TOKEN}" \
  --header 'content-type: application/json' \
  --data '{
    "email": "barista@coffeeshop.com",
    "password": "CoffeeShop2024!",
    "connection": "Username-Password-Authentication",
    "email_verified": true,
    "name": "Coffee Barista"
  }')

BARISTA_USER_ID=$(echo $BARISTA_RESPONSE | grep -o '"user_id":"[^"]*' | cut -d'"' -f4)

if [ -z "$BARISTA_USER_ID" ]; then
    echo "❌ Erro ao criar barista"
    echo "$BARISTA_RESPONSE"
    exit 1
fi

echo "✅ Barista criado (ID: $BARISTA_USER_ID)"
echo

# 3. Criar Usuário Manager
echo "3. Criando usuário manager..."
MANAGER_RESPONSE=$(curl -s --request POST \
  --url https://${AUTH0_DOMAIN}/api/v2/users \
  --header "authorization: Bearer ${ACCESS_TOKEN}" \
  --header 'content-type: application/json' \
  --data '{
    "email": "manager@coffeeshop.com",
    "password": "CoffeeShop2024!",
    "connection": "Username-Password-Authentication",
    "email_verified": true,
    "name": "Coffee Manager"
  }')

MANAGER_USER_ID=$(echo $MANAGER_RESPONSE | grep -o '"user_id":"[^"]*' | cut -d'"' -f4)

if [ -z "$MANAGER_USER_ID" ]; then
    echo "❌ Erro ao criar manager"
    echo "$MANAGER_RESPONSE"
    exit 1
fi

echo "✅ Manager criado (ID: $MANAGER_USER_ID)"
echo

# 4. Criar Role Barista
echo "4. Criando role Barista..."
BARISTA_ROLE_RESPONSE=$(curl -s --request POST \
  --url https://${AUTH0_DOMAIN}/api/v2/roles \
  --header "authorization: Bearer ${ACCESS_TOKEN}" \
  --header 'content-type: application/json' \
  --data '{
    "name": "Barista",
    "description": "Can view drink details"
  }')

BARISTA_ROLE_ID=$(echo $BARISTA_ROLE_RESPONSE | grep -o '"id":"[^"]*' | cut -d'"' -f4)

if [ -z "$BARISTA_ROLE_ID" ]; then
    echo "❌ Erro ao criar role Barista"
    echo "$BARISTA_ROLE_RESPONSE"
    exit 1
fi

echo "✅ Role Barista criado (ID: $BARISTA_ROLE_ID)"
echo

# 5. Criar Role Manager
echo "5. Criando role Manager..."
MANAGER_ROLE_RESPONSE=$(curl -s --request POST \
  --url https://${AUTH0_DOMAIN}/api/v2/roles \
  --header "authorization: Bearer ${ACCESS_TOKEN}" \
  --header 'content-type: application/json' \
  --data '{
    "name": "Manager",
    "description": "Can manage all drinks"
  }')

MANAGER_ROLE_ID=$(echo $MANAGER_ROLE_RESPONSE | grep -o '"id":"[^"]*' | cut -d'"' -f4)

if [ -z "$MANAGER_ROLE_ID" ]; then
    echo "❌ Erro ao criar role Manager"
    echo "$MANAGER_ROLE_RESPONSE"
    exit 1
fi

echo "✅ Role Manager criado (ID: $MANAGER_ROLE_ID)"
echo

# 6. Adicionar permissions ao Role Barista
echo "6. Adicionando permissions ao role Barista..."
curl -s --request POST \
  --url https://${AUTH0_DOMAIN}/api/v2/roles/${BARISTA_ROLE_ID}/permissions \
  --header "authorization: Bearer ${ACCESS_TOKEN}" \
  --header 'content-type: application/json' \
  --data '{
    "permissions": [
      {
        "resource_server_identifier": "coffee-shop-api",
        "permission_name": "get:drinks"
      },
      {
        "resource_server_identifier": "coffee-shop-api",
        "permission_name": "get:drinks-detail"
      }
    ]
  }' > /dev/null

echo "✅ Permissions adicionadas ao role Barista"
echo

# 7. Adicionar permissions ao Role Manager
echo "7. Adicionando permissions ao role Manager..."
curl -s --request POST \
  --url https://${AUTH0_DOMAIN}/api/v2/roles/${MANAGER_ROLE_ID}/permissions \
  --header "authorization: Bearer ${ACCESS_TOKEN}" \
  --header 'content-type: application/json' \
  --data '{
    "permissions": [
      {
        "resource_server_identifier": "coffee-shop-api",
        "permission_name": "get:drinks"
      },
      {
        "resource_server_identifier": "coffee-shop-api",
        "permission_name": "get:drinks-detail"
      },
      {
        "resource_server_identifier": "coffee-shop-api",
        "permission_name": "post:drinks"
      },
      {
        "resource_server_identifier": "coffee-shop-api",
        "permission_name": "patch:drinks"
      },
      {
        "resource_server_identifier": "coffee-shop-api",
        "permission_name": "delete:drinks"
      }
    ]
  }' > /dev/null

echo "✅ Permissions adicionadas ao role Manager"
echo

# 8. Atribuir role ao usuário Barista
echo "8. Atribuindo role Barista ao usuário..."
curl -s --request POST \
  --url https://${AUTH0_DOMAIN}/api/v2/users/${BARISTA_USER_ID}/roles \
  --header "authorization: Bearer ${ACCESS_TOKEN}" \
  --header 'content-type: application/json' \
  --data "{\"roles\": [\"${BARISTA_ROLE_ID}\"]}" > /dev/null

echo "✅ Role Barista atribuído ao usuário"
echo

# 9. Atribuir role ao usuário Manager
echo "9. Atribuindo role Manager ao usuário..."
curl -s --request POST \
  --url https://${AUTH0_DOMAIN}/api/v2/users/${MANAGER_USER_ID}/roles \
  --header "authorization: Bearer ${ACCESS_TOKEN}" \
  --header 'content-type: application/json' \
  --data "{\"roles\": [\"${MANAGER_ROLE_ID}\"]}" > /dev/null

echo "✅ Role Manager atribuído ao usuário"
echo

echo "=================================================="
echo "✅ TUDO CONCLUÍDO COM SUCESSO!"
echo "=================================================="
echo
echo "Credenciais de teste:"
echo "  Barista: barista@coffeeshop.com / CoffeeShop2024!"
echo "  Manager: manager@coffeeshop.com / CoffeeShop2024!"
echo
echo "Agora você pode fazer login com estes usuários!"

