# Auth0 Setup - Passo a Passo Detalhado

## 📚 Este guia vai te levar da criação da conta até a obtenção dos tokens JWT

---

## 🎯 PASSO 1: Criar Conta no Auth0

### 1.1 Acessar o Auth0
1. Vá para: **https://auth0.com**
2. Clique em **"Sign Up"**
3. Escolha criar conta com Google ou email
4. Complete o cadastro

### 1.2 Escolher Tenant
- Após criar a conta, você será redirecionado para o dashboard
- O URL será algo como: `https://YOUR-TENANT.auth0.com`
- **ANOTE o nome do tenant** (exemplo: `minha-empresa-fsnd`)

---

## 🎯 PASSO 2: Criar a API no Auth0

### 2.1 Navegar até Applications
1. No menu lateral esquerdo, clique em **"Applications"**
2. Você verá a aba **"APIs"** no topo

### 2.2 Criar API
1. Clique na aba **"APIs"**
2. Clique no botão **"+ Create API"**

### 2.3 Preencher Informações da API
**Preencha exatamente assim:**

```
Name: Coffee Shop API

Identifier: coffee-shop-api

Signing Algorithm: RS256 (deixe padrão)
```

**NÃO clique em Create ainda!**

### 2.4 Configurações Importantes
Antes de clicar em Create, certifique-se que:
- Name: `Coffee Shop API`
- Identifier: `coffee-shop-api` (este será usado depois!)
- Algorithm: `RS256`

Agora clique em **"Create"**

### 2.5 VERIFICAÇÃO OBRIGATÓRIA
Após criar, você verá a página de Settings da API.

**VERIFIQUE:**
- [ ] A API foi criada com sucesso
- [ ] O Identifier é `coffee-shop-api`
- [ ] O nome é `Coffee Shop API`

**⚠️ IMPORTANTE:** O Identifier é o que você vai usar como `AUTH0_API_AUDIENCE` no seu código!

---

## 🎯 PASSO 3: Habilitar RBAC e Permissions

### 3.1 Na página Settings da API

**ENCONTRE as seções:**
- Settings (aba atual)
- Permissions (próxima etapa)
- Machine to Machine Apps

### 3.2 Habilitar RBAC
Na página Settings, role até achar a seção **"RBAC Settings"**

**Marque as seguintes opções:**
- ✅ **Enable RBAC**
- ✅ **Add Permissions in the Access Token**

**⚠️ CRÍTICO:** Ambas devem estar CHECKED (marcadas)

Clique em **"Save Changes"** se aparecer

### 3.3 Criar Permissions
1. Na página da API, clique na aba **"Permissions"**
2. Você verá que está vazio
3. Clique no botão **"+ Add Permission"**

**Crie CADA uma dessas permissions:**

| Permission Name | Description |
|----------------|-------------|
| `get:drinks` | Get all drinks |
| `get:drinks-detail` | Get drink details with recipe |
| `post:drinks` | Create new drinks |
| `patch:drinks` | Update existing drinks |
| `delete:drinks` | Delete drinks |

**Para cada permission:**
1. Clique em **"+ Add Permission"**
2. Digite o nome (exemplo: `get:drinks`)
3. Digite a description
4. Clique em **"Add"**

**⚠️ IMPORTANTE:** Crie TODAS as 5 permissions antes de continuar!

---

## 🎯 PASSO 4: Criar Roles (Barista e Manager)

### 4.1 Navegar até Roles
1. No menu lateral esquerdo, clique em **"User Management"**
2. Clique em **"Roles"**

### 4.2 Criar Role: Barista

1. Clique no botão **"+ Create Role"**
2. Preencha:
   ```
   Name: Barista
   Description: Can view drink details
   ```
3. Clique em **"Create"**

### 4.3 Adicionar Permissions ao Role Barista

Na página do role Barista:

1. Role até encontrar a seção **"Permissions"**
2. Clique em **"+ Add Permission"**
3. Selecione `Coffee Shop API`
4. Marque apenas estas duas:
   - ✅ `get:drinks`
   - ✅ `get:drinks-detail`
5. Clique em **"Add"**

