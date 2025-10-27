# 🚀 Como Iniciar Tudo - Coffee Shop

## ⚠️ Backend Não Está Rodando

### Como Iniciar o Backend

**Execute em um terminal:**

```bash
cd /home/fabiolima/Workdir/udacity_projects/identity-access-management/coffee-shop/backend
./start_server.sh
```

**Você deve ver:**
```
Starting Coffee Shop Backend Server...
Activating virtual environment...
Installing dependencies...
Starting Flask server on http://localhost:5000
* Running on http://127.0.0.1:5000
```

**Manter este terminal aberto!**

---

## 🎯 Próximos Passos

### 1. Aguardar Backend Iniciar

Esperar aparecer: "* Running on http://127.0.0.1:5000"

### 2. Testar Backend

Abrir outro terminal e executar:

```bash
curl http://localhost:5000/drinks
```

**Se retornar JSON** = ✅ Backend OK!

### 3. Iniciar Frontend

Abrir outro terminal:

```bash
cd /home/fabiolima/Workdir/udacity_projects/identity-access-management/coffee-shop/frontend
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve
```

**Aguardar:** "dev server running: http://localhost:8100"

### 4. Abrir Navegador

**http://localhost:8100**

---

## ✅ Estrutura de Terminais

```
TERMINAL 1: Backend (rodar ./start_server.sh)
TERMINAL 2: Frontend (rodar ionic serve)
NAVEGADOR: http://localhost:8100
```

---

## 🆘 Se Backend Não Iniciar

### Verificar Python e Dependências:

```bash
cd backend
python3 --version
source .venv/bin/activate
pip list | grep Flask
```

### Reinstalar Dependências:

```bash
cd backend
source .venv/bin/activate
pip install -r requirements.txt
```

### Rodar Manualmente:

```bash
cd backend/src
python3 api.py
```

---

## 📚 Comandos Úteis

```bash
# Testar se backend responde
curl http://localhost:5000/drinks

# Ver processos Flask
ps aux | grep flask

# Ver porta 5000
lsof -i :5000

# Matar processo na porta 5000
kill -9 $(lsof -t -i:5000)
```

---

**Execute:** `cd backend && ./start_server.sh` e aguarde iniciar!

