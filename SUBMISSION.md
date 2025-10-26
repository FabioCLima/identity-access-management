# Coffee Shop Full Stack - Submission Guide

## Project Summary

This project is a full-stack drink menu application for a digitally enabled cafe. The application demonstrates identity and access management (IAM) skills with role-based authentication.

## Repository Setup

✅ **Git Repository Initialized**  
✅ **All project code committed to version control  
✅ **`.gitignore` properly configured to exclude:**
  - Virtual environment directories (`.venv/`, `venv/`, etc.)
  - Python cache files (`__pycache__/`, `*.pyc`)
  - Node.js dependencies (`node_modules/`)
  - Database files (`*.db`, `*.sqlite3`)
  - IDE and OS files
  - Log files and temporary files

## Project Structure

```
coffee-shop/
├── backend/                      # Flask backend API
│   ├── src/
│   │   ├── api.py               # Main Flask application
│   │   ├── auth/                # Authentication module
│   │   │   ├── auth.py         # Auth0 integration (TODOs to implement)
│   │   └── __init__.py
│   ├── database/
│   │   ├── models.py           # SQLAlchemy models
│   │   └── __init__.py
│   ├── pyproject.toml          # UV package configuration
│   ├── requirements.txt        # Python dependencies
│   ├── README.md               # Backend setup instructions
│   └── udacity-fsnd-udaspicelatte.postman_collection.json
├── frontend/                    # Ionic frontend
│   ├── src/
│   │   ├── app/                # Angular application
│   │   ├── environments/       # Environment configuration
│   │   └── services/           # Auth and API services
│   ├── package.json
│   ├── README.md               # Frontend setup instructions
│   └── ... (Ionic/Angular files)
├── .gitignore                   # Git ignore rules
├── README.md                    # Main project documentation
├── QUICKSTART.md                # Quick start guide
├── setup.sh                     # Automated setup script
├── create-submission-zip.sh     # Submission zip creation
└── SUBMISSION.md                # This file
```

## Creating Submission Zip

### Automated Method (Recommended)

From the `coffee-shop` directory, run:

```bash
./create-submission-zip.sh
```

This will create `coffee-shop-submission.zip` in the parent directory (`~/Workdir/udacity_projects/identity-access-management/`) with all project code properly excluded.

### What's Excluded

The submission zip automatically excludes:
- ✅ `.venv/` - Virtual environment directory
- ✅ `__pycache__/` - Python cache files
- ✅ `node_modules/` - Node.js dependencies
- ✅ `*.db` - SQLite database files
- ✅ `*.log` - Log files
- ✅ `.git/` - Git repository
- ✅ Other local development files

Only the **project source code** and **documentation** are included in the submission.

## Manual Verification

You can verify what will be included in the zip by checking the git repository:

```bash
cd coffee-shop
git log --oneline           # View commit history
git ls-files                # List all tracked files
git status                   # Check current status
```

## Git Repository

The project demonstrates proper Git usage:
- ✅ All source code is committed
- ✅ Virtual environments are excluded via `.gitignore`
- ✅ Unnecessary files are excluded
- ✅ Clean, readable commit history
- ✅ Proper project organization

### View Git History

```bash
cd coffee-shop
git log
```

### View Tracked Files

```bash
git ls-tree -r HEAD --name-only
```

## Project Features

### Backend (Flask + SQLAlchemy)
- RESTful API endpoints for drink management
- Auth0 JWT authentication
- Role-based permissions (Barista, Manager)
- SQLite database with Drink models

### Frontend (Ionic + Angular)
- Mobile-responsive drink menu interface
- Auth0 authentication integration
- Role-based UI controls
- Drink graphics visualization
- Full CRUD operations for managers

## Next Steps for Implementation

1. **Setup Auth0** - Follow instructions in `backend/README.md`
2. **Implement Authentication** - Complete TODOs in `backend/src/auth/auth.py`
3. **Implement API Endpoints** - Complete TODOs in `backend/src/api.py`
4. **Configure Frontend** - Update `frontend/src/environments/environment.ts`
5. **Test with Postman** - Use the provided collection

## Required Tasks

### Backend TODOs

Located in `backend/src/`:
1. `auth/auth.py`:
   - `get_token_auth_header()` - Extract JWT from header
   - `check_permissions()` - Verify permissions
   - `verify_decode_jwt()` - Validate JWT token
   - `@requires_auth()` - Decorator for protected routes

2. `api.py`:
   - `GET /drinks` - Public endpoint for drink list
   - `GET /drinks-detail` - Barista endpoint with full recipe
   - `POST /drinks` - Manager endpoint to create drinks
   - `PATCH /drinks/<id>` - Manager endpoint to update drinks
   - `DELETE /drinks/<id>` - Manager endpoint to delete drinks
   - Error handlers (404, AuthError, etc.)

### Frontend Configuration

Update `frontend/src/environments/environment.ts` with your Auth0:
- `auth0Domain`
- `auth0ClientId`
- `apiServerUrl`

## Testing

### Backend Testing

Import the Postman collection: `backend/udacity-fsnd-udaspicelatte.postman_collection.json`

### Frontend Testing

```bash
cd frontend
ionic serve
```

## Dependencies

### Backend
- Python 3.11+
- Flask 2.0.0
- SQLAlchemy 1.4.41
- python-jose[cryptography] 3.3.0
- Flask-CORS 3.0.8

### Frontend
- Node.js
- Ionic CLI
- Angular
- Auth0

## License

This project is part of the Udacity Full Stack Nanodegree program - Identity and Access Management specialization.

