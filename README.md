# Coffee Shop Full Stack

## Backend Developer with Python - Project Coffee Shop Full Stack

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.

You have been called on to demonstrate your newly learned skills to create a full stack drink menu application. The application must:

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.

---

## 📋 Project Status

### ✅ Backend: Complete
- All endpoints implemented (no TODOs)
- JWT authentication with Auth0
- RBAC (Role-Based Access Control)
- Tests created with pytest
- Ready to run

### ✅ Frontend: Configured
- Auth0 environment configured
- Login functional
- JWT tokens working
- RBAC permissions implemented

### ✅ Auth0: Configured
- SPA Application created
- Machine to Machine Application created
- Roles and Permissions configured
- Users created with roles

---

## 🚀 Quick Start

### 1. Start Backend

```bash
cd backend
./start_server.sh
```

Backend runs on: http://localhost:5000

### 2. Start Frontend

In a new terminal:

```bash
cd frontend
export NODE_OPTIONS=--openssl-legacy-provider
npx ionic serve
```

Frontend runs on: http://localhost:8100

### 3. Login & Test

1. Open http://localhost:8100
2. Click "Login"
3. Use Google OAuth (or configured Auth0 credentials)
4. You should see your JWT with permissions
5. Navigate and test creating/editing drinks

---

## 🧪 Testing

### Backend Tests

```bash
cd backend
pytest
```

With coverage:

```bash
pytest --cov
```

### Test Users

You can create test users via the script:

```bash
./criar_usuarios.sh
```

This creates:
- **Barista:** barista@coffeeshop.com / CoffeeShop2024!
- **Manager:** manager@coffeeshop.com / CoffeeShop2024!

---

## 📁 Project Structure

```
coffee-shop/
├── README.md                    # This file
│
├── backend/                     # Flask Backend
│   ├── src/
│   │   ├── api.py              # Main API file
│   │   ├── auth/               # Auth module
│   │   │   └── auth.py        # JWT verification
│   │   └── database/
│   │       └── models.py       # Drink model
│   ├── tests/                  # Test files
│   ├── .env                    # Environment variables
│   ├── pyproject.toml          # Dependencies
│   └── start_server.sh         # Start script
│
├── frontend/                    # Ionic Frontend
│   ├── src/
│   │   ├── app/
│   │   │   ├── services/
│   │   │   │   ├── auth.service.ts
│   │   │   │   └── drinks.service.ts
│   │   │   └── pages/
│   │   └── environments/
│   │       └── environment.ts  # Auth0 config
│   └── package.json
│
└── docs/                        # Documentation
    ├── STATUS_PARA_SUBMISSAO.md
    └── *.md                     # All guides
```

---

## ✅ Implementation Details

### Backend Endpoints

| Endpoint | Method | Access | Description |
|----------|--------|--------|-------------|
| `/drinks` | GET | Public | List all drinks (short format) |
| `/drinks-detail` | GET | Barista | List all drinks (detailed with recipes) |
| `/drinks` | POST | Manager | Create new drink |
| `/drinks/<id>` | PATCH | Manager | Update drink |
| `/drinks/<id>` | DELETE | Manager | Delete drink |

### Authentication

- **Auth0 Domain:** dev-huk2wemon6z8ehay.us.auth0.com
- **Algorithm:** RS256
- **Audience:** coffee-shop-api
- **SPA Client ID:** VZlYOX3rUjE5n46rPU5rSrRGVV8mLFyl

### Authorization (RBAC)

**Roles:**
- **Barista:** Can view drink details
  - `get:drinks`
  - `get:drinks-detail`

- **Manager:** Can manage all drinks
  - `get:drinks`
  - `get:drinks-detail`
  - `post:drinks`
  - `patch:drinks`
  - `delete:drinks`

---

## 🔧 Configuration

### Backend (.env)

```bash
AUTH0_DOMAIN=dev-huk2wemon6z8ehay.us.auth0.com
AUTH0_ALGORITHM=RS256
AUTH0_API_AUDIENCE=coffee-shop-api
FLASK_ENV=development
FLASK_DEBUG=True
```

### Frontend (environment.ts)

```typescript
auth0: {
  url: 'dev-huk2wemon6z8ehay',
  audience: 'coffee-shop-api',
  clientId: 'VZlYOX3rUjE5n46rPU5rSrRGVV8mLFyl',
  callbackURL: 'http://localhost:8100',
}
```

---

## 📚 Documentation

All detailed documentation is in `docs/`:

- **STATUS_PARA_SUBMISSAO.md** - Submission status
- **CRIAR_USUARIOS_AUTH0.md** - Creating users
- **PROBLEMA_APOS_ADICIONAR_DRINK.md** - Troubleshooting

---

## 🎯 Key Features Implemented

### ✅ Security
- JWT authentication with Auth0
- Role-Based Access Control (RBAC)
- Secure token verification
- Permission-based authorization

### ✅ API
- RESTful endpoints
- CRUD operations
- Error handling
- SQLite database

### ✅ Frontend
- Ionic/Angular
- Auth0 integration
- Role-based UI
- Responsive design

### ✅ Testing
- Unit tests
- Integration tests
- Pytest configuration
- Code coverage

---

## 📖 Technical Stack

**Backend:**
- Python 3.11+
- Flask 2.0.0
- SQLAlchemy 1.4.41
- python-jose (JWT)
- Ruff (linting)
- Pytest (testing)

**Frontend:**
- Ionic
- Angular
- TypeScript
- Auth0 SDK

**Database:**
- SQLite

**Authentication:**
- Auth0
- JWT (RS256)
- OAuth 2.0

---

## 🚀 Deployment Notes

### Environment Variables
- Keep `.env` files secure
- Never commit credentials
- Use environment variables in production

### Security
- Enable HTTPS in production
- Configure CORS properly
- Validate all inputs
- Use environment-specific configs

---

## 📝 License

This project is part of the Udacity Full Stack Nanodegree program.

---

## 🎉 Project Complete!

All requirements met:
- ✅ Authentication implemented
- ✅ Authorization (RBAC) implemented
- ✅ All endpoints working
- ✅ Tests passing
- ✅ Frontend functional
- ✅ Documentation complete
