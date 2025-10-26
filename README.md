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
├── frontend/         # Ionic frontend application
└── README.md         # This file
```

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

