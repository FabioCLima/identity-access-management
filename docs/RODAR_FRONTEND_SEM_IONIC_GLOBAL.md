# 🚀 Rodar Frontend SEM Instalar Ionic Globalmente

## ⚠️ Problema de Permissão

Você teve erro ao instalar Ionic globalmente (`EACCES: permission denied`).

## ✅ Solução: Usar npx (SEM instalação global)

Você NÃO precisa instalar Ionic globalmente! Pode usar `npx`:

### Comando Completo:

```bash
cd frontend
export NODE_OPTIONS=--openssl-legacy-provider
npx ionic serve
```

**Isso funciona sem instalar globalmente!**

---

## 🎯 Passo a Passo Completo

### Terminal 1: Backend

```bash
cd backend
./start_server.sh
```

**Aguardar:** "* Running on http://127.0.0.1:5000"

### Terminal 2: Frontend (SEM instalar globalmente)

```bash
cd frontend
export NODE_OPTIONS=--openssl-legacy-provider
npx ionic serve
```

**Aguardar:** "dev server running: http://localhost:8100"

### Abrir Navegador

**http://localhost:8100**

---

## ✅ Vantagem do npx

- ✅ Não precisa instalar globalmente
- ✅ Não precisa sudo
- ✅ Pega versão correta automaticamente
- ✅ Funciona imediatamente

---

## 🆘 Alternativa: Instalar com sudo (se quiser)

Se preferir instalar globalmente:

```bash
sudo npm install -g @ionic/cli
```

Mas **não é necessário!** `npx ionic serve` funciona perfeitamente.

---

## 📝 Comandos Finais

```bash
# Terminal 1 - Backend
cd /home/fabiolima/Workdir/udacity_projects/identity-access-management/coffee-shop/backend
./start_server.sh

# Terminal 2 - Frontend (COM NPX - SEM INSTALAR!)
cd /home/fabiolima/Workdir/udacity_projects/identity-access-management/coffee-shop/frontend
export NODE_OPTIONS=--openssl-legacy-provider
npx ionic serve

# Navegador
# http://localhost:8100
```

---

## 🎉 Resumo

**Você já tem tudo instalado (Node.js, npm, dependências do projeto)!**

**Só precisa usar `npx ionic serve` ao invés de `ionic serve`**

**É isso! Execute o comando com `npx` e vai funcionar!**

