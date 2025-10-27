"""
Pytest configuration and fixtures.

This module provides shared fixtures for testing.
"""

import json
import os
import pytest

from src.api import app
from src.database.models import Drink, db


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    with app.app_context():
        db.drop_all()
        db.create_all()

        # Create test drinks
        drink1 = Drink(
            title="Coffee",
            recipe=json.dumps([{"name": "coffee", "color": "brown", "parts": 1}]),
        )
        drink2 = Drink(
            title="Latte",
            recipe=json.dumps([
                {"name": "coffee", "color": "brown", "parts": 1},
                {"name": "milk", "color": "white", "parts": 3},
            ]),
        )

        drink1.insert()
        drink2.insert()

        yield app.test_client()

        db.session.rollback()
        db.session.close()


@pytest.fixture
def sample_drink_data():
    """Sample drink data for testing."""
    return {
        "title": "Test Drink",
        "recipe": [
            {"name": "water", "color": "blue", "parts": 1},
            {"name": "sugar", "color": "white", "parts": 1},
        ],
    }

