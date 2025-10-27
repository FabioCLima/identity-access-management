# 🧪 Como Testar o Frontend - Coffee Shop

## 📍 O Que Falta Configurar

### ✅ Backend: Pronto!
- .env configurado
- Código completo
- Auth0 configurado

### ⚠️ Frontend: Precisa Configurar

**Arquivo:** `frontend/src/environments/environment.ts`

**Status:** Vazio - Precisa preencher Auth0 variables

---

## 🔧 Como Configurar o Frontend

### Passo 1: Editar environment.ts

```bash
cd frontend
code src/environments/environment.ts
```

**Adicionar os valores do backend .env:**

```typescript
export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000',
  auth0: {
    url: 'dev-huk2wemon6z8ehay',              // ← Domain prefix
    audience: 'coffee-shop-api',              // ← API audience
    clientId: 'GoLpoo1s5t58RaJ6R2XQeiyN3eUUP8QV',  // ← Client ID
    callbackURL: 'http://localhost:8100',
  }
};
```

### Passo 2: Instalar Dependências

```bash
cd frontend
npm install
```

**⚠️ Se der erro com OpenSSL:**
```bash
export NODE_OPTIONS=--openssl-legacy-provider
npm install
```

### Passo 3: Verificar Backend Rodando

```bash
# Em um terminal
cd backend
./start_server.sh
```

**Verificar:** http://localhost:5000/drinks deve retornar JSON

### Passo 4: Rodar Frontend

```bash
# Em outro terminal
cd frontend
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve
```

**Abrir:** http://localhost:8100

---

## 🧪 Teste Completo do Frontend

### Teste 1: Página Inicial

1. Abrir: http://localhost:8100
2. **Verificar:**
   - ✅ Página abre sem erros
   - ✅ "Login" button visível
   - ✅ Sem erros no console do navegador (F12)

### Teste 2: Login

1. Clicar em "Login"
2. **Verificar:**
   - ✅ Redireciona para Auth0
   - ✅ Tela de login Auth0 aparece

**Fazer login:**
- Email e senha do usuário criado no Auth0
- Ou usar credenciais de teste

3. **Após login:**
   - ✅ Redireciona de volta para app
   - ✅ Token salvo no localStorage
   - ✅ Drinks carregam
   - ✅ Usuário logado

### Teste 3: Visualizar Drinks

**Após login, verificar:**
- ✅ Lista de drinks aparece
- ✅ Gráficos de proporções corretos
- ✅ Botão "Get Drink Details" funciona
- ✅ Detalhes das receitas aparecem

### Teste 4: Permissions (Role Barista)

**Se logado como Barista:**
- ✅ Ver drinks (funciona)
- ✅ Ver drink details (funciona)
- ❌ Criar drink (botão desabilitado)
- ❌ Editar drink (botão desabilitado)
- ❌ Deletar drink (botão desabilitado)

### Teste 5: Permissions (Role Manager)

**Se logado como Manager:**
- ✅ Ver drinks (funciona)
- ✅ Ver drink details (funciona)
- ✅ Criar drink (botão habilitado)
- ✅ Editar drink (botão habilitado)
- ✅ Deletar drink (botão habilitado)
- ✅ Todas operações funcionam

### Teste 6: CRUD Operations (Manager)

**Criar Drink:**
1. Clicar em "Create Drink"
2. Preencher formulário
3. Submit
4. **Verificar:** Drink aparece na lista

**Editar Drink:**
1. Clicar em "Edit"
2. Modificar dados
3. Submit
4. **Verificar:** Mudanças salvas

**Deletar Drink:**
1. Clicar em "Delete"
2. Confirmar
3. **Verificar:** Drink removido da lista

---

## 🔍 Verificações de Console

### Abrir Console do Navegador

**F12 → Console tab**

**Verificar se há erros:**
- ❌ Erros de Auth0
- ❌ Erros de CORS
- ❌ Erros de API connection
- ❌ Erros de permissions

**✅ Esperado:** Sem erros ou warnings relevantes

---

## 📊 Checklist Final de Testes

### Instalação
- [ ] `environment.ts` configurado
- [ ] `npm install` executado
- [ ] Sem erros na instalação

### Execução
- [ ] `ionic serve` inicia
- [ ] Página abre em http://localhost:8100
- [ ] Sem erros no console

### Autenticação
- [ ] Login funciona
- [ ] Token salvo no localStorage
- [ ] Callback Auth0 funciona

### Funcionalidades
- [ ] Drinks carregam
- [ ] Visualização funciona
- [ ] Permissions corretas (Barista)
- [ ] Permissions corretas (Manager)
- [ ] CRUD funciona (Manager)

---

## 🆘 Troubleshooting

### Erro: "Cannot find module"

```bash
rm -rf node_modules package-lock.json
npm install
```

### Erro: OpenSSL Legacy Provider

```bash
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve
```

### Erro: CORS

**Verificar backend:**
- Backend rodando em http://localhost:5000
- CORS habilitado no backend
- Frontend em http://localhost:8100

### Erro: Auth0 Connection

**Verificar:**
- environment.ts configurado corretamente
- Auth0 credentials corretos
- Callback URL correto

---

## ✅ Quando Está Funcionando

- ✅ Frontend abre sem erros
- ✅ Login redireciona para Auth0
- ✅ Após login, drinks aparecem
- ✅ Permissions funcionam corretamente
- ✅ CRUD operations funcionam (Manager)

**Frontend está funcional e pronto para uso!**

---

**Leia também:** `docs/FRONTEND_SETUP.md` para mais detalhes

