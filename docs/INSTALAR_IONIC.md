# ⚠️ Ionic CLI Não Está Instalado

## 🔧 Como Instalar o Ionic CLI

### Instalar Ionic CLI

```bash
npm install -g @ionic/cli
```

### Aguardar Instalação

Isso pode levar 1-2 minutos. Aguarde o comando terminar.

### Verificar Instalação

```bash
ionic --version
```

**Deve mostrar:** versão do Ionic (ex: 7.2.1)

---

## 🚀 Após Instalação, Rodar Frontend

```bash
cd /home/fabiolima/Workdir/udacity_projects/identity-access-management/coffee-shop/frontend

# Exportar NODE_OPTIONS
export NODE_OPTIONS=--openssl-legacy-provider

# Rodar Ionic
ionic serve
```

### Aguardar

```
dev server running: http://localhost:8100
```

### Abrir Navegador

**http://localhost:8100**

---

## 🆘 Se Instalação Falhar

### Erro de Permissão:

```bash
sudo npm install -g @ionic/cli
```

### Com npx (sem instalar globalmente):

```bash
npx ionic serve
```

---

## ✅ Resumo: Comandos Completos

```bash
# 1. Instalar Ionic CLI
npm install -g @ionic/cli

# 2. Ir para pasta frontend
cd /home/fabiolima/Workdir/udacity_projects/identity-access-management/coffee-shop/frontend

# 3. Configurar OpenSSL
export NODE_OPTIONS=--openssl-legacy-provider

# 4. Rodar frontend
ionic serve
```

**Abrir navegador:** http://localhost:8100

---

## 📝 Estrutura de Terminais

```
TERMINAL 1: Backend
cd backend && ./start_server.sh

TERMINAL 2: Frontend  
npm install -g @ionic/cli
cd frontend
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve

NAVEGADOR: http://localhost:8100
```

---

**Execute:** `npm install -g @ionic/cli` primeiro!

