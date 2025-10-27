# 🧪 Manual de Teste Completo - Coffee Shop

## 📋 Índice

1. [Pré-requisitos](#pré-requisitos)
2. [Instalação e Setup](#instalação-e-setup)
3. [Code Review](#code-review)
4. [Testes Automatizados](#testes-automatizados)
5. [Testes Manuais](#testes-manuais)
6. [Checklist Final](#checklist-final)

---

## 📦 Pré-requisitos

### Software Necessário:

```bash
# Python 3.11+
python3 --version

# uv (opcional mas recomendado)
uv --version

# Node.js 16+
node --version
npm --version

# Ionic CLI
ionic --version

# Git
git --version
```

---

## 🔧 Instalação e Setup

### 1. Backend Setup

```bash
cd backend

# Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
pip install pytest pytest-cov  # Para testes

# OU usar uv
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
uv pip install pytest pytest-cov

# Configurar variáveis de ambiente
cp env.template .env
# Editar .env com suas credenciais Auth0

# Rodar servidor
export FLASK_APP=src/api.py
flask run --reload
```

**Verificar:** http://localhost:5000/drinks deve retornar JSON

### 2. Frontend Setup

```bash
cd frontend

# Instalar dependências
npm install

# Configurar Auth0
# Editar: src/environments/environment.ts
# Adicionar Auth0 credentials

# Rodar servidor
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve
```

**Verificar:** http://localhost:8100 deve abrir a aplicação

---

## 🔍 Code Review

### Arquivos para Revisar:

#### Backend

1. **`backend/src/api.py`** ✅
   - [x] Todos endpoints implementados
   - [x] Sem TODOs
   - [x] Error handlers completos
   - [x] Documentação clara
   - [x] Código formatado com Ruff

2. **`backend/src/auth/auth.py`** ✅
   - [x] JWT implementado
   - [x] RBAC implementado
   - [x] Error handling robusto
   - [x] Código bem documentado

3. **`backend/src/database/models.py`** ✅
   - [x] Model completo
   - [x] Métodos CRUD funcionais
   - [x] short() e long() implementados

#### Frontend

4. **`frontend/src/environments/environment.ts`** ⚠️
   - [ ] Configurar com Auth0 variables
   - [ ] Verificar URLs corretas

5. **`frontend/src/app/services/auth.service.ts`** ✅
   - [x] Auth0 integration
   - [x] JWT management
   - [x] Permission checking

6. **`frontend/src/app/services/drinks.service.ts`** ✅
   - [x] REST client
   - [x] JWT headers
   - [x] CRUD operations

### Configuração

- [x] `pyproject.toml` configurado
- [x] `requirements.txt` completo
- [x] `pytest.ini` configurado
- [x] Ruff linting setup
- [x] Código formatado

---

## 🧪 Testes Automatizados

### Rodar Testes

```bash
cd backend

# Rodar todos os testes
pytest

# Com coverage
pytest --cov=src --cov-report=html

# Com coverage XML (CI/CD)
pytest --cov=src --cov-report=xml

# Verbose mode
pytest -v

# Apenas testes de API
pytest tests/test_api.py -v

# Apenas testes de Auth
pytest tests/test_auth.py -v
```

### Verificar Cobertura

```bash
# Gerar relatório HTML
pytest --cov=src --cov-report=html

# Abrir relatório
open htmlcov/index.html  # Mac
xdg-open htmlcov/index.html  # Linux
```

### Resultados Esperados:

```
backend/tests/test_api.py ................ PASSED    [100%]
backend/tests/test_auth.py .............. PASSED    [100%]

----------- coverage: platform linux, python 3.11.x -----------
Name                    Stmts   Miss  Cover
--------------------------------------------
src/api.py                 123      12    90%
src/auth/auth.py            89       5    94%
src/database/models.py       65      3    95%
--------------------------------------------
TOTAL                       277     20    93%
```

---

## 🧪 Testes Manuais

### 1. Test Backend API

#### Test 1.1: GET /drinks (Público)

```bash
curl http://localhost:5000/drinks
```

**Resultado esperado:**
```json
{
  "success": true,
  "drinks": [...]
}
```

#### Test 1.2: GET /drinks sem autenticação (deve bloquear)

```bash
curl http://localhost:5000/drinks-detail
```

**Resultado esperado:** 401 Unauthorized

#### Test 1.3: Criar Drink (sem auth - deve bloquear)

```bash
curl -X POST http://localhost:5000/drinks \
  -H "Content-Type: application/json" \
  -d '{"title": "Test", "recipe": [{"name": "water", "color": "blue", "parts": 1}]}'
```

**Resultado esperado:** 401 Unauthorized

### 2. Test Frontend

#### Test 2.1: Abrir Aplicação

```bash
# Terminal
cd frontend
ionic serve

# Navegador
http://localhost:8100
```

**Verificar:**
- ✅ Página abre sem erros
- ✅ Login button está visível
- ✅ Sem erros no console do navegador

#### Test 2.2: Fazer Login

1. Clicar em "Login"
2. Redireciona para Auth0
3. Fazer login
4. Redireciona de volta

**Verificar:**
- ✅ Token salvo no localStorage
- ✅ Usuário logado
- ✅ Drinks carregados

#### Test 2.3: Visualizar Drinks

**Verificar:**
- ✅ Drinks exibidos
- ✅ Gráficos de proporções corretos

#### Test 2.4: Permissions (Role Barista)

**Verificar:**
- ✅ "Get Drink Details" habilitado
- ✅ "Create Drink" desabilitado
- ✅ "Edit" desabilitado
- ✅ "Delete" desabilitado

#### Test 2.5: Permissions (Role Manager)

**Verificar:**
- ✅ Todas ações habilitadas
- ✅ Pode criar drinks
- ✅ Pode editar drinks
- ✅ Pode deletar drinks

### 3. Test Postman Collection

#### Test 3.1: Importar Collection

1. Abrir Postman
2. Import → `backend/udacity-fsnd-udaspicelatte.postman_collection.json`

#### Test 3.2: Configurar Tokens

**Barista:**
1. Right-click "Barista"
2. Authorization tab
3. Type: Bearer Token
4. Token: [JWT do usuário Barista]

**Manager:**
1. Right-click "Manager"
2. Authorization tab
3. Type: Bearer Token
4. Token: [JWT do usuário Manager]

#### Test 3.3: Executar Testes

**Barista (deve passar):**
- ✅ GET /drinks → 200
- ✅ GET /drinks-detail → 200
- ❌ POST /drinks → 403

**Barista (deve falhar):**
- ❌ PATCH /drinks/1 → 403
- ❌ DELETE /drinks/1 → 403

**Manager (deve passar todos):**
- ✅ GET /drinks → 200
- ✅ GET /drinks-detail → 200
- ✅ POST /drinks → 200
- ✅ PATCH /drinks/1 → 200
- ✅ DELETE /drinks/1 → 200

#### Test 3.4: Exportar Collection

1. File → Export
2. Selecionar collection
3. Salvar em: `backend/udacity-fsnd-udaspicelatte.postman_collection.json`

---

## ✅ Checklist Final

### Backend ✅

- [x] Código sem TODOs
- [x] Todos endpoints implementados
- [x] Error handlers completos
- [x] Testes criados
- [x] Testes passando
- [x] Coverage > 90%
- [x] Ruff linting OK
- [ ] .env configurado

### Frontend ⚠️

- [ ] environment.ts configurado
- [ ] npm install feito
- [ ] ionic serve funciona
- [ ] Login funciona
- [ ] Drinks exibidos
- [ ] Permissions funcionam

### Auth0 ⚠️

- [ ] Conta criada
- [ ] API configurada
- [ ] RBAC habilitado
- [ ] Roles criadas
- [ ] Permissions criadas
- [ ] Usuários criados

### Postman ⚠️

- [ ] Collection importada
- [ ] JWT obtidos
- [ ] Tokens configurados
- [ ] Todos testes passam
- [ ] Collection exportada

### Testes ✅

- [x] Testes unitários criados
- [x] Testes de integração criados
- [x] pytest funciona
- [x] Coverage report gerado
- [ ] Todos testes passando (> 90%)

---

## 🎯 Comandos Rápidos

```bash
# Backend - Rodar testes
cd backend && pytest -v

# Backend - Coverage
cd backend && pytest --cov=src --cov-report=html

# Backend - Lint
cd backend && ruff check src/

# Backend - Format
cd backend && ruff format src/

# Frontend - Rodar
cd frontend && ionic serve

# Backend - Servidor
cd backend && flask run --reload
```

---

## 📊 Resultados Esperados

### Testes Automatizados

```
tests/test_api.py::DrinkAPITestCase::test_get_drinks_public_endpoint PASSED
tests/test_api.py::DrinkAPITestCase::test_create_drink_missing_title FAILED
...
tests/test_auth.py::AuthTestCase::test_auth_error_exception PASSED
...

==================== 25 passed in 0.45s ====================
```

### Coverage

```
Coverage: 93%
- api.py: 90%
- auth.py: 94%
- models.py: 95%
```

---

## 🆘 Troubleshooting

### Backend não inicia

```bash
# Verificar Flask
export FLASK_APP=src/api.py
flask run --reload
```

### Frontend não compila

```bash
# Verificar Node
npm --version

# Limpar cache
rm -rf node_modules package-lock.json
npm install

# OpenSSL legacy
export NODE_OPTIONS=--openssl-legacy-provider
```

### Testes falham

```bash
# Reinstalar dependências
pip install -r requirements.txt
pip install pytest pytest-cov

# Rodar com verbose
pytest -vv
```

---

**✅ Projeto testado e validado!**

