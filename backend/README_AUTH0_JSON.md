# Auth0 Setup Automatizado com JSON

## 📋 Visão Geral

Este guia mostra como configurar usuários e roles do Auth0 automaticamente usando um arquivo JSON, em vez de criar manualmente no dashboard.

## ✨ Benefícios

- ✅ Configuração versionada no Git
- ✅ Criação rápida e repetível
- ✅ Facilita múltiplos ambientes (dev, staging, prod)
- ✅ Configuração como código
- ✅ Evita erros de digitação

## 🚀 Como Usar

### Passo 1: Configure o JSON

Edite o arquivo `backend/auth0_users_template.json`:

```json
{
  "roles": [
    {
      "name": "Barista",
      "description": "Can view drink details",
      "permissions": [
        "get:drinks",
        "get:drinks-detail"
      ]
    },
    {
      "name": "Manager",
      "description": "Can perform all actions",
      "permissions": [
        "get:drinks",
        "get:drinks-detail",
        "post:drinks",
        "patch:drinks",
        "delete:drinks"
      ]
    }
  ],
  "users": [
    {
      "email": "barista@test.com",
      "password": "MinhaSenhaSegura123!",
      "connection": "Username-Password-Authentication",
      "roles": ["Barista"],
      "verify_email": false
    },
    {
      "email": "manager@test.com",
      "password": "MinhaSenhaSegura123!",
      "connection": "Username-Password-Authentication",
      "roles": ["Manager"],
      "verify_email": false
    }
  ]
}
```

### Passo 2: Obtenha Credenciais da Management API

1. Acesse https://manage.auth0.com
2. Vá em **Applications** → **Create Application**
3. Escolha **Machine to Machine Applications**
4. Autorize para **Auth0 Management API**
5. Copie o **Client ID** e **Client Secret**

### Passo 3: Execute o Script

```bash
cd backend
source .venv/bin/activate

# Instalar dependência se necessário
pip install auth0-python

# Executar o script
python setup_auth0.py \
  --domain seu-tenant.auth0.com \
  --client-id SEU_CLIENT_ID \
  --client-secret SEU_CLIENT_SECRET \
  --config auth0_users_template.json
```

### Passo 4: Verifique a Saída

O script mostrará:

```
Getting Management API access token...

=== Creating Roles ===
✓ Created role: Barista
  Adding permission: get:drinks
  Adding permission: get:drinks-detail
✓ Updated permissions for role
✓ Created role: Manager
...

=== Creating Users ===
✓ Created user: barista@test.com
  ✓ Assigned role Barista to user
✓ Created user: manager@test.com
  ✓ Assigned role Manager to user

✓ Setup complete!

Users created:
  - barista@test.com (Password: MinhaSenhaSegura123!)
  - manager@test.com (Password: MinhaSenhaSegura123!)
```

## 📝 Estrutura do JSON

### Roles

```json
{
  "name": "Nome do Role",
  "description": "Descrição",
  "permissions": ["permission1", "permission2"]
}
```

### Users

```json
{
  "email": "usuario@email.com",
  "password": "SenhaForte123!",
  "connection": "Username-Password-Authentication",
  "roles": ["Barista"],
  "verify_email": false
}
```

## 🔧 Personalização

### Adicionar Mais Roles

Adicione ao array `roles` no JSON:

```json
{
  "name": "Administrator",
  "description": "Full system access",
  "permissions": [
    "get:drinks",
    "get:drinks-detail",
    "post:drinks",
    "patch:drinks",
    "delete:drinks",
    "manage:users"
  ]
}
```

### Adicionar Mais Users

Adicione ao array `users`:

```json
{
  "email": "admin@test.com",
  "password": "AdminPass123!",
  "connection": "Username-Password-Authentication",
  "roles": ["Administrator"],
  "verify_email": false
}
```

## 🎯 Casos de Uso

### Ambiente de Desenvolvimento

```json
{
  "users": [
    {
      "email": "dev-barista@local.dev",
      "password": "dev123",
      "roles": ["Barista"]
    }
  ]
}
```

### Ambiente de Produção

```json
{
  "users": [
    {
      "email": "prod-barista@coffee-shop.com",
      "password": "SenhaForteProdução123!",
      "roles": ["Barista"]
    }
  ]
}
```

## 🔒 Segurança

⚠️ **Importante:**
- Não commite arquivos JSON com senhas reais
- Use `.gitignore` para arquivos sensíveis
- Varie senhas por ambiente
- Considere usar variáveis de ambiente para senhas

## ❓ Troubleshooting

### "Role already exists"
- Normal em re-execuções
- O script detecta e pula roles existentes

### "User already exists"  
- Normal em re-execuções
- O script detecta e atualiza users existentes

### "Permission denied"
- Verifique credenciais da Management API
- Confirme permissões da API

## 📚 Recursos

- [Auth0 Management API](https://auth0.com/docs/api/management/v2)
- [auth0-python SDK](https://github.com/auth0/auth0-python)
- [Auth0 Dashboard](https://manage.auth0.com)

## 🎉 Próximos Passos

Após criar usuários e roles:

1. Obtenha JWT tokens (veja `docs/backend/AUTH0_SETUP.md`)
2. Configure Postman collection
3. Teste os endpoints
4. Deploy da aplicação

