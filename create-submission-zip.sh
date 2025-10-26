#!/bin/bash

# Coffee Shop Full Stack - Create Submission Zip
# This script creates a zip file excluding git files and files listed in .gitignore

echo "Creating submission zip for Coffee Shop Full Stack project..."
echo ""

PROJECT_NAME="coffee-shop"
ZIP_NAME="${PROJECT_NAME}-submission.zip"

# Go to the parent directory
cd ..

# Create a zip excluding git files and .gitignore patterns
zip -r "$ZIP_NAME" "$PROJECT_NAME" \
    -x "$PROJECT_NAME/.git/*" \
    -x "$PROJECT_NAME/.venv/*" \
    -x "$PROJECT_NAME/__pycache__/*" \
    -x "$PROJECT_NAME/**/__pycache__/*" \
    -x "$PROJECT_NAME/node_modules/*" \
    -x "$PROJECT_NAME/.env*" \
    -x "$PROJECT_NAME/*.db" \
    -x "$PROJECT_NAME/**/*.pyc" \
    -x "$PROJECT_NAME/**/*.pyo" \
    -x "$PROJECT_NAME/.DS_Store" \
    -x "$PROJECT_NAME/**/.DS_Store" \
    -x "$PROJECT_NAME/*.log"

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ Submission zip created successfully: $ZIP_NAME"
    echo "✓ File size: $(du -h "$ZIP_NAME" | cut -f1)"
    echo ""
    echo "The zip file contains all project code excluding:"
    echo "  - .git directory"
    echo "  - Virtual environment (.venv)"
    echo "  - Python cache files (__pycache__)"
    echo "  - node_modules"
    echo "  - Database files (.db)"
    echo "  - Log files (.log)"
    echo "  - Other local files defined in .gitignore"
    echo ""
else
    echo "✗ Error creating zip file"
    exit 1
fi

