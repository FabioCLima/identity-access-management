# 🚀 Como Iniciar o Backend Corretamente

## ⚠️ Backend Não Está Rodando

Baseado no erro de conexão, o backend parou ou não iniciou corretamente.

## 🔧 Como Rodar o Backend

### Opção 1: Script Automático

```bash
cd backend
./start_server.sh
```

### Opção 2: Manual

```bash
cd backend

# Ativar ambiente virtual
source .venv/bin/activate

# Exportar variáveis do .env
export $(cat .env | grep -v '^#' | xargs)

# Configurar Flask
export FLASK_APP=src/api.py
export FLASK_ENV=development
export FLASK_DEBUG=1

# Rodar servidor
flask run --reload
```

### Opção 3: Com uv

```bash
cd backend
source .venv/bin/activate
uv pip install -r requirements.txt
export FLASK_APP=src/api.py
flask run --reload
```

---

## ✅ Verificar se Funcionou

### Ver Logs:

Você deve ver:
```
* Running on http://127.0.0.1:5000
* Debug mode: on
* Debugger is active!
```

### Testar:

```bash
curl http://localhost:5000/drinks
```

**Deve retornar:** JSON com drinks

---

## 🆘 Problemas Comuns

### Erro: "No module named flask"

```bash
cd backend
source .venv/bin/activate
pip install -r requirements.txt
```

### Erro: "Address already in use"

Porta 5000 ocupada. Use outra:

```bash
flask run --port=5001
```

E configure frontend para usar porta 5001.

### Erro: Import errors

```bash
cd backend/src
python -m flask run
```

---

## 📝 Passo a Passo Completo

```bash
# 1. Ir para pasta backend
cd /home/fabiolima/Workdir/udacity_projects/identity-access-management/coffee-shop/backend

# 2. Ativar venv
source .venv/bin/activate

# 3. Verificar dependências
pip list | grep Flask

# 4. Rodar servidor
export FLASK_APP=src/api.py
flask run --reload
```

**Aguardar:** Logs mostrando servidor rodando

---

## ✅ Quando Está Funcionando

Você verá:
- "* Running on http://127.0.0.1:5000"
- "* Debug mode: on"
- Nenhum erro vermelho

**Testar endpoint:**
```bash
curl http://localhost:5000/drinks
```

**Se retornar JSON = Backend OK!** ✅

---

## 🚀 Próximo: Frontend

Após backend rodar:

```bash
cd ../frontend
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve
```

---

**Execute:** `cd backend && ./start_server.sh` e aguarde os logs!

