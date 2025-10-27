# 🚀 Instruções de Instalação e Teste - Coffee Shop

## ✅ Código Completo e Testes Criados

### 📦 O que foi feito:

1. **Code Review Completo** ✅
2. **Testes Automatizados Criados** ✅
   - `backend/tests/test_api.py` - Testes de API
   - `backend/tests/test_auth.py` - Testes de autenticação
   - `backend/tests/conftest.py` - Fixtures pytest
3. **Documentação Organizada** ✅
4. **Manual de Teste Criado** ✅

---

## 🏃 Quick Start

### 1. Instalar Dependências

```bash
cd backend

# Instalar dependências do projeto
pip install -r requirements.txt

# Instalar dependências de desenvolvimento (testes)
pip install pytest pytest-cov coverage
```

### 2. Rodar Testes

```bash
cd backend

# Rodar todos os testes
pytest

# Com coverage report
pytest --cov=src --cov-report=html

# Ver coverage report
open htmlcov/index.html  # Mac
xdg-open htmlcov/index.html  # Linux
```

### 3. Configurar e Rodar Backend

```bash
cd backend

# Criar .env
cp env.template .env

# Editar .env com suas credenciais Auth0
nano .env

# Rodar servidor
export FLASK_APP=src/api.py
flask run --reload
```

### 4. Configurar e Rodar Frontend

```bash
cd frontend

# Instalar dependências
npm install

# Editar environment.ts
code src/environments/environment.ts
# Adicionar Auth0 credentials

# Rodar servidor
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve
```

---

## 📍 Onde Configurar

### Backend Environment Variables

**Arquivo:** `backend/.env` (CRIAR)

```bash
cd backend
cp env.template .env
nano .env
```

Adicionar:
```
AUTH0_DOMAIN=seu-tenant.auth0.com
AUTH0_ALGORITHM=RS256
AUTH0_API_AUDIENCE=coffee-shop-api
```

### Postman Collection

**Arquivo:** `backend/udacity-fsnd-udaspicelatte.postman_collection.json`

1. Abrir Postman
2. Import → selecionar arquivo acima
3. Obter JWTs (Barista e Manager)
4. Right-click "Barista" → Authorization → Bearer Token
5. Right-click "Manager" → Authorization → Bearer Token
6. Testar todos endpoints
7. Export → save collection

### Frontend Environment

**Arquivo:** `frontend/src/environments/environment.ts`

```typescript
export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000',
  auth0: {
    url: 'seu-tenant',           // ⚠️ CONFIGURAR
    audience: 'coffee-shop-api',  // ⚠️ CONFIGURAR
    clientId: 'seu-client-id',    // ⚠️ CONFIGURAR
    callbackURL: 'http://localhost:8100',
  }
};
```

---

## 📚 Documentação Completa

### Todos os guias em `docs/`:

- **CONFIGURACAO_PROJETO.md** - ⭐ Onde configurar cada item
- **MANUAL_TESTE_COMPLETO.md** - Manual completo de testes
- **FRONTEND_SETUP.md** - Setup do frontend
- **RBAC_IMPLEMENTATION.md** - RBAC guide
- **RESUMO_FINAL.txt** - Resumo executivo

---

## ✅ Checklist de Configuração

```bash
# Backend
[ ] pip install -r requirements.txt
[ ] pip install pytest pytest-cov
[ ] cp env.template .env
[ ] Editar .env com Auth0 credentials
[ ] pytest (testes devem passar)
[ ] flask run --reload (servidor deve iniciar)

# Frontend
[ ] npm install
[ ] Editar src/environments/environment.ts
[ ] ionic serve (sem erros)

# Postman
[ ] Import collection
[ ] Obter JWTs
[ ] Configurar tokens
[ ] Testar endpoints
[ ] Export collection
```

---

## 🧪 Comandos de Teste

```bash
# Rodar testes
cd backend && pytest

# Coverage report
cd backend && pytest --cov=src --cov-report=html

# Lint code
cd backend && ruff check src/

# Format code
cd backend && ruff format src/

# Test backend endpoint
curl http://localhost:5000/drinks
```

---

## 📁 Estrutura Final

```
coffee-shop/
├── README.md                    # Principal
├── LICENSE.md                   # Licença
├── INSTALACAO_TESTE.md          # Este arquivo ⭐
│
├── backend/
│   ├── src/                     # ✅ Código completo
│   ├── tests/                   # ✅ Testes criados
│   │   ├── test_api.py
│   │   ├── test_auth.py
│   │   └── conftest.py
│   ├── .env                     # ⚠️  Criar e configurar
│   ├── pyproject.toml           # ✅ Configurado
│   └── pytest.ini               # ✅ Configurado
│
├── frontend/
│   ├── src/environments/
│   │   └── environment.ts       # ⚠️  Configurar
│
└── docs/                        # 📚 Toda documentação
    ├── CONFIGURACAO_PROJETO.md  # ⭐ Onde configurar
    ├── MANUAL_TESTE_COMPLETO.md # 🧪 Como testar
    ├── FRONTEND_SETUP.md
    ├── RBAC_IMPLEMENTATION.md
    └── ...
```

---

## 🎯 Próximos Passos

1. **Ler:** `docs/CONFIGURACAO_PROJETO.md` - Onde configurar
2. **Seguir:** Setup Auth0
3. **Configurar:** Backend (.env)
4. **Configurar:** Frontend (environment.ts)
5. **Configurar:** Postman (JWT tokens)
6. **Testar:** Tudo funcionando
7. **Submeter:** Projeto completo

---

**✅ Tudo pronto! Basta configurar os 3 arquivos e testar!**

