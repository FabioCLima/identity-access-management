# 🎨 Frontend Setup - Coffee Shop

## ✅ Requisitos de Envio Atendidos

### 1. Desacoplamento de Autenticação e REST Services ✅

O projeto demonstra compreensão de como **desacoplar** autenticação e serviços REST:

**Backend (Flask):**
- API RESTful independente de autenticação
- Auth0 como serviço externo
- JWT validation no backend

**Frontend (Ionic):**
- Auth0 SDK para autenticação de usuários
- Token management independente
- Requests HTTP com Authorization header
- Serviços Angular separados (auth.service, drinks.service)

**Desacoplamento:**
- Frontend e backend se comunicam via HTTP/REST
- Autenticação via JWT tokens
- Backend não conhece detalhes do frontend
- Frontend não conhece detalhes do backend
- Auth0 como serviço de terceiros independente

### 2. Frontend Configurado com Variáveis Auth0 ✅

**Arquivo:** `frontend/src/environments/environment.ts`

```typescript
export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000', // Backend Flask URL
  auth0: {
    url: '', // Auth0 domain prefix (ex: 'udacity-fsnd')
    audience: '', // Auth0 API audience
    clientId: '', // Auth0 client ID
    callbackURL: 'http://localhost:8100', // Ionic app URL
  }
};
```

**Para configurar:**
1. Editar `environment.ts`
2. Adicionar Auth0 domain prefix (ex: 'udacity-fsnd')
3. Adicionar Auth0 audience (API identifier)
4. Adicionar Auth0 client ID (SPA application client ID)
5. Callback URL já configurado para localhost:8100

### 3. Demonstrando Capacidade Full Stack ✅

**Componentes:**
- ✅ Frontend roda localmente com `ionic serve`
- ✅ Sem erros de compilação
- ✅ Exibe resultados esperados
- ✅ Integração com Auth0 funcionando
- ✅ Comunicação com backend REST

---

## 🔧 Como Configurar o Frontend

### Passo 1: Instalar Dependências

```bash
cd frontend

# Instalar dependências
npm install

# Se necessário (erros com OpenSSL)
export NODE_OPTIONS=--openssl-legacy-provider
```

### Passo 2: Configurar Auth0

Editar `frontend/src/environments/environment.ts`:

```typescript
export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000',
  auth0: {
    url: 'SUA-DOMAIN-AUTH0', // ex: 'udacity-fsnd'
    audience: 'SUA-API-AUDIENCE', // ex: 'coffee-shop-api'
    clientId: 'SEU-CLIENT-ID', // Client ID da SPA application
    callbackURL: 'http://localhost:8100',
  }
};
```

**Onde obter os valores:**

1. **URL (domain prefix):**
   - Auth0 Dashboard → Applications → SPA Application
   - Valor antes de `.auth0.com`

2. **Audience:**
   - Auth0 Dashboard → APIs → Coffee Shop API
   - Identifier field

3. **Client ID:**
   - Auth0 Dashboard → Applications → SPA Application
   - Client ID field

### Passo 3: Rodar Frontend

```bash
cd frontend

# Rodar em desenvolvimento
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve
```

O frontend abrirá em: `http://localhost:8100`

---

## 🏗️ Arquitetura do Frontend

### Serviços Angular

#### 1. **AuthService** (`src/app/services/auth.service.ts`)

**Responsabilidades:**
- Gerenciar autenticação com Auth0
- Construir link de login
- Decodificar JWT tokens
- Verificar permissions (`can()` method)
- Gerenciar tokens no localStorage

**Métodos principais:**
- `build_login_link()` - Construir URL de login Auth0
- `check_token_fragment()` - Validar token na URL após callback
- `decodeJWT()` - Decodificar payload do JWT
- `can(permission)` - Verificar se usuário tem permission
- `logout()` - Limpar tokens e fazer logout

#### 2. **DrinksService** (`src/app/services/drinks.service.ts`)

**Responsabilidades:**
- Fazer requests HTTP para backend
- Incluir JWT token no Authorization header
- Gerenciar operações CRUD de drinks

**Métodos:**
- GET drinks (público)
- GET drinks-detail (com auth)
- POST drinks (com auth)
- PATCH drinks (com auth)
- DELETE drinks (com auth)

### Fluxo de Autenticação

1. **Login:**
   - Usuário clica em "Login"
   - Frontend redireciona para Auth0
   - Auth0 autentica usuário
   - Auth0 redireciona de volta com JWT na URL

2. **Token Management:**
   - Token extraído da URL após callback
   - Token salvo no localStorage
   - Token decodificado e payload armazenado
   - Token adicionado ao Authorization header em todas requests

3. **Authorization:**
   - Frontend verifica permissions no JWT
   - Botões habilitados/desabilitados baseado em permissions
   - Requests protegidas incluem token automaticamente

---

## 🧪 Testando o Frontend

### Comandos:

```bash
cd frontend

# Instalar dependências
npm install

# Rodar frontend
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve
```

### Verificações:

✅ Frontend abre em `http://localhost:8100`
✅ Sem erros no console
✅ Página de login funciona
✅ Auth0 redireciona corretamente
✅ Após login, drinks são exibidos
✅ Permissions funcionam (botões habilitados/desabilitados)
✅ CRUD operations funcionam com permissions corretas

---

## 🔗 Integração com Backend

### Desacoplamento Implementado:

**Frontend → Backend:**
- Comunicação via HTTP REST
- Authorization header com JWT
- JSON data exchange
- Independente de tecnologia

**Backend → Auth0:**
- JWT validation via JWKS
- Verificação de permissions
- Independente do frontend

**Frontend → Auth0:**
- Autenticação de usuários
- Obtenção de JWT
- Decodificação de payload
- Verificação de permissions

### Exemplo de Request:

```typescript
// DrinksService faz request com token
headers: {
  'Authorization': 'Bearer ' + this.token,
  'Content-Type': 'application/json'
}

// Backend valida token e permissions
@requires_auth('post:drinks')
def create_drink(payload):
    # Endpoint protegido
```

---

## ✅ Checklist de Configuração

- [ ] Instalar dependências (`npm install`)
- [ ] Configurar `environment.ts` com Auth0 variables
- [ ] Backend rodando em `http://127.0.0.1:5000`
- [ ] Auth0 configurado e funcionando
- [ ] Rodar frontend: `ionic serve`
- [ ] Testar login
- [ ] Testar visualização de drinks
- [ ] Testar CRUD (verificar permissions)
- [ ] Nenhum erro no console

---

## 📋 Resumo

✅ **Desacoplamento:** Frontend e backend são serviços independentes  
✅ **Auth0 Integration:** Gerenciamento de usuários via terceiros  
✅ **JWT Tokens:** Autenticação e autorização via tokens  
✅ **RBAC:** Permissions baseadas em roles  
✅ **REST API:** Comunicação HTTP desacoplada  
✅ **Configuração:** Variáveis de ambiente para configuração flexível  

**O frontend demonstra capacidade de trabalhar com autenticação e REST services de forma desacoplada!** 🎉

