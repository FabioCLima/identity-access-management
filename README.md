# Coffee Shop Full Stack

## Full Stack Nano - IAM Final Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.

You have been called on to demonstrate your newly learned skills to create a full stack drink menu application. The application must:

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.

## Project Structure

```
coffee-shop/
├── backend/          # Flask backend API
│   ├── src/          # Application source code
│   ├── requirements.txt
│   └── README.md
├── frontend/         # Ionic frontend application
│   ├── src/          # Application source code
│   └── README.md
├── docs/             # Comprehensive documentation
│   ├── backend/      # Backend-specific docs
│   ├── frontend/      # Frontend-specific docs
│   └── *.md          # Project documentation
└── README.md         # This file
```

## 📚 Documentation

All documentation is located in the `docs/` directory:

### Quick Start
- **[EXECUTION_ROADMAP.md](docs/EXECUTION_ROADMAP.md)** - Step-by-step execution guide
- **[QUICKSTART.md](docs/QUICKSTART.md)** - Quick setup instructions

### Project Overview
- **[PROJECT_SUMMARY.md](docs/PROJECT_SUMMARY.md)** - Complete project overview
- **[PROJECT_REQUIREMENTS.md](docs/PROJECT_REQUIREMENTS.md)** - Requirements checklist

### Backend Documentation
- **[AUTH0_SETUP.md](docs/backend/AUTH0_SETUP.md)** - Auth0 configuration guide
- **[TESTING_GUIDE.md](docs/backend/TESTING_GUIDE.md)** - Testing instructions
- **[POSTMAN_SETUP_SUMMARY.md](docs/backend/POSTMAN_SETUP_SUMMARY.md)** - Postman configuration
- **[AUTH0_MFA_SETUP.md](docs/backend/AUTH0_MFA_SETUP.md)** - Multi-factor auth setup
- **[RBAC_ENHANCEMENT.md](docs/backend/RBAC_ENHANCEMENT.md)** - Advanced RBAC guide

### Frontend Documentation
- **[UI_ENHANCEMENTS.md](docs/frontend/UI_ENHANCEMENTS.md)** - UI enhancement guide

### Development & Deployment
- **[API_IMPLEMENTATION.md](docs/API_IMPLEMENTATION.md)** - API documentation
- **[BEST_PRACTICES.md](docs/BEST_PRACTICES.md)** - Coding best practices
- **[DEPLOYMENT_GUIDE.md](docs/DEPLOYMENT_GUIDE.md)** - Cloud deployment guide
- **[ENHANCEMENT_SUGGESTIONS.md](docs/ENHANCEMENT_SUGGESTIONS.md)** - Future enhancements
- **[SUBMISSION.md](docs/SUBMISSION.md)** - Submission guide

## Getting Started

### Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) - Python package manager
- Node.js and npm
- Ionic CLI

### Backend Setup

The `./backend` directory contains a partially completed Flask server with a pre-written SQLAlchemy module to simplify your data needs. You will need to complete the required endpoints, configure, and integrate Auth0 for authentication.

#### Install Dependencies with uv

From the `backend` directory:

```bash
cd backend
uv pip install -r requirements.txt
```

Or using uv's built-in environment:

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

#### Running the Backend

From the `backend` directory:

```bash
export FLASK_APP=src/api.py
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

[View the README.md within ./backend for more details.](./backend/README.md)

### Frontend Setup

The `./frontend` directory contains a complete Ionic frontend to consume the data from the Flask server. You will only need to update the environment variables found within (./frontend/src/environment/environment.ts) to reflect the Auth0 configuration details set up for the backend app.

#### Installing Dependencies

```bash
cd frontend
npm install
```

#### Running the Frontend

```bash
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve
```

[View the README.md within ./frontend for more details.](./frontend/README.md)

## Tasks

There are `@TODO` comments throughout the project. We recommend tackling the sections in order. Start by reading the READMEs in:

1. [`./backend/README.md`](./backend/README.md)
2. [`./frontend/README.md`](./frontend/README.md)

## About the Stack

### Backend

The `./backend` directory contains a partially completed Flask server with:
- Flask for web framework
- SQLAlchemy for database ORM
- python-jose for JWT handling
- Flask-CORS for cross-origin requests

### Frontend

The `./frontend` directory contains a complete Ionic frontend with:
- Angular framework
- Ionic UI components
- Auth0 integration for authentication
- Service-based architecture

## Development Workflow

1. Set up Auth0 account and configure permissions
2. Complete backend authentication implementation
3. Implement all API endpoints
4. Configure frontend Auth0 environment variables
5. Test the complete stack

## Git Repository

This project is initialized as a git repository and demonstrates the ability to share code on Git.

### Creating a Submission Zip

To create a clean submission zip file that excludes virtual environments, node_modules, and other local files:

```bash
./create-submission-zip.sh
```

This will create `coffee-shop-submission.zip` in the parent directory with all project code while excluding:
- .venv/ virtual environment directory
- __pycache__/ Python cache files
- node_modules/ Node.js dependencies
- *.db database files
- *.log log files
- .git/ git directory

All files are already properly configured in `.gitignore`.

## License

This project is part of the Udacity Full Stack Nanodegree program.

