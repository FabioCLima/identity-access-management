"""
Database models for Coffee Shop API.

This module provides database configuration and models using SQLAlchemy.
It includes the Drink model and database initialization functions.
"""

import json
import os

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

# Database configuration
DATABASE_FILENAME = "database.db"
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = f"sqlite:///{os.path.join(PROJECT_DIR, DATABASE_FILENAME)}"

db = SQLAlchemy()


def setup_db(app):
    """
    Configure and initialize database for Flask application.

    Args:
        app: Flask application instance

    This function binds the Flask application to the SQLAlchemy service
    and sets up the database connection.
    """
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_PATH
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


def db_drop_and_create_all():
    """
    Drop all database tables and start fresh.

    WARNING: This will delete all existing data!

    Can be used to initialize a clean database.
    Adds one demo row for testing.
    Note: You can change the DATABASE_FILENAME variable to have multiple
    database versions.
    """
    db.drop_all()
    db.create_all()
    # Add one demo row for testing
    drink = Drink(title="water", recipe='[{"name": "water", "color": "blue", "parts": 1}]')
    drink.insert()


class Drink(db.Model):
    """
    Drink model representing a coffee shop beverage.

    Attributes:
        id: Auto-incrementing unique primary key
        title: String title (max 80 chars, must be unique)
        recipe: JSON string containing ingredient list
                Format: [{'color': str, 'name': str, 'parts': int}]
    """

    # Autoincrementing, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    # String title
    title = Column(String(80), unique=True)
    # Recipe ingredients stored as JSON string
    # Format: [{'color': string, 'name': string, 'parts': number}]
    recipe = Column(String(180), nullable=False)

    def short(self):
        """
        Return short form representation of the Drink model.

        Returns:
            dict: Contains id, title, and simplified recipe
                  with color and parts only

        Example:
            {'id': 1, 'title': 'Coffee', 'recipe': [{'color': 'brown', 'parts': 1}]}
        """
        print(json.loads(self.recipe))
        short_recipe = [{"color": r["color"], "parts": r["parts"]} for r in json.loads(self.recipe)]
        return {"id": self.id, "title": self.title, "recipe": short_recipe}

    def long(self):
        """
        Return long form representation of the Drink model.

        Returns:
            dict: Contains id, title, and full recipe
                  with color, name, and parts

        Example:
            {'id': 1, 'title': 'Coffee', 'recipe': [{'color': 'brown', 'name': 'coffee', 'parts': 1}]}
        """
        return {"id": self.id, "title": self.title, "recipe": json.loads(self.recipe)}

    def insert(self):
        """
        Insert a new drink into the database.

        The drink must have a unique title.
        The drink must have a unique id or null id.

        Example:
            drink = Drink(title='Coffee', recipe='[{"name": "coffee", "color": "brown", "parts": 1}]')
            drink.insert()
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        Delete this drink from the database.

        The drink must exist in the database.

        Example:
            drink = Drink.query.filter(Drink.id == drink_id).one_or_none()
            drink.delete()
        """
        db.session.delete(self)
        db.session.commit()

    def update(self):
        """
        Update this drink in the database.

        The drink must exist in the database.

        Example:
            drink = Drink.query.filter(Drink.id == drink_id).one_or_none()
            drink.title = 'Black Coffee'
            drink.recipe = 'updated_recipe'
            drink.update()
        """
        db.session.commit()

    def __repr__(self):
        """Return string representation of the drink."""
        return json.dumps(self.short())
