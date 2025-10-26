# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.11+

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Using uv (Recommended)

This project uses [uv](https://github.com/astral-sh/uv) for fast Python package management.

Install uv if you haven't already:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or on Windows:
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### Installing Dependencies with uv

Create a virtual environment and install dependencies:

```bash
cd backend
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

#### Environment Variables Configuration

Create a `.env` file in the `backend` directory to store sensitive configuration:

```bash
cd backend
cat > .env << EOF
# Auth0 Configuration
# Get these values from https://manage.auth0.com
AUTH0_DOMAIN=udacity-fsnd.auth0.com
AUTH0_ALGORITHM=RS256
AUTH0_API_AUDIENCE=dev

# Flask Configuration (Optional)
FLASK_ENV=development
FLASK_DEBUG=True
EOF
```

**Important:** The `.env` file is already included in `.gitignore` to protect your secrets. Never commit actual credentials to version control.

#### Alternative: Using PIP

If you prefer using pip, you can still use traditional pip installation:

```bash
pip install -r requirements.txt
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./backend` directory first ensure you are working using your created virtual environment.

Activate your virtual environment (if not already activated):

```bash
cd backend
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

Each time you open a new terminal session, run:

```bash
cd backend/src
export FLASK_APP=api.py
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
   - in API Settings:
     - Enable RBAC
     - Enable Add Permissions in the Access Token
5. Create new API permissions:
   - `get:drinks`
   - `get:drinks-detail`
   - `post:drinks`
   - `patch:drinks`
   - `delete:drinks`
6. Create new roles for:
   - Barista
     - can `get:drinks-detail`
     - can `get:drinks`
   - Manager
     - can perform all actions
7. Test your endpoints with [Postman](https://getpostman.com).
   - Register 2 users - assign the Barista role to one and Manager role to the other.
   - Sign into each account and make note of the JWT.
   - Import the postman collection `./udacity-fsnd-udaspicelatte.postman_collection.json`
   - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
   - Run the collection and correct any errors.
   - Export the collection overwriting the one we've included so that we have your proper JWTs during review!

### Implement The Server

There are `@TODO` comments throughout the `./backend/src`. We recommend tackling the files in order and from top to bottom:

1. `./src/auth/auth.py`
2. `./src/api.py`
