# Coffee Shop - Quick Start Guide

## Project Organization

The project has been organized in the following structure:

```
identity-access-management/
└── coffee-shop/
    ├── backend/          # Flask backend API
    ├── frontend/         # Ionic frontend
    ├── setup.sh         # Automated setup script
    ├── README.md         # Main project documentation
    └── .gitignore        # Git ignore rules
```

## Quick Setup

### Option 1: Automated Setup (Recommended)

Run the setup script:

```bash
cd ~/Workdir/udacity_projects/identity-access-management/coffee-shop
./setup.sh
```

### Option 2: Manual Setup

#### Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment with uv
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt

# Or using traditional pip
pip install -r requirements.txt
```

#### Frontend Setup

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install
```

## Running the Applications

### Start Backend Server

```bash
cd backend/src
export FLASK_APP=api.py
flask run --reload
```

The backend will run on `http://localhost:5000`

### Start Frontend Application

Open a new terminal:

```bash
cd frontend
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve
```

The frontend will run on `http://localhost:8100`

## Next Steps

### 1. Setup Auth0

Follow the instructions in [`backend/README.md`](./backend/README.md) to:
- Create an Auth0 account
- Configure API and permissions
- Create roles (Barista and Manager)

### 2. Implement Backend

Complete the TODO items in:
- `backend/src/auth/auth.py` - Authentication implementation
- `backend/src/api.py` - API endpoints

### 3. Configure Frontend

Update the environment variables in:
- `frontend/src/environments/environment.ts`

### 4. Test with Postman

Import `backend/udacity-fsnd-udaspicelatte.postman_collection.json` into Postman to test your API.

## Development Workflow

1. **Auth0 Configuration**: Set up Auth0 with proper roles and permissions
2. **Backend Development**: Complete authentication and API endpoints
3. **Frontend Configuration**: Update environment variables
4. **Integration Testing**: Test the full stack

## Useful Commands

### Backend
```bash
# Activate virtual environment
source .venv/bin/activate

# Run development server
flask run --reload

# Deactivate virtual environment
deactivate
```

### Frontend
```bash
# Run development server
ionic serve

# Build for production
ionic build
```

## Troubleshooting

### Backend Issues

- **Module not found**: Make sure virtual environment is activated
- **Port already in use**: Kill the process using port 5000: `lsof -ti:5000 | xargs kill`

### Frontend Issues

- **Node version**: Use Node 16.x or lower, or set `NODE_OPTIONS=--openssl-legacy-provider`
- **npm install errors**: Try deleting `node_modules` and `package-lock.json`, then run `npm install` again

## Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Ionic Documentation](https://ionicframework.com/docs)
- [Auth0 Documentation](https://auth0.com/docs)
- [SQLAlchemy Documentation](https://www.sqlalchemy.org/)

