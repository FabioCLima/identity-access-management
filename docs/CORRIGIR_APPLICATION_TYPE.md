# ⚠️ Application Type Incorreto - Auth0

## 🔍 Problema Identificado

**Application atual:**
- Type: **Machine to Machine** ❌
- Client ID: `KNT5h1CaoPmZ11CzALx6uPyX0NuwSbRx`
- Client Secret: Tem (não usado em SPA)

**O que precisa:**
- Type: **Single Page Application** ✅
- Client ID diferente (para frontend)

---

## ✅ Solução: Criar Nova Application (SPA)

### Passo 1: Criar SPA Application

1. **Abrir:** https://manage.auth0.com
2. **Applications** → **Create Application**
3. **Name:** "Coffee Shop Frontend"
4. **Type:** Selecionar **"Single Page Application"**
5. **Clicar:** Create

### Passo 2: Configurar Application

**Na página da nova Application:**

**Allowed Callback URLs:**
```
http://localhost:8100
http://localhost:8100/*
http://localhost:8100/tabs/user-page
```

**Allowed Logout URLs:**
```
http://localhost:8100
```

**Allowed Web Origins:**
```
http://localhost:8100
```

**Application URIs → Logout URLs:**
```
http://localhost:8100
```

### Passo 3: Copiar Client ID

**Client ID** será algo como:
```
abc123...xyz789
```

**Salvar este Client ID!**

### Passo 4: Configurar Frontend

**Editar:** `frontend/src/environments/environment.ts`

```typescript
export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000',
  auth0: {
    url: 'dev-huk2wemon6z8ehay',
    audience: 'coffee-shop-api',
    clientId: 'NOVO_CLIENT_ID_AQUI',  // ← Usar Client ID da SPA
    callbackURL: 'http://localhost:8100',
  }
};
```

### Passo 5: Salvar e Reiniciar Frontend

```bash
cd frontend
export NODE_OPTIONS=--openssl-legacy-provider
npx ionic serve
```

---

## 🔄 Duas Applications Necessárias

### 1. Machine to Machine (para Backend)

- Type: **Machine to Machine** ✅
- Client ID: `KNT5h1CaoPmZ11CzALx6uPyX0NuwSbRx`
- **Usar:** Backend para operações admin

### 2. Single Page Application (para Frontend)

- Type: **Single Page Application** ✅
- Client ID: (novo - copiar ao criar)
- **Usar:** Frontend para login de usuários

---

## 📝 Checklist Completo

**No Auth0 Dashboard:**

- [ ] Application "Machine to Machine" existe (para backend)
- [ ] Application "SPA" criada (para frontend)
- [ ] Callback URLs configurados na SPA
- [ ] Client ID da SPA copiado
- [ ] environment.ts atualizado com novo Client ID
- [ ] Frontend reiniciado

---

## ✅ Resumo

**Você tem:**
- ✅ Machine to Machine application
- ❌ **Falta:** Single Page Application

**Ação:**
1. Criar SPA application no Auth0
2. Copiar novo Client ID
3. Atualizar environment.ts
4. Reiniciar frontend

**Depois vai funcionar!** 🎉

