"""
Coffee Shop API - Main Flask Application.

This module provides RESTful API endpoints for the Coffee Shop application.
It includes endpoints for managing drinks with role-based access control.

Endpoints:
    GET /drinks - Public endpoint to get all drinks (short form)
    GET /drinks-detail - Protected endpoint to get all drinks (long form)
    POST /drinks - Protected endpoint to create a new drink
    PATCH /drinks/<id> - Protected endpoint to update a drink
    DELETE /drinks/<id> - Protected endpoint to delete a drink

Roles:
    - Public: Can view drink menu
    - Barista: Can view drink details with full recipe
    - Manager: Can perform all operations (CRUD)
"""

import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

# Initialize database tables
# WARNING: Uncommenting the line below will drop all existing data!
# Uncomment on first run only to create the database
# db_drop_and_create_all()


# ROUTES

@app.route('/drinks', methods=['GET'])
def get_drinks():
    """
    GET /drinks - Retrieve all drinks (public endpoint).

    Returns short form representation of drinks without recipe details.

    Returns:
        JSON response with status code 200:
        {
            "success": True,
            "drinks": [drink1, drink2, ...]
        }

    Example:
        GET /drinks
        Response:
        {
            "success": True,
            "drinks": [
                {"id": 1, "title": "Water", "recipe": [{"color": "blue", "parts": 1}]}
            ]
        }
    """
    # TODO: Implement this endpoint
    # It should be a public endpoint
    # It should contain only the drink.short() data representation
    # Returns status code 200 and json {"success": True, "drinks": drinks}
    # or appropriate status code indicating reason for failure
    abort(501)  # Not Implemented


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_detail(payload):
    """
    GET /drinks-detail - Retrieve all drinks with full details (protected).

    Requires 'get:drinks-detail' permission (Barista and Manager roles).
    Returns long form representation of drinks with complete recipe information.

    Returns:
        JSON response with status code 200:
        {
            "success": True,
            "drinks": [drink1, drink2, ...]
        }

    Example:
        GET /drinks-detail
        Response:
        {
            "success": True,
            "drinks": [
                {"id": 1, "title": "Water", "recipe": [{"name": "water", "color": "blue", "parts": 1}]}
            ]
        }
    """
    # TODO: Implement this endpoint
    # It should require the 'get:drinks-detail' permission
    # It should contain the drink.long() data representation
    abort(501)  # Not Implemented


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def create_drink(payload):
    """
    POST /drinks - Create a new drink (protected).

    Requires 'post:drinks' permission (Manager role only).
    Creates a new drink in the database.

    Request Body:
        {
            "title": "string",
            "recipe": [{"name": "string", "color": "string", "parts": int}]
        }

    Returns:
        JSON response with status code 200:
        {
            "success": True,
            "drinks": [new_drink]
        }

    Example:
        POST /drinks
        Request: {"title": "Latte", "recipe": [{"name": "coffee", "color": "brown", "parts": 1}]}
        Response: {"success": True, "drinks": [{"id": 2, "title": "Latte", ...}]}
    """
    # TODO: Implement this endpoint
    # It should create a new row in the drinks table
    # It should require the 'post:drinks' permission
    # It should contain the drink.long() data representation
    abort(501)  # Not Implemented


@app.route('/drinks/<int:drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(payload, drink_id):
    """
    PATCH /drinks/<id> - Update an existing drink (protected).

    Requires 'patch:drinks' permission (Manager role only).
    Updates the drink with the specified ID.

    Args:
        drink_id: ID of the drink to update

    Request Body:
        {
            "title": "string" (optional),
            "recipe": [...] (optional)
        }

    Returns:
        JSON response with status code 200:
        {
            "success": True,
            "drinks": [updated_drink]
        }
        or 404 if drink not found

    Example:
        PATCH /drinks/1
        Request: {"title": "Updated Drink"}
        Response: {"success": True, "drinks": [updated_drink]}
    """
    # TODO: Implement this endpoint
    # It should update the corresponding row for <id>
    # It should respond with a 404 error if <id> is not found
    # It should require the 'patch:drinks' permission
    abort(501)  # Not Implemented


@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(payload, drink_id):
    """
    DELETE /drinks/<id> - Delete a drink (protected).

    Requires 'delete:drinks' permission (Manager role only).
    Deletes the drink with the specified ID.

    Args:
        drink_id: ID of the drink to delete

    Returns:
        JSON response with status code 200:
        {
            "success": True,
            "delete": id
        }
        or 404 if drink not found

    Example:
        DELETE /drinks/1
        Response: {"success": True, "delete": 1}
    """
    # TODO: Implement this endpoint
    # It should delete the corresponding row for <id>
    # It should respond with a 404 error if <id> is not found
    # It should require the 'delete:drinks' permission
    abort(501)  # Not Implemented


# Error Handling

@app.errorhandler(422)
def unprocessable(error):
    """
    Handle unprocessable entity errors (422).

    Args:
        error: The error object

    Returns:
        JSON response with status code 422:
        {
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }
    """
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def not_found(error):
    """
    Handle resource not found errors (404).

    Args:
        error: The error object

    Returns:
        JSON response with status code 404:
        {
            "success": False,
            "error": 404,
            "message": "resource not found"
        }
    """
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(AuthError)
def handle_auth_error(error):
    """
    Handle authentication and authorization errors.

    Args:
        error: The AuthError object with error details

    Returns:
        JSON response with appropriate status code:
        {
            "success": False,
            "error": status_code,
            "message": error_message
        }
    """
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error.get('description', 'Authentication failed')
    }), error.status_code


@app.errorhandler(400)
def bad_request(error):
    """
    Handle bad request errors (400).

    Args:
        error: The error object

    Returns:
        JSON response with status code 400:
        {
            "success": False,
            "error": 400,
            "message": "bad request"
        }
    """
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400


@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle internal server errors (500).

    Args:
        error: The error object

    Returns:
        JSON response with status code 500:
        {
            "success": False,
            "error": 500,
            "message": "internal server error"
        }
    """
    return jsonify({
        "success": False,
        "error": 500,
        "message": "internal server error"
    }), 500
