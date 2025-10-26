#!/bin/bash

# Coffee Shop Backend - Start Server Script

echo "Starting Coffee Shop Backend Server..."
echo ""

# Get script directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    uv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Install/update dependencies
echo "Installing dependencies..."
uv pip install -r requirements.txt

# Set Flask environment
export FLASK_APP=src.api
export FLASK_ENV=development
export FLASK_DEBUG=1

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cat > .env << 'EOF'
# Auth0 Configuration
# Get these values from https://manage.auth0.com
AUTH0_DOMAIN=udacity-fsnd.auth0.com
AUTH0_ALGORITHM=RS256
AUTH0_API_AUDIENCE=dev

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
EOF
    echo "✓ Created .env file - Update with your Auth0 credentials"
fi

# Start Flask server
echo ""
echo "Starting Flask server on http://localhost:5000"
echo "Press Ctrl+C to stop"
echo ""
flask run --host=0.0.0.0 --reload

