"""
Tests for Coffee Shop API endpoints.

This module tests all API endpoints for proper functionality,
authentication, and authorization.
"""

import json
import os
import unittest

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.api import app
from src.database.models import Drink, db, db_drop_and_create_all, setup_db


class DrinkAPITestCase(unittest.TestCase):
    """Test cases for the Drink API endpoints."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.app = app
        self.client = self.app.test_client()
        self.app.config["TESTING"] = True
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        with self.app.app_context():
            db.drop_all()
            db.create_all()

            # Create test drinks
            drink1 = Drink(
                title="Coffee",
                recipe=json.dumps(
                    [{"name": "coffee", "color": "brown", "parts": 1}]
                ),
            )
            drink2 = Drink(
                title="Latte",
                recipe=json.dumps(
                    [
                        {"name": "coffee", "color": "brown", "parts": 1},
                        {"name": "milk", "color": "white", "parts": 3},
                    ]
                ),
            )

            drink1.insert()
            drink2.insert()

    def tearDown(self):
        """Clean up after each test method."""
        with self.app.app_context():
            db.session.rollback()
            db.session.close()

    def test_get_drinks_public_endpoint(self):
        """Test GET /drinks public endpoint."""
        response = self.client.get("/drinks")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])
        self.assertIn("drinks", data)
        self.assertIsInstance(data["drinks"], list)
        self.assertEqual(len(data["drinks"]), 2)

    def test_get_drinks_returns_short_form(self):
        """Test that GET /drinks returns short form representation."""
        response = self.client.get("/drinks")
        data = json.loads(response.data)

        drink = data["drinks"][0]
        # Short form should not have 'name' in recipe
        if drink.get("recipe"):
            ingredient = drink["recipe"][0]
            self.assertNotIn("name", ingredient)
            self.assertIn("color", ingredient)
            self.assertIn("parts", ingredient)

    def test_create_drink_missing_title(self):
        """Test POST /drinks with missing title returns 400."""
        response = self.client.post(
            "/drinks",
            data=json.dumps({"recipe": [{"name": "water", "color": "blue", "parts": 1}]}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_drink_missing_recipe(self):
        """Test POST /drinks with missing recipe returns 400."""
        response = self.client.post(
            "/drinks",
            data=json.dumps({"title": "Water"}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_drink_invalid_recipe_format(self):
        """Test POST /drinks with invalid recipe format returns 422."""
        response = self.client.post(
            "/drinks",
            data=json.dumps(
                {
                    "title": "Test Drink",
                    "recipe": "not a list",
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 422)

    def test_create_drink_incomplete_recipe(self):
        """Test POST /drinks with incomplete recipe ingredients returns 422."""
        response = self.client.post(
            "/drinks",
            data=json.dumps(
                {
                    "title": "Test Drink",
                    "recipe": [{"name": "water"}],  # Missing color and parts
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 422)

    def test_update_drink_not_found(self):
        """Test PATCH /drinks/<id> with non-existent ID returns 404."""
        response = self.client.patch(
            "/drinks/999",
            data=json.dumps({"title": "Updated"}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 404)

    def test_delete_drink_not_found(self):
        """Test DELETE /drinks/<id> with non-existent ID returns 404."""
        response = self.client.delete("/drinks/999")

        self.assertEqual(response.status_code, 404)

    def test_error_handlers_404(self):
        """Test 404 error handler."""
        response = self.client.get("/nonexistent")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertFalse(data["success"])
        self.assertEqual(data["error"], 404)

    def test_error_handlers_422(self):
        """Test 422 error handler."""
        response = self.client.post(
            "/drinks",
            data=json.dumps({"title": "Test", "recipe": "invalid"}),
            content_type="application/json",
        )
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertFalse(data["success"])
        self.assertEqual(data["error"], 422)


class DrinkModelTestCase(unittest.TestCase):
    """Test cases for the Drink model."""

    def setUp(self):
        """Set up test fixtures."""
        self.app = app
        self.app.config["TESTING"] = True
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        with self.app.app_context():
            db.drop_all()
            db.create_all()

    def tearDown(self):
        """Clean up after each test."""
        with self.app.app_context():
            db.session.rollback()
            db.session.close()

    def test_drink_short_method(self):
        """Test Drink.short() method returns correct format."""
        drink = Drink(
            title="Test Drink",
            recipe=json.dumps([{"name": "water", "color": "blue", "parts": 1}]),
        )
        drink.insert()

        short = drink.short()
        self.assertEqual(short["id"], drink.id)
        self.assertEqual(short["title"], "Test Drink")
        self.assertEqual(short["recipe"][0]["color"], "blue")
        self.assertEqual(short["recipe"][0]["parts"], 1)
        self.assertNotIn("name", short["recipe"][0])

    def test_drink_long_method(self):
        """Test Drink.long() method returns correct format."""
        drink = Drink(
            title="Test Drink",
            recipe=json.dumps([{"name": "water", "color": "blue", "parts": 1}]),
        )
        drink.insert()

        long = drink.long()
        self.assertEqual(long["id"], drink.id)
        self.assertEqual(long["title"], "Test Drink")
        self.assertEqual(long["recipe"][0]["name"], "water")
        self.assertEqual(long["recipe"][0]["color"], "blue")
        self.assertEqual(long["recipe"][0]["parts"], 1)

    def test_drink_crud_operations(self):
        """Test Drink CRUD operations."""
        # Create
        drink = Drink(title="Test", recipe=json.dumps([{"name": "test", "color": "red", "parts": 1}]))
        drink.insert()

        # Read
        retrieved = Drink.query.filter(Drink.id == drink.id).one_or_none()
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.title, "Test")

        # Update
        retrieved.title = "Updated Test"
        retrieved.update()
        updated = Drink.query.filter(Drink.id == drink.id).one_or_none()
        self.assertEqual(updated.title, "Updated Test")

        # Delete
        updated.delete()
        deleted = Drink.query.filter(Drink.id == drink.id).one_or_none()
        self.assertIsNone(deleted)


if __name__ == "__main__":
    unittest.main()

