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

import json

from flask import Flask, abort, jsonify, request
from flask_cors import CORS
from sqlalchemy import exc

from .auth.auth import AuthError, requires_auth
from .database.models import Drink, setup_db

app = Flask(__name__)
setup_db(app)
CORS(app)

# Initialize database tables
# WARNING: Uncommenting the line below will drop all existing data!
# Uncomment on first run only to create the database
# db_drop_and_create_all()


# ROUTES


@app.route("/drinks", methods=["GET"])
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
    try:
        # Query all drinks from database
        drinks = Drink.query.all()

        # Return short form representation
        drinks_list = [drink.short() for drink in drinks]

        return jsonify({"success": True, "drinks": drinks_list}), 200

    except Exception as e:
        print(f"Error getting drinks: {str(e)}")
        abort(500)


@app.route("/drinks-detail", methods=["GET"])
@requires_auth("get:drinks-detail")
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
    try:
        # Query all drinks from database
        drinks = Drink.query.all()

        # Return long form representation
        drinks_list = [drink.long() for drink in drinks]

        return jsonify({"success": True, "drinks": drinks_list}), 200

    except Exception as e:
        print(f"Error getting drinks detail: {str(e)}")
        abort(500)


@app.route("/drinks", methods=["POST"])
@requires_auth("post:drinks")
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
    try:
        # Get request body
        body = request.get_json()

        # Validate required fields
        if not body:
            abort(400)

        title = body.get("title", None)
        recipe = body.get("recipe", None)

        # Validate that both fields are provided
        if not title or not recipe:
            abort(400)

        # Validate recipe is a list
        if not isinstance(recipe, list):
            abort(422)

        # Validate each ingredient in recipe
        for ingredient in recipe:
            if not all(key in ingredient for key in ["name", "color", "parts"]):
                abort(422)

        # Create new drink
        new_drink = Drink(title=title, recipe=json.dumps(recipe))

        # Insert drink into database
        new_drink.insert()

        # Return the created drink in long form
        return jsonify({"success": True, "drinks": [new_drink.long()]}), 200

    except exc.IntegrityError:
        # Handle duplicate title
        abort(422)
    except Exception as e:
        print(f"Error creating drink: {str(e)}")
        abort(422)


@app.route("/drinks/<int:drink_id>", methods=["PATCH"])
@requires_auth("patch:drinks")
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
    try:
        # Get the drink by ID
        drink = Drink.query.filter(Drink.id == drink_id).one_or_none()

        # Return 404 if drink not found
        if drink is None:
            abort(404)

        # Get request body
        body = request.get_json()

        # Validate request body
        if not body:
            abort(400)

        # Update title if provided
        if "title" in body:
            drink.title = body.get("title")

        # Update recipe if provided
        if "recipe" in body:
            recipe = body.get("recipe")

            # Validate recipe is a list
            if not isinstance(recipe, list):
                abort(422)

            # Validate each ingredient in recipe
            for ingredient in recipe:
                if not all(key in ingredient for key in ["name", "color", "parts"]):
                    abort(422)

            drink.recipe = json.dumps(recipe)

        # Update the drink in database
        drink.update()

        # Return the updated drink in long form
        return jsonify({"success": True, "drinks": [drink.long()]}), 200

    except exc.IntegrityError:
        # Handle duplicate title
        abort(422)
    except Exception as e:
        print(f"Error updating drink: {str(e)}")
        abort(422)


@app.route("/drinks/<int:drink_id>", methods=["DELETE"])
@requires_auth("delete:drinks")
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
    try:
        # Get the drink by ID
        drink = Drink.query.filter(Drink.id == drink_id).one_or_none()

        # Return 404 if drink not found
        if drink is None:
            abort(404)

        # Delete the drink from database
        drink.delete()

        # Return success response
        return jsonify({"success": True, "delete": drink_id}), 200

    except Exception as e:
        print(f"Error deleting drink: {str(e)}")
        abort(500)


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
    return jsonify({"success": False, "error": 422, "message": "unprocessable"}), 422


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
    return jsonify({"success": False, "error": 404, "message": "resource not found"}), 404


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
    return jsonify(
        {
            "success": False,
            "error": error.status_code,
            "message": error.error.get("description", "Authentication failed"),
        }
    ), error.status_code


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
    return jsonify({"success": False, "error": 400, "message": "bad request"}), 400


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
    return jsonify({"success": False, "error": 500, "message": "internal server error"}), 500
