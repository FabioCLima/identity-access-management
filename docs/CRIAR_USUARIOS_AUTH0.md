# 👥 Criar Usuários no Auth0 via Management API

## 📋 Pré-requisitos

### 1. Obter Access Token (Auth0 Management API)

Você já tem a Machine to Machine Application criada:
- Client ID: `KNT5h1CaoPmZ11CzALx6uPyX0NuwSbRx`
- Client Secret: `Ze8JJSCkFizTC9p7qj11URxap7BkViPuW6i8g8RqrK7U77s7ELxSSH_o7tJUNRa`

### 2. Get Management API Token

```bash
curl --request POST \
  --url https://dev-huk2wemon6z8ehay.us.auth0.com/oauth/token \
  --header 'content-type: application/json' \
  --data '{
    "client_id":"KNT5h1CaoPmZ11CzALx6uPyX0NuwSbRx",
    "client_secret":"Ze8JJSCkFizTC9p7qj11URxap7BkViPuW6i8g8RqrK7U77s7ELxSSH_o7tJUNRa",
    "audience":"https://dev-huk2wemon6z8ehay.us.auth0.com/api/v2/",
    "grant_type":"client_credentials"
  }'
```

**Salvar o access_token do JSON de resposta!**

---

## 👤 Criar Usuários via API

### Script 1: Criar Usuário Barista

```bash
curl --request POST \
  --url https://dev-huk2wemon6z8ehay.us.auth0.com/api/v2/users \
  --header 'authorization: Bearer YOUR_ACCESS_TOKEN' \
  --header 'content-type: application/json' \
  --data '{
    "email": "barista@coffeeshop.com",
    "password": "CoffeeShop2024!",
    "connection": "Username-Password-Authentication",
    "email_verified": true,
    "name": "Coffee Barista"
  }'
```

### Script 2: Criar Usuário Manager

```bash
curl --request POST \
  --url https://dev-huk2wemon6z8ehay.us.auth0.com/api/v2/users \
  --header 'authorization: Bearer YOUR_ACCESS_TOKEN' \
  --header 'content-type: application/json' \
  --data '{
    "email": "manager@coffeeshop.com",
    "password": "CoffeeShop2024!",
    "connection": "Username-Password-Authentication",
    "email_verified": true,
    "name": "Coffee Manager"
  }'
```

---

## 🎭 Criar Roles

### 1. Criar Role: Barista

```bash
curl --request POST \
  --url https://dev-huk2wemon6z8ehay.us.auth0.com/api/v2/roles \
  --header 'authorization: Bearer YOUR_ACCESS_TOKEN' \
  --header 'content-type: application/json' \
  --data '{
    "name": "Barista",
    "description": "Can view drink details"
  }'
```

### 2. Criar Role: Manager

```bash
curl --request POST \
  --url https://dev-huk2wemon6z8ehay.us.auth0.com/api/v2/roles \
  --header 'authorization: Bearer YOUR_ACCESS_TOKEN' \
  --header 'content-type: application/json' \
  --data '{
    "name": "Manager",
    "description": "Can manage all drinks"
  }'
```

---

## 🔐 Adicionar Permissões aos Roles

Primeiro, **perguntar quais role IDs foram criados:**

```bash
# Listar roles
curl --request GET \
  --url https://dev-huk2wemon6z8ehay.us.auth0.com/api/v2/roles \
  --header 'authorization: Bearer YOUR_ACCESS_TOKEN'
```

### Depois, adicionar permissions (substituir ROLE_ID):

**Barista Role:**
```bash
curl --request PATCH \
  --url https://dev-huk2wemon6z8ehay.us.auth0.com/api/v2/roles/ROLE_ID_BARISTA \
  --header 'authorization: Bearer YOUR_ACCESS_TOKEN' \
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
  }'
```

**Manager Role:**
```bash
curl --request PATCH \
  --url https://dev-huk2wemon6z8ehay.us.auth0.com/api/v2/roles/ROLE_ID_MANAGER \
  --header 'authorization: Bearer YOUR_ACCESS_TOKEN' \
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
  }'
```

---

## 👤 Atribuir Roles a Usuários

Primeiro, pegar o **user_id** dos usuários criados:

```bash
# Listar usuários
curl --request GET \
  --url https://dev-huk2wemon6z8ehay.us.auth0.com/api/v2/users \
  --header 'authorization: Bearer YOUR_ACCESS_TOKEN'
```

### Atribuir role ao usuário (substituir USER_ID e ROLE_ID):

```bash
curl --request POST \
  --url https://dev-huk2wemon6z8ehay.us.auth0.com/api/v2/users/USER_ID/roles \
  --header 'authorization: Bearer YOUR_ACCESS_TOKEN' \
  --header 'content-type: application/json' \
  --data '{
    "roles": ["ROLE_ID"]
  }'
```

---

## 📝 Resumo dos Passos

1. ✅ Get Management API Token
2. ✅ Criar Usuário Barista
3. ✅ Criar Usuário Manager
4. ✅ Criar Role Barista
5. ✅ Criar Role Manager
6. ✅ Listar Roles (pegar IDs)
7. ✅ Adicionar Permissions ao Role Barista
8. ✅ Adicionar Permissions ao Role Manager
9. ✅ Listar Users (pegar IDs)
10. ✅ Atribuir Role ao Usuário Barista
11. ✅ Atribuir Role ao Usuário Manager

---

## 🔧 Script Python Simplificado

Vou criar um script Python que faz tudo automaticamente...

