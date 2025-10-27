# Coffee Shop Full Stack

## Full Stack Nano - IAM Final Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.

You have been called on to demonstrate your newly learned skills to create a full stack drink menu application. The application must:

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.

## 📋 Project Status

### ✅ Backend: 100% Complete
- All endpoints implemented (no TODOs)
- JWT authentication with Auth0
- RBAC (Role-Based Access Control)
- Tests created with pytest
- Ready to run

### ⚠️ Frontend: Needs Configuration
- Code ready
- **Need to configure:** `src/environments/environment.ts`
- **Need to install:** `npm install`
- **Need to test:** `ionic serve`

### ⚠️ Postman: Needs Tokens
- Collection ready
- **Need to add:** JWT tokens
- **Need to test:** All endpoints

---

## 🚀 Quick Start

### 1. Setup Backend

```bash
cd backend
./start_server.sh
```

Backend runs on: http://localhost:5000

### 2. Configure Frontend

Edit `frontend/src/environments/environment.ts`:

```typescript
auth0: {
  url: 'your-tenant',           // From Auth0 Dashboard
  audience: 'your-audience',    // From Auth0 Dashboard
  clientId: 'your-client-id',    // From Auth0 Dashboard
}
```

### 3. Setup Frontend

```bash
cd frontend
npm install
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve
```

Frontend runs on: http://localhost:8100

---

## 📚 Documentation

All detailed documentation is in `docs/`:

### Essential Guides
- **docs/TESTE_FRONTEND.md** - How to test frontend ⭐
- **docs/CONFIGURACAO_PROJETO.md** - Configuration guide
- **docs/MANUAL_TESTE_COMPLETO.md** - Complete testing manual

### Setup Guides
- **docs/FRONTEND_SETUP.md** - Frontend setup
- **docs/TESTE_BACKEND.md** - Backend testing
- **docs/RBAC_IMPLEMENTATION.md** - RBAC guide

---

## 🧪 Testing

### Backend Tests

```bash
cd backend
pytest
```

### Frontend Tests

See: `docs/TESTE_FRONTEND.md`

### Postman Tests

See: `docs/CONFIGURACAO_PROJETO.md`

---

## 📁 Project Structure

```
coffee-shop/
├── README.md                    # This file
├── LICENSE.md                   # License
│
├── backend/                     # Flask Backend ✅
│   ├── src/                     # Source code
│   ├── tests/                    # Test files
│   ├── .env                     # Configured ✅
│   └── pyproject.toml          # Configured
│
├── frontend/                    # Ionic Frontend
│   ├── src/
│   │   └── environments/
│   │       └── environment.ts  # ⚠️  Configure
│   └── package.json
│
├── starter-code/                # Reference code
│
└── docs/                        # Documentation
    └── *.md                     # All guides
```

---

## ✅ What's Complete

- ✅ Backend API (5 endpoints)
- ✅ Authentication (JWT + Auth0)
- ✅ Authorization (RBAC)
- ✅ Database models
- ✅ Error handlers
- ✅ Tests (pytest)
- ✅ Code formatted

## ⚠️ What Needs Configuration

- ⚠️ Frontend environment variables
- ⚠️ Postman JWT tokens
- ⚠️ Auth0 setup (if not done)

---

## 🎯 Next Steps

1. **Read:** `docs/TESTE_FRONTEND.md`
2. **Configure:** Frontend environment.ts
3. **Install:** `npm install` in frontend
4. **Test:** `ionic serve`
5. **Configure:** Postman with JWTs

---

## 📖 Detailed Guides

- **Configuration:** `docs/CONFIGURACAO_PROJETO.md`
- **Frontend Testing:** `docs/TESTE_FRONTEND.md`
- **Backend Testing:** `docs/TESTE_BACKEND.md`
- **Complete Testing:** `docs/MANUAL_TESTE_COMPLETO.md`
- **RBAC:** `docs/RBAC_IMPLEMENTATION.md`

---

## License

This project is part of the Udacity Full Stack Nanodegree program.
