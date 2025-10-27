# ⚙️ Guia de Configuração - Coffee Shop

## 📍 Onde Configurar os Itens Pendentes

### 1. Backend Environment Variables

**Arquivo:** `backend/.env` (CRIAR)

**Como configurar:**

```bash
cd backend

# Copiar template
cp env.template .env

# Editar .env
nano .env
# ou
code .env  # VS Code
# ou
vim .env
```

**Conteúdo do .env:**
```bash
# Auth0 Configuration
AUTH0_DOMAIN=seu-tenant.auth0.com        # ⚠️ CONFIGURAR
AUTH0_ALGORITHM=RS256
AUTH0_API_AUDIENCE=coffee-shop-api       # ⚠️ CONFIGURAR

# Flask Configuration (Opcional)
FLASK_ENV=development
FLASK_DEBUG=True
```

**Onde obter os valores:**

1. **AUTH0_DOMAIN:**
   - Login em https://manage.auth0.com
   - Dashboard → Applications → SPA Application
   - Domain = `seu-tenant` (antes de .auth0.com)
   - Exemplo: Se domain é `dev-123.auth0.com`, use `dev-123`

2. **AUTH0_API_AUDIENCE:**
   - Dashboard → APIs → Coffee Shop API
   - Identifier field
   - Exemplo: `coffee-shop-api`

3. **AUTH0_ALGORITHM:**
   - Geralmente `RS256` (já está no template)

---

### 2. Postman Collection

**Arquivo:** `backend/udacity-fsnd-udaspicelatte.postman_collection.json`

**Como configurar:**

#### Passo 1: Importar no Postman

1. Abrir Postman
2. File → Import
3. Selecionar `backend/udacity-fsnd-udaspicelatte.postman_collection.json`

#### Passo 2: Obter JWT Tokens

**Opção A - Via Auth0 Dashboard:**
1. Login em https://manage.auth0.com
2. Applications → APIs → Coffee Shop API → Test
3. Copiar Access Token
4. ⚠️ Token expira em 8 horas!

**Opção B - Via Auth0 Authentication (Login real):**
1. Criar 2 usuários no Auth0:
   - Usuário Barista (role: Barista)
   - Usuário Manager (role: Manager)
2. Fazer login como cada um
3. Copiar JWT do response

#### Passo 3: Configurar Tokens no Postman

**Para Barista folder:**
1. Right-click na pasta "Barista"
2. Click em "Authorization" tab
3. Type: Bearer Token
4. Token: [cole o JWT do usuário Barista]
5. ✅ Save

**Para Manager folder:**
1. Right-click na pasta "Manager"
2. Click em "Authorization" tab
3. Type: Bearer Token
4. Token: [cole o JWT do usuário Manager]
5. ✅ Save

#### Passo 4: Testar

Execute cada request e verifique status codes:
- GET /drinks → 200
- GET /drinks-detail → 200 (para ambos)
- POST /drinks → 403 (Barista), 200 (Manager)

#### Passo 5: Exportar

1. File → Export
2. Selecionar a collection
3. Export To File
4. Salvar em: `backend/udacity-fsnd-udaspicelatte.postman_collection.json`

⚠️ **IMPORTANTE:** Tokens expiram em 8 horas! Renovar antes de submeter!

---

### 3. Frontend Environment Variables

**Arquivo:** `frontend/src/environments/environment.ts`

**Como configurar:**

```bash
cd frontend

# Editar arquivo
code src/environments/environment.ts
# ou
nano src/environments/environment.ts
```

**Arquivo atual (necessita configuração):**
```typescript
export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000',
  auth0: {
    url: '', // ⚠️ CONFIGURAR
    audience: '', // ⚠️ CONFIGURAR
    clientId: '', // ⚠️ CONFIGURAR
    callbackURL: 'http://localhost:8100',
  }
};
```

**Arquivo configurado (exemplo):**
```typescript
export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000',
  auth0: {
    url: 'seu-tenant',           // Auth0 domain prefix
    audience: 'coffee-shop-api',  // API identifier
    clientId: 'abc123...',        // SPA Client ID
    callbackURL: 'http://localhost:8100',
  }
};
```

**Onde obter os valores:**

