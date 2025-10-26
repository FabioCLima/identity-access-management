# Coffee Shop Project - Roteiro de Execução

## 📋 Visão Geral

Este documento detalha o roteiro completo para executar e testar o projeto Coffee Shop Full Stack.

## 🎯 Fases do Projeto

### Fase 1: Configuração Inicial (1-2 horas)

#### 1.1 Verificar Dependências
```bash
# Verificar Python
python --version  # Deve ser 3.11+

# Verificar uv (Python package manager)
uv --version

# Verificar Node.js
node --version

# Verificar npm
npm --version

# Verificar Ionic CLI
ionic --version
```

#### 1.2 Configurar Auth0
- [ ] Criar conta Auth0 (https://auth0.com)
- [ ] Criar API no Auth0 Dashboard
- [ ] Habilitar RBAC
- [ ] Criar permissões (get:drinks, get:drinks-detail, post:drinks, patch:drinks, delete:drinks)
- [ ] Criar roles (Barista, Manager)
- [ ] Criar usuários de teste
- [ ] Atribuir roles aos usuários

**Documento de referência:** `docs/backend/AUTH0_SETUP.md`

#### 1.3 Obter JWT Tokens
```bash
cd backend
./get_auth0_token.sh
```

Ou manualmente:
```bash
curl -X POST https://YOUR-DOMAIN.auth0.com/oauth/token \
  -H "Content-Type: application/json" \
  -d '{
    "client_id":"YOUR_CLIENT_ID",
    "client_secret":"YOUR_CLIENT_SECRET",
    "audience":"YOUR_API_AUDIENCE",
    "grant_type":"client_credentials"
  }'
```

---

### Fase 2: Setup Backend (30 minutos)

#### 2.1 Preparar Ambiente Python
```bash
cd ~/Workdir/udacity_projects/identity-access-management/coffee-shop/backend

# Criar ambiente virtual
uv venv

# Ativar ambiente
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

#### 2.2 Instalar Dependências
```bash
# Instalar com uv
uv pip install -r requirements.txt

# Verificar instalação
uv pip list
```

#### 2.3 Configurar Variáveis de Ambiente
```bash
# Criar arquivo .env
cat > .env << EOF
AUTH0_DOMAIN=your-domain.auth0.com
AUTH0_ALGORITHM=RS256
AUTH0_API_AUDIENCE=coffee-shop-api
FLASK_ENV=development
FLASK_DEBUG=True
EOF
```

#### 2.4 Inicializar Banco de Dados (Primeira execução)
```bash
# Opção A: Usando Python direto
cd backend
source .venv/bin/activate
python -c "from src.database.models import db_drop_and_create_all; db_drop_and_create_all()"

# Opção B: Editar api.py temporariamente
# Descomentar a linha db_drop_and_create_all() em src/api.py por uma vez
# Executar: flask run
# Comentar novamente
```

---

### Fase 3: Executar Backend (5 minutos)

#### 3.1 Iniciar Servidor Flask

**Opção 1: Usando o script (RECOMENDADO)**
```bash
cd backend
./start_server.sh
```

**Opção 2: Manual**
```bash
cd backend
source .venv/bin/activate
export FLASK_APP=src.api  # ← CORRETO: src.api é o módulo Python
flask run --host=0.0.0.0 --reload
```

**Verificar:** Servidor deve estar em http://localhost:5000

#### 3.2 Testar Endpoint Público
```bash
curl http://localhost:5000/drinks
```

**Resposta esperada:**
```json
{
  "success": true,
  "drinks": []
}
```

---

### Fase 4: Setup Frontend (30 minutos)

#### 4.1 Preparar Ambiente Node
```bash
cd ~/Workdir/udacity_projects/identity-access-management/coffee-shop/frontend

# Instalar dependências
npm install

# Se houver erro com node-sass
npm uninstall node-sass
npm install node-sass@4.14.1
```

#### 4.2 Configurar Auth0 no Frontend
Editar `frontend/src/environments/environment.ts`:

```typescript
export const environment = {
  apiServerUrl: 'http://localhost:5000',
  auth0Domain: 'your-domain.auth0.com',
  auth0ClientId: 'your-client-id',
};
```

#### 4.3 Executar Frontend
```bash
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve
```

**Verificar:** App deve abrir em http://localhost:8100

---

### Fase 5: Configurar Postman (15 minutos)

#### 5.1 Atualizar Collection com JWT Tokens
```bash
cd backend

# Com os tokens obtidos
python update_postman_auth.py \
  udacity-fsnd-udaspicelatte.postman_collection.json \
  <barista_token> \
  <manager_token>
```

#### 5.2 Importar no Postman
1. Abrir Postman
2. Clicar em "Import"
3. Selecionar arquivo atualizado
4. Verificar 3 pastas: public, barista, manager

---

### Fase 6: Testar Endpoints (30 minutos)

#### 6.1 Testes Públicos (Sem Auth)
- [ ] GET /drinks - Deve retornar drinks (pode estar vazio)

#### 6.2 Testes com Token Barista
- [ ] GET /drinks - Deve funcionar
- [ ] GET /drinks-detail - Deve retornar detalhes completos
- [ ] POST /drinks - Deve falhar (403 Forbidden)
- [ ] PATCH /drinks/:id - Deve falhar (403 Forbidden)
- [ ] DELETE /drinks/:id - Deve falhar (403 Forbidden)

#### 6.3 Testes com Token Manager
- [ ] GET /drinks - Deve funcionar
- [ ] GET /drinks-detail - Deve funcionar
- [ ] POST /drinks - Deve criar novo drink
- [ ] PATCH /drinks/:id - Deve atualizar drink
- [ ] DELETE /drinks/:id - Deve deletar drink

---

### Fase 7: Testes Manuais com cURL (15 minutos)

#### 7.1 Teste Endpoint Público
```bash
curl http://localhost:5000/drinks
```

#### 7.2 Teste Com Barista Token
```bash
BARISTA_TOKEN="seu_token_aqui"

curl -H "Authorization: Bearer $BARISTA_TOKEN" \
  http://localhost:5000/drinks-detail
```

#### 7.3 Teste Com Manager Token (Criar Drink)
```bash
MANAGER_TOKEN="seu_token_aqui"

curl -X POST http://localhost:5000/drinks \
  -H "Authorization: Bearer $MANAGER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Espresso",
    "recipe": [
      {"name": "espresso", "color": "brown", "parts": 1}
    ]
  }'
