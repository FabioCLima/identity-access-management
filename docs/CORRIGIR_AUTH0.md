# ⚠️ Erro: Unknown Host - Auth0

## 🔍 Problema

**Erro:** `Unknown host: dev-huk2wemon6z8ehay.auth0.com`

**Causa:** O domínio Auth0 não existe ou está incorreto.

---

## 🔧 Soluções

### Opção 1: Verificar Domínio Auth0 Correto

1. **Login em Auth0:**
   https://manage.auth0.com

2. **Applications** → SPA Application
3. **Verificar Domain:**
   - Onde está o valor correto?
   - Exemplo: `dev-xxxxx.us.auth0.com`

### Opção 2: Criar Novo Tenant Auth0 (se necessário)

Se o domínio não existe, você precisa:

1. **Criar conta Auth0:**
   https://auth0.com/signup

2. **Escolher Tenant:**
   - Criar novo tenant
   - Exemplo: `seu-app.auth0.com`

3. **Configurar .env:**
   ```bash
   cd backend
   nano .env
   ```
   
   Adicionar:
   ```
   AUTH0_DOMAIN=seu-app.auth0.com
   ```

4. **Configurar environment.ts:**
   ```typescript
   auth0: {
     url: 'seu-app',  // Apenas o prefixo, SEM .auth0.com
     audience: 'coffee-shop-api',
     clientId: 'seu-client-id',
   }
   ```

---

## ⚠️ Domínio Atual vs Correto

### Atual (INCORRETO):
```
dev-huk2wemon6z8ehay.auth0.com
```

### Formato Correto:
```
xxxxx.auth0.com      → Domínio padrão
xxxxx.us.auth0.com   → US Region
xxxxx.eu.auth0.com   → EU Region
```

---

## 🔍 Como Verificar Domínio Correto

### 1. Acessar Auth0 Dashboard

```
https://manage.auth0.com
```

### 2. Ver Applications → Domain

Copiar o valor exato do domínio.

### 3. Verificar no .env

```bash
cd backend
cat .env | grep AUTH0_DOMAIN
```

### 4. Comparar com environment.ts

```bash
cd frontend
cat src/environments/environment.ts
```

**Os valores devem combinar!**

---

## 🆘 Solução Temporária: Desabilitar Auth

Para testar apenas a visualização (sem login):

### Editar environment.ts:

```typescript
export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000',
  auth0: {
    url: 'udacity-fsnd',  // Usar domínio padrão
    audience: 'dev',
    clientId: '',  // Vazio por enquanto
    callbackURL: 'http://localhost:8100',
  }
};
```

Mas isso **não vai funcionar completamente** porque precisa de Auth0 real.

---

## ✅ Solução Correta

### 1. Criar/Acessar Auth0

- Criar conta em https://auth0.com
- Criar Application (SPA)
- Copiar Client ID e Domain

### 2. Atualizar environment.ts

```typescript
auth0: {
  url: 'seu-tenant-correcto',  // Do Auth0 dashboard
  audience: 'coffee-shop-api',
  clientId: 'seu-client-id-correto',  // Do Auth0 dashboard
  callbackURL: 'http://localhost:8100',
}
```

### 3. Atualizar backend .env

```bash
AUTH0_DOMAIN=seu-tenant-correcto.auth0.com
```

---

## 📝 Checklist de Configuração Auth0

- [ ] Conta Auth0 criada
- [ ] Application criada (SPA)
- [ ] API criada com RBAC
- [ ] Roles criadas (Barista, Manager)
- [ ] Permissions criadas
- [ ] Usuários criados
- [ ] Client ID copiado
- [ ] Domain copiado
- [ ] Configurado no environment.ts
- [ ] Configurado no backend .env

---

**O domínio Auth0 precisa ser o CORRETO do seu Auth0 dashboard!**

Verifique em: https://manage.auth0.com