### 4.4 Criar Role: Manager

1. Volte para a lista de roles (Role Management)
2. Clique em **"+ Create Role"**
3. Preencha:
   ```
   Name: Manager
   Description: Can perform all actions
   ```
4. Clique em **"Create"**

### 4.5 Adicionar Permissions ao Role Manager

Na página do role Manager:

1. Na seção **"Permissions"**
2. Clique em **"+ Add Permission"**
3. Selecione `Coffee Shop API`
4. Marque TODAS as 5 permissions:
   - ✅ `get:drinks`
   - ✅ `get:drinks-detail`
   - ✅ `post:drinks`
   - ✅ `patch:drinks`
   - ✅ `delete:drinks`
5. Clique em **"Add"**

### 4.6 VERIFICAÇÃO

Você deve ter agora:
- [ ] Role "Barista" criado com 2 permissions
- [ ] Role "Manager" criado com 5 permissions

---

## 🎯 PASSO 5: Criar Usuários de Teste

### 5.1 Navegar até Users

1. No menu lateral esquerdo: **User Management**
2. Clique em **Users**

### 5.2 Criar Usuário Barista

1. Clique no botão **"+ Create User"**
2. Preencha:
   ```
   Email: barista@coffee-shop.com
   Password: (digite uma senha, exemplo: CoffeeBarista123!)
   ```
3. **Importante:** Desmarque "Verify Email" se aparecer
4. Clique em **"Create"**

### 5.3 Atribuir Role ao User Barista

Na página do usuário criado:

1. Procure a seção **"Roles"**
2. Clique em **"Assign Roles"**
3. Selecione o role **"Barista"**
4. Clique em **"Assign"**

### 5.4 Criar Usuário Manager

1. Volte para a lista de Users
2. Clique em **"+ Create User"**
3. Preencha:
   ```
   Email: manager@coffee-shop.com
   Password: (digite uma senha, exemplo: CoffeeManager123!)
   ```
4. Desmarque "Verify Email" se aparecer
5. Clique em **"Create"**

### 5.5 Atribuir Role ao User Manager

Na página do usuário manager:

1. Na seção **"Roles"**
2. Clique em **"Assign Roles"**
3. Selecione o role **"Manager"**
4. Clique em **"Assign"**

### 5.6 VERIFICAÇÃO FINAL

Você deve ter agora:
- [ ] Usuário `barista@coffee-shop.com` com role Barista
- [ ] Usuário `manager@coffee-shop.com` com role Manager
- [ ] Ambos com senhas definidas

**⚠️ IMPORTANTE:** Anote as senhas que você criou!

---

## 🎯 PASSO 6: Obter JWT Tokens

### 6.1 Escolher Método

Você tem 2 opções:

#### **OPÇÃO A: Via Dashboard (Mais Fácil)**
#### **OPÇÃO B: Via Terminal (Usando cURL)**

---

### OPÇÃO A: Obter Token pelo Dashboard

#### A.1 Acessar Test Application

1. No menu lateral: **Applications**
2. Certifique-se que está na aba **"Applications" (não APIs)**
3. Você verá uma aplicação chamada **"Auth0 Management API"** ou outra

**Se não existir nenhuma aplicação:**

1. Clique em **"+ Create Application"**
2. Escolha **"Regular Web Applications"**
3. Nome: `Coffee Shop Test`
4. Click **Create**

#### A.2 Testar Login Manual

Agora você pode testar o login manualmente no Dashboard para ver os tokens, mas isso é complicado.

**Recomendo usar a OPÇÃO B (Terminal) que é mais direta.**

---

### OPÇÃO B: Obter Token via Terminal (RECOMENDADO)

#### B.1 Instruções Simples

Abra um terminal e execute:

```bash
# Substitua com SEU tenant (exemplo: minha-empresa-fsnd)
DOMAIN="seu-tenant.auth0.com"

# Este comando vai pedir as credenciais para você
curl -X POST https://${DOMAIN}/oauth/token \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "client_id":"YOUR_CLIENT_ID",
  "client_secret":"YOUR_CLIENT_SECRET",
  "audience":"coffee-shop-api",
  "grant_type":"client_credentials"
}
EOF
```

