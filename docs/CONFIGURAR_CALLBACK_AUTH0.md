# 🔧 Configurar Callback URL no Auth0

## ⚠️ Problema: Callback URL Mismatch

**Erro:** "redirect_uri is not in the list of allowed callback URLs"

**Causa:** Auth0 não tem a URL de callback permitida na configuração da Application.

---

## ✅ Solução: Configurar no Auth0 Dashboard

### Passo 1: Acessar Auth0 Dashboard

1. **Abrir:** https://manage.auth0.com
2. **Login** com suas credenciais

### Passo 2: Ir para Applications

1. **Sidebar** → **Applications** → **Applications**
2. **Clicar** na sua aplicação (SPA)

### Passo 3: Configurar Callback URLs

**Na página da Application, procurar:**

```
Allowed Callback URLs
Allowed Logout URLs
```

**Adicionar estas URLs:**

```
http://localhost:8100
http://localhost:8100/*
http://localhost:8100/callback
http://localhost:8100/tabs/user-page
```

**OU** adicionar wildcard:

```
http://localhost:8100/*
```

### Passo 4: Salvar Mudanças

1. **Scroll down** até ver botão **"Save Changes"**
2. **Clicar em Save**

### Passo 5: Verificar Configuração

Você deve ver algo como:

```
Allowed Callback URLs:
http://localhost:8100
http://localhost:8100/*
http://localhost:8100/callback

Allowed Logout URLs:
http://localhost:8100
```

---

## 🚀 Após Configurar

### 1. Aguardar 1-2 minutos

Auth0 pode levar alguns segundos para atualizar.

### 2. Testar Novamente

1. **Recarregar** página http://localhost:8100
2. **Clicar** em "Login"
3. **Agora deve funcionar!**

---

## 📋 Checklist de Configuração Auth0

Na Application do Auth0, verificar:

- [ ] **Allowed Callback URLs** contém `http://localhost:8100`
- [ ] **Allowed Logout URLs** contém `http://localhost:8100`
- [ ] **Allowed Web Origins** contém `http://localhost:8100`
- [ ] **Application Type** é "Single Page Application"
- [ ] **Mudanças salvas** (botão Save)

---

## 🔍 Como Verificar URL Correta

### Ver no Console do Navegador:

Pressione **F12** → **Console**

Procurar mensagem como:
```
redirect_uri=http://localhost:8100/...
```

**Essa URL precisa estar na lista de Allowed Callback URLs do Auth0!**

---

## 🆘 Se Ainda Não Funcionar

### Verificar URL Exata no Erro:

O erro pode mostrar:
```
redirect_uri=http://localhost:8100/tabs/user-page
```

**Adicionar essa URL exata** na lista de callbacks!

### Ou Adicionar Todas:

No Auth0, adicionar todas estas URLs:

```
http://localhost:8100
http://localhost:8100/
http://localhost:8100/*
http://localhost:8100/tabs/user-page
http://localhost:8100/callback
http://localhost:8100/tabs/user-page/
```

---

## ✅ Resumo Rápido

**O que fazer:**

1. **Abrir:** https://manage.auth0.com
2. **Applications** → sua SPA application
3. **Scroll** até "Allowed Callback URLs"
4. **Adicionar:** `http://localhost:8100`
5. **Adicionar:** `http://localhost:8100/*`
6. **Salvar** changes
7. **Aguardar** 1 minuto
8. **Testar** login novamente

**Deve funcionar agora!** ✅

