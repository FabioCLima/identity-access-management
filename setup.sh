#!/bin/bash

# Coffee Shop Full Stack - Setup Script
echo "=== Coffee Shop Full Stack Setup ==="
echo ""

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.cargo/env
fi

# Setup backend
echo "Setting up backend..."
cd backend
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
cd ..

# Setup frontend
echo "Setting up frontend..."
cd frontend
npm install
cd ..

echo ""
echo "=== Setup Complete ==="
echo ""
echo "To run the backend:"
echo "  cd backend"
echo "  source .venv/bin/activate"
echo "  cd src"
echo "  export FLASK_APP=api.py"
echo "  flask run --reload"
echo ""
echo "To run the frontend:"
echo "  cd frontend"
echo "  export NODE_OPTIONS=--openssl-legacy-provider"
echo "  ionic serve"
echo ""

