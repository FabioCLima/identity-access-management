# 🚀 Como Finalizar o Frontend - GUIA RÁPIDO

## ⏱️ 3 Passos - 5 Minutos

Você só precisa fazer **3 coisas** para o frontend funcionar:

---

## PASSO 1: Editar Environment File ⏱️ 1 minuto

```bash
cd frontend
code src/environments/environment.ts
```

**Substituir todo o conteúdo por:**

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

**Salvar e fechar**

---

## PASSO 2: Instalar Dependências ⏱️ 2 minutos

```bash
cd frontend
npm install
```

Se der erro com OpenSSL:
```bash
export NODE_OPTIONS=--openssl-legacy-provider
npm install
```

**Aguardar terminar** (pode demorar 1-2 minutos)

---

## PASSO 3: Rodar o Frontend ⏱️ 1 minuto

```bash
cd frontend
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve
```

**Abrir navegador:** http://localhost:8100

---

## ✅ Verificar se Funcionou

1. **Página abre?** ✅ Sim → Continuar | ❌ Não → Ver Troubleshooting
2. **Clicar "Login"?** ✅ Redireciona Auth0 → Continuar | ❌ Não → Ver Auth0
3. **Fazer login?** ✅ Volta com drinks → **FRONTEND FUNCIONANDO!** 🎉

---

## 🆘 Problemas Comuns

### Erro: npm install falha
```bash
rm -rf node_modules package-lock.json
npm install
```

### Erro: OpenSSL
```bash
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve
```

### Frontend não conecta ao backend
- Verificar: Backend rodando em http://localhost:5000
- Executar: `cd backend && ./start_server.sh`

---

## 📚 Mais Detalhes

- **docs/PASSO_A_PASSO_FRONTEND.md** - Guia detalhado
- **docs/TESTE_FRONTEND.md** - Como testar tudo
- **docs/CONFIGURACAO_PROJETO.md** - Configuração completa

---

## 🎯 RESUMO: Você Precisa

1. ✅ Editar `frontend/src/environments/environment.ts`
2. ✅ Rodar `npm install`
3. ✅ Rodar `ionic serve`

**É SÓ ISSO! Leva 5 minutos!** ⏱️

