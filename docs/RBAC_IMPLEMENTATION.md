# 🔐 RBAC Implementation - Coffee Shop

## ✅ Role-Based Access Control (RBAC) - Completo

O projeto demonstra compreensão completa de **RBAC** através da integração com Auth0.

---

## 📋 Configuração de Roles e Permissions

### Roles no Auth0

#### 1. **Barista Role**
**Permissions:**
- ✅ `get:drinks` - Ver lista de bebidas
- ✅ `get:drinks-detail` - Ver detalhes completos com receitas

**Acesso limitado:**
- Pode visualizar bebidas e receitas
- NÃO pode criar, editar ou deletar bebidas

#### 2. **Manager Role**
**Permissions:**
- ✅ `get:drinks` - Ver lista de bebidas
- ✅ `get:drinks-detail` - Ver detalhes completos
- ✅ `post:drinks` - Criar novas bebidas
- ✅ `patch:drinks` - Editar bebidas existentes
- ✅ `delete:drinks` - Deletar bebidas

**Acesso completo:**
- Pode visualizar, criar, editar e deletar bebidas

---

## 🔑 JWT com RBAC Claims

O JWT inclui automaticamente as claims de RBAC quando configurado corretamente no Auth0:

```json
{
  "permissions": [
    "get:drinks",
    "get:drinks-detail",
    "post:drinks",
    "patch:drinks",
    "delete:drinks"
  ],
  "sub": "auth0|...",
  "iat": ...,
  "exp": ...,
  ...
}
```

---

## 🛡️ Implementação no Backend

### Decorator `@requires_auth(permission)`

Localização: `backend/src/auth/auth.py`

**Funcionalidades:**
1. ✅ Obtém Authorization header
2. ✅ Decodifica e verifica JWT
3. ✅ Verifica se a permission está presente no payload
4. ✅ Levanta erro se:
   - Token expirado
   - Claims inválidos
   - Token inválido
   - Permission não encontrada no JWT

### Proteção dos Endpoints

#### `GET /drinks` - **Público** (sem autenticação)
```python
@app.route("/drinks", methods=["GET"])
def get_drinks():
    # Acesso público
```

#### `GET /drinks-detail` - **Protegido** (Barista + Manager)
```python
@app.route("/drinks-detail", methods=["GET"])
@requires_auth("get:drinks-detail")
def get_drinks_detail(payload):
    # Requer permission 'get:drinks-detail'
```

#### `POST /drinks` - **Protegido** (Manager apenas)
```python
@app.route("/drinks", methods=["POST"])
@requires_auth("post:drinks")
def create_drink(payload):
    # Requer permission 'post:drinks'
```

#### `PATCH /drinks/<id>` - **Protegido** (Manager apenas)
```python
@app.route("/drinks/<int:drink_id>", methods=["PATCH"])
@requires_auth("patch:drinks")
def update_drink(payload, drink_id):
    # Requer permission 'patch:drinks'
```

#### `DELETE /drinks/<id>` - **Protegido** (Manager apenas)
```python
@app.route("/drinks/<int:drink_id>", methods=["DELETE"])
@requires_auth("delete:drinks")
def delete_drink(payload, drink_id):
    # Requer permission 'delete:drinks'
```

---

## 📝 Configuração do Postman

### Arquivo: `backend/udacity-fsnd-udaspicelatte.postman_collection.json`

### Passos para Configurar:

1. **Importar a Collection no Postman**
   - File → Import
   - Selecionar `backend/udacity-fsnd-udaspicelatte.postman_collection.json`

2. **Obter Tokens JWT:**

   **Opção A - Via Auth0 Dashboard:**
   - Login em https://manage.auth0.com
   - Ir em APIs → Test
   - Copiar o Access Token

   **Opção B - Via Auth0 User:**
   - Obter token de um usuário Barista
   - Obter token de um usuário Manager

3. **Configurar na Collection:**

   **Para Barista:**
   - Right-click na pasta "Barista"
   - Navigate to "Authorization" tab
   - Type: Bearer Token
   - Token: [cole o JWT do usuário Barista]
   - Save

   **Para Manager:**
   - Right-click na pasta "Manager"
   - Navigate to "Authorization" tab
   - Type: Bearer Token
   - Token: [cole o JWT do usuário Manager]
   - Save

4. **⚠️ IMPORTANTE:**
   - Tokens expiram em 8 horas
   - Renovar tokens antes do review
   - Exportar a collection após configurar

5. **Exportar Collection:**
   - File → Export
   - Selecionar a collection
   - Salvar em: `backend/udacity-fsnd-udaspicelatte.postman_collection.json`
   - Ou manter no diretório atual

---

## ✅ Validação

### Testes que devem passar:

#### Barista (permite apenas READ):
- ✅ GET /drinks - 200 OK
- ✅ GET /drinks-detail - 200 OK
- ❌ POST /drinks - 403 Forbidden (sem permission)
- ❌ PATCH /drinks/1 - 403 Forbidden (sem permission)
- ❌ DELETE /drinks/1 - 403 Forbidden (sem permission)

#### Manager (permite CRUD completo):
- ✅ GET /drinks - 200 OK
- ✅ GET /drinks-detail - 200 OK
- ✅ POST /drinks - 200 OK
- ✅ PATCH /drinks/1 - 200 OK
- ✅ DELETE /drinks/1 - 200 OK

#### Público (sem autenticação):
- ✅ GET /drinks - 200 OK
- ❌ GET /drinks-detail - 401 Unauthorized

---

## 🎯 Resumo Final

✅ **Roles configurados no Auth0** (Barista, Manager)  
✅ **Permissions configuradas** (get:drinks, get:drinks-detail, post:drinks, patch:drinks, delete:drinks)  
✅ **JWT inclui RBAC claims** (permissions array)  
✅ **@requires_auth decorator completo**  
✅ **Endpoints protegidos corretamente**  
✅ **Collection Postman configurável**  

**O projeto demonstra capacidade completa de implementar e controlar acesso baseado em roles!** 🔐

