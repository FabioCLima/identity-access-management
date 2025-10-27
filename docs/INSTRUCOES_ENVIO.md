# 📤 Instruções Finais de Envio - Coffee Shop

## ✅ Checklist Pré-Envio

### 1. Backend Completo
- [x] Todos endpoints implementados
- [x] Auth.py com JWT completo
- [x] RBAC implementado
- [x] Error handlers completos
- [x] Código sem TODOs

### 2. Auth0 Configurado
- [ ] Criar conta Auth0
- [ ] Criar API com RBAC habilitado
- [ ] Criar Role: Barista (permissions: get:drinks, get:drinks-detail)
- [ ] Criar Role: Manager (permissions: get:drinks, get:drinks-detail, post:drinks, patch:drinks, delete:drinks)
- [ ] Configurar `.env` com credenciais

### 3. Postman Collection
- [ ] Importar collection em Postman
- [ ] Obter JWT de usuário Barista
- [ ] Obter JWT de usuário Manager
- [ ] Configurar tokens na collection (Authorization tab)
- [ ] Testar todos os endpoints
- [ ] Exportar collection atualizada
- [ ] Salvar em: `backend/udacity-fsnd-udaspicelatte.postman_collection.json`

---

## 🔐 Configurar Auth0

### Passo a Passo:

1. **Criar conta Auth0**
   - Acesse https://auth0.com
   - Crie conta gratuita
   - Escolha tenant domain

2. **Criar API**
   - Applications → APIs → Create API
   - Identifier: `coffee-shop-api`
   - Enable RBAC: ✅ ON
   - Enable Add Permissions in Access Token: ✅ ON

3. **Criar Permissions**
   - Vá em APIs → coffee-shop-api → Permissions
   - Criar:
     - `get:drinks`
     - `get:drinks-detail`
     - `post:drinks`
     - `patch:drinks`
     - `delete:drinks`

4. **Criar Roles**
   
   **Barista:**
   - Auth0 Dashboard → User Management → Roles
   - Create Role: "Barista"
   - Adicionar permissions: `get:drinks`, `get:drinks-detail`
   
   **Manager:**
   - Create Role: "Manager"
   - Adicionar todas permissions: `get:drinks`, `get:drinks-detail`, `post:drinks`, `patch:drinks`, `delete:drinks`

5. **Criar Usuários**
   - User Management → Users → Create User
   - Criar 2 usuários
   - Atribuir Role: Um como Barista, outro como Manager

---

## 🧪 Configurar Postman Collection

### 1. Obter Tokens JWT

**Método 1 - Auth0 Dashboard:**
```
Auth0 Dashboard → Applications → APIs → cooffee-shop-api → Test
```

Copiar o Access Token gerado (válido por 8 horas).

**Método 2 - Login real:**
- Fazer login como usuário Barista
- Obter JWT
- Fazer login como usuário Manager
- Obter JWT

### 2. Configurar na Collection

1. Abrir Postman
2. File → Import → `backend/udacity-fsnd-udaspicelatte.postman_collection.json`
3. Expandir a collection

**Para Barista folder:**
- Right-click em "Barista"
- Authorization tab
- Type: Bearer Token
- Token: [JWT do Barista]
- ✅ Save

**Para Manager folder:**
- Right-click em "Manager"
- Authorization tab
- Type: Bearer Token
- Token: [JWT do Manager]
- ✅ Save

### 3. Testar Todos os Endpoints

Execute cada request e verifique status codes:

**Barista:**
- GET /drinks → 200
- GET /drinks-detail → 200
- POST /drinks → 403
- PATCH /drinks/1 → 403
- DELETE /drinks/1 → 403

**Manager:**
- GET /drinks → 200
- GET /drinks-detail → 200
- POST /drinks → 200
- PATCH /drinks/1 → 200
- DELETE /drinks/1 → 200

### 4. Exportar Collection

1. File → Export
2. Selecionar a collection
3. Export To File
4. Salvar em: `backend/udacity-fsnd-udaspicelatte.postman_collection.json`

---

## ⚠️ IMPORTANTE

### Tokens JWT Expirem em 8 Horas!

- Renove tokens antes de submeter
- Verifique se tokens estão válidos
- Teste a collection após exportar
- Certifique-se de que todos os testes passam

---

## 📦 Preparar Submission

### Arquivos para Enviar:

```
coffee-shop/
├── README.md                    # ✅ Principal
├── LICENSE.md                   # ✅ Licença
├── backend/
│   ├── src/                     # ✅ Todo código
│   ├── pyproject.toml          # ✅ Configuração
│   ├── requirements.txt         # ✅ Dependências
│   ├── env.template             # ✅ Template
│   ├── README.md                # ✅ Docs backend
│   └── udacity-fsnd-udaspicelatte.postman_collection.json  # ⚠️  COM JWT CONFIGURADOS
├── frontend/                    # ✅ Frontend
├── starter-code/                # ✅ Referência
└── docs/                        # ✅ Documentação
```

---

## ✅ Verificação Final

Antes de enviar:

1. [ ] Todos endpoints funcionam?
2. [ ] Todos testes Postman passam?
3. [ ] Collection exportada com JWT válidos?
4. [ ] .env configurado?
5. [ ] Nenhum TODO no código?
6. [ ] Código formatado (Ruff)?
7. [ ] Documentação completa?

---

**🎉 Projeto pronto para envio! 🎉**

