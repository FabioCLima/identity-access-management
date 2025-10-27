#!/usr/bin/env python3
"""
Script para criar usuários, roles e permissões no Auth0 via Management API
"""

import requests
import json

# Configuração Auth0
AUTH0_DOMAIN = "dev-huk2wemon6z8ehay.us.auth0.com"
CLIENT_ID = "KNT5h1CaoPmZ11CzALx6uPyX0NuwSbRx"
CLIENT_SECRET = "Ze8JJSCkFizTC9p7qj11URxap7BkViPuW6i8g8RqrK7U77s7ELxSSH_o7tJUNRa"
AUDIENCE = f"https://{AUTH0_DOMAIN}/api/v2/"

# Variáveis globais
access_token = None
role_barista_id = None
role_manager_id = None


def get_management_token():
    """Obter access token da Management API"""
    global access_token
    
    url = f"https://{AUTH0_DOMAIN}/oauth/token"
    headers = {"content-type": "application/json"}
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "audience": AUDIENCE,
        "grant_type": "client_credentials"
    }
    
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    
    access_token = response.json()["access_token"]
    print("✅ Access token obtido com sucesso!")
    return access_token


def get_headers():
    """Retornar headers com authorization"""
    return {
        "authorization": f"Bearer {access_token}",
        "content-type": "application/json"
    }


def criar_usuario(email, senha, nome):
    """Criar usuário no Auth0"""
    url = f"https://{AUTH0_DOMAIN}/api/v2/users"
    data = {
        "email": email,
        "password": senha,
        "connection": "Username-Password-Authentication",
        "email_verified": True,
        "name": nome
    }
    
    response = requests.post(url, headers=get_headers(), json=data)
    response.raise_for_status()
    
    user = response.json()
    print(f"✅ Usuário criado: {email} (ID: {user['user_id']})")
    return user


def criar_role(nome, descricao):
    """Criar role no Auth0"""
    url = f"https://{AUTH0_DOMAIN}/api/v2/roles"
    data = {
        "name": nome,
        "description": descricao
    }
    
    response = requests.post(url, headers=get_headers(), json=data)
    response.raise_for_status()
    
    role = response.json()
    print(f"✅ Role criada: {nome} (ID: {role['id']})")
    return role


def listar_roles():
    """Listar todas as roles"""
    url = f"https://{AUTH0_DOMAIN}/api/v2/roles"
    
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()
    
    roles = response.json()
    return roles


def adicionar_permissions_role(role_id, permissions):
    """Adicionar permissions a uma role"""
    url = f"https://{AUTH0_DOMAIN}/api/v2/roles/{role_id}/permissions"
    
    # Preparar permissions no formato correto
    permissions_data = [
        {
            "resource_server_identifier": "coffee-shop-api",
            "permission_name": perm
        }
        for perm in permissions
    ]
    
    response = requests.post(url, headers=get_headers(), json={"permissions": permissions_data})
    response.raise_for_status()
    
    print(f"✅ Permissions adicionadas ao role ID: {role_id}")


def atribuir_role_usuario(user_id, role_id):
    """Atribuir role a um usuário"""
    url = f"https://{AUTH0_DOMAIN}/api/v2/users/{user_id}/roles"
    
    response = requests.post(url, headers=get_headers(), json={"roles": [role_id]})
    response.raise_for_status()
    
    print(f"✅ Role atribuída ao usuário ID: {user_id}")


def main():
    """Função principal"""
    global role_barista_id, role_manager_id
    
    print("=" * 60)
    print("CRIAR USUÁRIOS, ROLES E PERMISSÕES NO AUTH0")
    print("=" * 60)
    print()
    
    # 1. Obter access token
    get_management_token()
    
    # 2. Criar usuários
    print("\n--- Criando Usuários ---")
    user_barista = criar_usuario(
        "barista@coffeeshop.com",
        "CoffeeShop2024!",
        "Coffee Barista"
    )
    
    user_manager = criar_usuario(
        "manager@coffeeshop.com",
        "CoffeeShop2024!",
        "Coffee Manager"
    )
    
    # 3. Criar roles
    print("\n--- Criando Roles ---")
    role_barista_obj = criar_role(
        "Barista",
        "Can view drink details"
    )
    role_barista_id = role_barista_obj["id"]
    
    role_manager_obj = criar_role(
        "Manager",
        "Can manage all drinks"
    )
    role_manager_id = role_manager_obj["id"]
    
    # 4. Adicionar permissions aos roles
    print("\n--- Adicionando Permissions aos Roles ---")
    adicionar_permissions_role(role_barista_id, [
        "get:drinks",
        "get:drinks-detail"
    ])
    
    adicionar_permissions_role(role_manager_id, [
        "get:drinks",
        "get:drinks-detail",
        "post:drinks",
        "patch:drinks",
        "delete:drinks"
    ])
    
    # 5. Atribuir roles aos usuários
    print("\n--- Atribuindo Roles aos Usuários ---")
    atribuir_role_usuario(user_barista["user_id"], role_barista_id)
    atribuir_role_usuario(user_manager["user_id"], role_manager_id)
    
    print("\n" + "=" * 60)
    print("✅ TUDO CONCLUÍDO COM SUCESSO!")
    print("=" * 60)
    print("\nCredenciais:")
    print(f"Barista: barista@coffeeshop.com / CoffeeShop2024!")
    print(f"Manager: manager@coffeeshop.com / CoffeeShop2024!")
    print("\nAgora você pode fazer login com estes usuários!")


if __name__ == "__main__":
    main()

