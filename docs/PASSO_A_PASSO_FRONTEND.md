# 🚀 Como Finalizar o Frontend - Passo a Passo

## 📍 O Que Você Precisa Fazer Como Desenvolvedor

### ✅ Status Atual:
- Backend: ✅ **PRONTO** (backend/.env configurado)
- Frontend: ⚠️ **PRECISA CONFIGURAR** (apenas 3 passos!)

---

## 🎯 PASSO A PASSO - Configure em 5 Minutos

### PASSO 1: Configurar environment.ts (2 minutos)

**Editar o arquivo:**
```bash
cd frontend
code src/environments/environment.ts
# ou
nano src/environments/environment.ts
```

**Substituir por:**
```typescript
export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000',
  auth0: {
    url: 'dev-huk2wemon6z8ehay',
    audience: 'coffee-shop-api',
    clientId: 'GoLpoo1s5t58RaJ6R2XQeiyN3eUUP8QV',
    callbackURL: 'http://localhost:8100',
  }
};
```

**✅ Salvar e fechar**

---

### PASSO 2: Instalar Dependências (1 minuto)

```bash
cd frontend

# Instalar dependências
npm install

# Se der erro OpenSSL, executar antes:
export NODE_OPTIONS=--openssl-legacy-provider
npm install
```

**Aguarde terminar a instalação** (pode demorar 1-2 minutos)

---

### PASSO 3: Rodar Backend (se ainda não está rodando)

```bash
# Em um terminal
cd backend
./start_server.sh
```

**Verificar:** Abrir http://localhost:5000/drinks deve mostrar JSON

---

### PASSO 4: Rodar Frontend (1 minuto)

```bash
# Em outro terminal
cd frontend

# Rodar com OpenSSL legacy
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve
```

**Aguarde iniciar** (aparecerá "dev server running: http://localhost:8100")

---

### PASSO 5: Testar no Navegador

1. **Abrir:** http://localhost:8100
2. **Ver página:** Deve mostrar botão "Login"
3. **Clicar Login:** Redireciona para Auth0
4. **Fazer login:** Com credenciais do Auth0
5. **Verificar:** Volta e mostra drinks

**✅ Frontend está funcionando!**

---

## 🧪 Testes Detalhados

### Teste 1: Login Funciona?
- ✅ Clique em Login
- ✅ Redireciona para Auth0
- ✅ Login bem-sucedido
- ✅ Volta para app com drinks

### Teste 2: Drinks Aparecem?
- ✅ Lista de drinks visível
- ✅ Gráficos de proporções corretos
- ✅ Detalhes das receitas aparecem

### Teste 3: Permissions (Barista)?
- Verificar botões habilitados/desabilitados
- ✅ Get Drink Details funciona
- ❌ Criar/Editar/Deletar bloqueado

### Teste 4: Permissions (Manager)?
- ✅ Todas ações habilitadas
- ✅ Criar funciona
- ✅ Editar funciona  
- ✅ Deletar funciona

---

## 🆘 Se Algo Não Funcionar

### Erro: "Cannot find module"

```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Erro: OpenSSL Legacy Provider

```bash
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve
```

### Frontend não conecta ao Backend

**Verificar:**
1. Backend está rodando? (http://localhost:5000)
2. apiServerUrl está correto? ('http://127.0.0.1:5000')
3. CORS habilitado no backend?

### Auth0 não funciona

**Verificar:**
1. environment.ts configurado corretamente?
2. url, audience, clientId corretos?
3. Auth0 Dashboard - Application ativa?

---

## ✅ Checklist Final

```bash
# ✅ environment.ts configurado
# ✅ npm install executado  
# ✅ Backend rodando (localhost:5000)
# ✅ Frontend rodando (localhost:8100)
# ✅ Login funciona
# ✅ Drinks carregam
# ✅ Permissions corretas

🎉 FRONTEND PRONTO!
```

---

## 📚 Documentação de Referência

- **docs/TESTE_FRONTEND.md** - Testes detalhados
- **docs/FRONTEND_SETUP.md** - Setup completo
- **docs/CONFIGURACAO_PROJETO.md** - Configuração geral

---

## 🎯 Resumo Executivo

**Você só precisa:**

1. Editar 1 arquivo: `frontend/src/environments/environment.ts`
2. Rodar 2 comandos: `npm install` e `ionic serve`
3. Testar: Abrir http://localhost:8100

**É só isso! Leva 5 minutos!** ⏱️

