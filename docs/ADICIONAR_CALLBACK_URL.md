# 🔧 Adicionar Callback URL no Auth0

## ⚠️ Erro Atual

**Callback URL mismatch:**
```
http://localhost:8100/tabs/user-page is not in the list of allowed callback URLs
```

---

## ✅ Solução: Adicionar URL no Auth0

### Passo 1: Abrir Auth0 Dashboard

1. **Ir:** https://manage.auth0.com
2. **Applications** → **Coffee Shop Frontend** (SPA)

### Passo 2: Encontrar "Allowed Callback URLs"

Scroll down até ver esta seção:
```
┌─────────────────────────────────────────────┐
│ Allowed Callback URLs                       │
├─────────────────────────────────────────────┤
│ http://localhost:8100                       │
└─────────────────────────────────────────────┘
```

### Passo 3: Adicionar URLs

**Substituir por:**

```
http://localhost:8100
http://localhost:8100/*
http://localhost:8100/tabs/user-page
```

**OU** adicionar apenas:
```
http://localhost:8100/*
```

(O wildcard `/*` cobre todas as URLs incluindo `/tabs/user-page`)

### Passo 4: Salvar

1. **Scroll down** até botão **"Save Changes"**
2. **Clicar** em Save
3. **Aguardar** confirmação

### Passo 5: Testar Novamente

1. **Aguardar** ~30 segundos
2. **Recarregar** página: http://localhost:8100
3. **Clicar** em "Login"
4. **Agora deve funcionar!** ✅

---

## 📝 Configuração Recomendada

**Na sua SPA Application (Coffee Shop Frontend):**

```
Allowed Callback URLs:
  http://localhost:8100
  http://localhost:8100/*
  http://localhost:8100/tabs/user-page

Allowed Logout URLs:
  http://localhost:8100

Allowed Web Origins:
  http://localhost:8100
```

---

## ✅ Resumo Rápido

**Problema:** URL `/tabs/user-page` não está na lista  
**Solução:** Adicionar no Auth0 Dashboard  
**Ação:** `http://localhost:8100/*` + Save + Testar

**Deve funcionar!** 🎉

