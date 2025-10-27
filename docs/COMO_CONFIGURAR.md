# ⚙️ Como Configurar o Projeto

## 📍 Onde Configurar Cada Item (Resposta Direta)

⚠️ **Não encontrou os arquivos?**
- `backend/.env` → **CRIAR** (copiar de env.template)
- `backend/udacity-fsnd-udaspicelatte.postman_collection.json` → **EXISTE** (atualizar no Postman)
- `frontend/src/environments/environment.ts` → **EXISTE** (editar)

---

### 1. Backend Environment Variables

**Pergunta:** "Aonde configurar backend/.env?"

**Resposta:**
```bash
cd backend
cp env.template .env
nano .env  # ou code .env
```

**Arquivo:** `backend/.env`

**Adicionar:**
```
AUTH0_DOMAIN=seu-tenant.auth0.com
AUTH0_ALGORITHM=RS256
AUTH0_API_AUDIENCE=coffee-shop-api
```

**Como obter valores:**
- AUTH0_DOMAIN: Dashboard Auth0 → Applications → Domain (antes de .auth0.com)
- AUTH0_API_AUDIENCE: Dashboard Auth0 → APIs → Identifier

---

### 2. Postman Collection

**Pergunta:** "Aonde configurar collection com JWT?"

**Resposta:**
1. Importar: `backend/udacity-fsnd-udaspicelatte.postman_collection.json`
2. Abrir Postman
3. Right-click "Barista" folder → Authorization → Bearer Token → [JWT]
4. Right-click "Manager" folder → Authorization → Bearer Token → [JWT]
5. Testar endpoints
6. Export collection

**Onde obter JWT:**
- Dashboard Auth0 → APIs → Test tab
- Ou fazer login real e copiar token

---

### 3. Frontend Environment

**Pergunta:** "Aonde configurar frontend environment.ts?"

**Resposta:**
```bash
cd frontend
code src/environments/environment.ts
```

**Arquivo:** `frontend/src/environments/environment.ts`

**Configurar:**
```typescript
auth0: {
  url: 'seu-tenant',           // ⚠️ CONFIGURAR - Domain prefix
  audience: 'coffee-shop-api',  // ⚠️ CONFIGURAR - API identifier
  clientId: 'seu-client-id',    // ⚠️ CONFIGURAR - SPA Client ID
  callbackURL: 'http://localhost:8100',  // ✅ Já está configurado
}
```

**Como obter valores:**
- url: Auth0 Dashboard → Applications → Domain prefix
- audience: Auth0 Dashboard → APIs → Identifier
- clientId: Auth0 Dashboard → Applications → SPA → Client ID

---

## 📝 Checklist Rápido

```bash
# 1. Backend
cd backend
cp env.template .env
nano .env  # Adicionar Auth0 credentials

# 2. Frontend
cd frontend
nano src/environments/environment.ts  # Adicionar Auth0 credentials

# 3. Postman
# - Import collection
# - Obter JWTs
# - Configurar tokens
# - Export collection

# 4. Testar
cd backend && pytest
cd frontend && ionic serve
```

---

## 📚 Documentação Detalhada

Leia em `docs/`:
- **CONFIGURACAO_PROJETO.md** - Guia completo de configuração
- **MANUAL_TESTE_COMPLETO.md** - Como testar tudo

---

**✅ É só isso! Configure esses 3 itens e o projeto funciona!**