```

#### 7.4 Teste Update
```bash
curl -X PATCH http://localhost:5000/drinks/1 \
  -H "Authorization: Bearer $MANAGER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Espresso"}'
```

#### 7.5 Teste Delete
```bash
curl -X DELETE http://localhost:5000/drinks/1 \
  -H "Authorization: Bearer $MANAGER_TOKEN"
```

---

### Fase 8: Verificação Final (15 minutos)

#### 8.1 Verificar Requisitos Funcionais
- [ ] Gráficos de drinks são exibidos
- [ ] Usuários públicos podem ver drinks
- [ ] Baristas podem ver receitas detalhadas
- [ ] Managers podem criar drinks
- [ ] Managers podem editar drinks
- [ ] Managers podem deletar drinks

#### 8.2 Verificar Requisitos Técnicos
- [ ] Autenticação funcionando
- [ ] Autorização funcionando
- [ ] RBAC implementado
- [ ] API segura
- [ ] Validação de entrada
- [ ] Tratamento de erros

#### 8.3 Verificar Código
- [ ] PEP 8 compliant
- [ ] Documentação completa
- [ ] Nomes descritivos
- [ ] Comentários apropriados
- [ ] README detalhado

---

## 🐛 Troubleshooting

### Backend não inicia
```bash
# Verificar Flask está instalado
pip list | grep Flask

# Verificar arquivo api.py existe
ls backend/src/api.py

# Verificar variável FLASK_APP
echo $FLASK_APP
```

### Erro 401 Unauthorized
- Verificar token não expirou
- Verificar token está correto
- Verificar cabeçalho Authorization

### Erro 403 Forbidden
- Verificar permissões no Auth0
- Verificar usuário tem role correta
- Verificar RBAC está habilitado

### Frontend não conecta
- Verificar backend está rodando
- Verificar CORS configurado
- Verificar URL da API no environment.ts

---

## ⏱️ Tempo Total Estimado

- Setup inicial: 2 horas
- Execução e testes: 1 hora
- **Total: 3 horas**

## 📚 Documentação de Apoio

Consulte a pasta `docs/` para:
- Configuração Auth0: `docs/backend/AUTH0_SETUP.md`
- Guia de testes: `docs/backend/TESTING_GUIDE.md`
- Setup Postman: `docs/backend/POSTMAN_SETUP_SUMMARY.md`
- Deploy: `docs/DEPLOYMENT_GUIDE.md`
- Melhorias: `docs/ENHANCEMENT_SUGGESTIONS.md`

## ✅ Checklist de Sucesso

### Antes de Submeter:
- [ ] Todos os endpoints funcionando
- [ ] Auth0 configurado
- [ ] Postman collection testada
- [ ] Código PEP 8 compliant
- [ ] Documentação completa
- [ ] README atualizado
- [ ] Git repository limpo
- [ ] Zip criado para submissão

### Arquivos para Submissão:
- Código do backend
- Código do frontend
- Postman collection atualizado
- README.md
- requirements.txt
- Todas as documentações relevantes

## 🚀 Próximos Passos

Depois de concluir todas as fases:

1. Criar zip para submissão:
```bash
./create-submission-zip.sh
```

2. Revisar PRO strengths:
- Verificar `docs/ENHANCEMENT_SUGGESTIONS.md`
- Implementar melhorias adicionais
- Considerar deploy em nuvem

3. Finalizar documentação:
- Revisar todos os READMEs
- Adicionar screenshots (opcional)
- Verificar exemplos estão corretos