1. **url (Auth0 domain):**
   - Dashboard → Applications → SPA Application
   - Domain prefix (antes de .auth0.com)
   - Exemplo: Se é `dev-123.auth0.com`, use `dev-123`

2. **audience:**
   - Dashboard → APIs → Coffee Shop API
   - Identifier field
   - Exemplo: `coffee-shop-api`

3. **clientId:**
   - Dashboard → Applications → SPA Application
   - Client ID field
   - Exemplo: `k9kQ...ABC123...`

4. **callbackURL:**
   - Já está configurado: `http://localhost:8100`
   - Não precisa mudar

---

## 📝 Checklist de Configuração

### Backend ⚠️

- [ ] Criar `.env` em `backend/`
- [ ] Configurar `AUTH0_DOMAIN`
- [ ] Configurar `AUTH0_API_AUDIENCE`
- [ ] Testar backend: `flask run --reload`

### Postman ⚠️

- [ ] Importar collection
- [ ] Obter JWT de Barista
- [ ] Obter JWT de Manager
- [ ] Configurar tokens na collection
- [ ] Testar todos endpoints
- [ ] Exportar collection atualizada

### Frontend ⚠️

- [ ] Editar `environment.ts`
- [ ] Configurar `url` (Auth0 domain)
- [ ] Configurar `audience` (API identifier)
- [ ] Configurar `clientId` (SPA Client ID)
- [ ] Testar: `ionic serve`

---

## 🔄 Fluxo Completo de Configuração

### 1. Criar Conta Auth0

```
https://auth0.com → Sign Up → Free tier
```

### 2. Criar API no Auth0

```
Dashboard → APIs → Create API
Name: Coffee Shop API
Identifier: coffee-shop-api
Enable RBAC: ✅ ON
Enable Add Permissions in Access Token: ✅ ON
```

### 3. Criar Permissions

```
APIs → Coffee Shop API → Permissions
Criar:
- get:drinks
- get:drinks-detail
- post:drinks
- patch:drinks
- delete:drinks
```

### 4. Criar Roles

**Barista:**
```
Users & Roles → Roles → Create Role
Name: Barista
Description: Can view drinks
Permissions: get:drinks, get:drinks-detail
```

**Manager:**
```
Users & Roles → Roles → Create Role
Name: Manager
Description: Can manage drinks
Permissions: Todas (get, post, patch, delete)
```

### 5. Criar Usuários

```
User Management → Users → Create User
Criar 2 usuários:
1. Email: barista@test.com, Role: Barista
2. Email: manager@test.com, Role: Manager
```

### 6. Criar SPA Application

```
Applications → Applications → Create Application
Name: Coffee Shop SPA
Type: Single Page Web Application
Login: http://localhost:8100
Callback URLs: http://localhost:8100/callback
```

### 7. Configurar Backend

```bash
cd backend
cp env.template .env
# Editar .env com os valores
```

### 8. Configurar Frontend

```bash
cd frontend
# Editar src/environments/environment.ts
```

### 9. Obter JWT e Configurar Postman

Veja seção "Postman Collection" acima

---

## ✅ Verificação Final

### Backend funcionando?
```bash
curl http://localhost:5000/drinks
# Deve retornar JSON com drinks
```

### Frontend funcionando?
```bash
# Abrir http://localhost:8100
# Deve abrir a página de login
```

### Auth0 funcionando?
- Login em Auth0 funciona?
- Token obtido com sucesso?
- Callback funciona?

### Postman funcionando?
- Collection importada?
- Todos requests funcionam?
- Status codes corretos?

---

## 🆘 Problemas Comuns

### Backend não conecta ao Auth0

**Verificar:**
- `.env` configurado corretamente?
- `AUTH0_DOMAIN` correto?
- `AUTH0_API_AUDIENCE` correto?
- Restart do servidor Flask

### Frontend não faz login

**Verificar:**
- `environment.ts` configurado?
- `url`, `audience`, `clientId` corretos?
- Auth0 SPA Application criado?
- Callback URL correto?

### Postman 401 Unauthorized

**Verificar:**
- Token válido? (não expirado)
- Token correto para o role?
- Authorization header está "Bearer [token]"?
- Token tem as permissions necessárias?

---

**✅ Com essas configurações, seu projeto estará 100% funcional!**