**Mas você precisa das credenciais primeiro!**

---

## 🎯 PASSO 7: Obter Credenciais da Application

### 7.1 Acessar Applications

1. **Applications** no menu lateral
2. Clique na aplicação que você quer usar

### 7.2 Ver Credenciais

Na página Settings, você encontrará:
- **Client ID** (copie este)
- **Client Secret** (clique para revelar, depois copie)

### 7.3 Usar para Obter Token

Agora execute (no terminal):

```bash
# Substitua TODOS os valores
curl -X POST https://SEU-TENANT.auth0.com/oauth/token \
  -H "Content-Type: application/json" \
  -d '{
    "client_id":"COLE_O_CLIENT_ID_AQUI",
    "client_secret":"COLE_O_CLIENT_SECRET_AQUI",
    "audience":"coffee-shop-api",
    "grant_type":"client_credentials"
  }'
```

### 7.4 Resposta

Você receberá algo como:

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIs...",
  "token_type": "Bearer"
}
```

**⚠️ IMPORTANTE:** Copie o `access_token`! Este é seu JWT!

---

## 🎯 PASSO 8: Atualizar Configuração do Backend

### 8.1 Atualizar .env

No arquivo `backend/.env`, atualize:

```bash
AUTH0_DOMAIN=seu-tenant.auth0.com  # ← Seu tenant
AUTH0_ALGORITHM=RS256
AUTH0_API_AUDIENCE=coffee-shop-api  # ← O Identifier da API
```

### 8.2 Salvar o Token

Para usar nos testes do Postman, salve o token em um arquivo:

```bash
echo "seu-token-jwt-aqui" > ~/auth0_token.txt
```

---

## 🎯 PASSO 9: Testar se Funciona

### 9.1 Iniciar Backend

```bash
cd backend
./start_server.sh
```

### 9.2 Testar Endpoint Público

Em outro terminal:

```bash
curl http://localhost:5000/drinks
```

**Deve retornar:**
```json
{"drinks": [], "success": true}
```

### 9.3 Testar Endpoint Protegido

```bash
curl -H "Authorization: Bearer SEU_TOKEN_JWT" \
  http://localhost:5000/drinks-detail
```

**Deve retornar:**
```json
{"drinks": [], "success": true}
```

Se funcionar, está tudo OK! 🎉

---

## 📋 Checklist Completo

Marque conforme for completando:

### Conta Auth0
- [ ] Conta criada
- [ ] Tenant anotado

### API
- [ ] API "Coffee Shop API" criada
- [ ] Identifier: `coffee-shop-api`
- [ ] RBAC habilitado
- [ ] "Add Permissions in Token" habilitado
- [ ] 5 permissions criadas

### Roles
- [ ] Role "Barista" criado
- [ ] Barista com 2 permissions
- [ ] Role "Manager" criado
- [ ] Manager com 5 permissions

### Users
- [ ] Usuário barista criado
- [ ] Barista com role Barista
- [ ] Usuário manager criado
- [ ] Manager com role Manager

### Tokens
- [ ] Token JWT obtido
- [ ] Token testado e funcionando

### Backend
- [ ] Backend iniciado
- [ ] Endpoint público funcionando
- [ ] Endpoint protegido funcionando

---

## 🆘 Troubleshooting

### Erro: "Invalid audience"
- Verifique que `AUTH0_API_AUDIENCE=coffee-shop-api` está correto
- Deve ser o mesmo Identifier da API

### Erro: "Invalid permissions"
- Verifique que RBAC está habilitado
- Verifique que "Add Permissions in Token" está habilitado
- Verifique que o user tem o role correto

### Erro: "Token expired"
- Obtenha um novo token
- Tokens expiram em algum tempo

### Não consigo ver as permissions
- Verifique que criou na API correta
- Verifique que habilitou RBAC

---

## 📞 Precisa de Ajuda?

Se ainda tiver dúvidas em algum passo específico, me diga:
- Em qual passo você está?
- Qual erro você está vendo?
- O que aparece na tela?

Eu posso criar screenshots detalhados ou ajustar este guia!

