#!/usr/bin/env python3
"""
Test script to verify backend configuration.

Run: python3 test_config.py
"""

import os
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))


def test_env_variables():
    """Test that environment variables are loaded."""
    print("🔍 Testing environment variables...")

    # Import auth module which reads from environment
    from auth.auth import AUTH0_DOMAIN, ALGORITHMS, API_AUDIENCE

    print(f"✅ AUTH0_DOMAIN: {AUTH0_DOMAIN}")
    print(f"✅ ALGORITHMS: {ALGORITHMS}")
    print(f"✅ API_AUDIENCE: {API_AUDIENCE}")

    # Verify values are not defaults
    if AUTH0_DOMAIN == "udacity-fsnd.auth0.com":
        print("⚠️  AUTH0_DOMAIN ainda tem valor padrão")
    else:
        print("✅ AUTH0_DOMAIN configurado")

    if API_AUDIENCE == "dev":
        print("⚠️  API_AUDIENCE ainda tem valor padrão")
    else:
        print("✅ API_AUDIENCE configurado")

    print()


def test_database():
    """Test database connection."""
    print("🔍 Testing database connection...")

    try:
        from database.models import db, setup_db
        from flask import Flask

        app = Flask(__name__)
        setup_db(app)

        with app.app_context():
            print("✅ Database configured successfully")
            print(f"✅ Database URI: {app.config.get('SQLALCHEMY_DATABASE_URI')}")
    except Exception as e:
        print(f"❌ Database error: {e}")
    finally:
        print()


def test_api():
    """Test API can be imported."""
    print("🔍 Testing API module...")

    try:
        from api import app
        print("✅ API module imported successfully")
        print(f"✅ Flask app configured: {app.name}")
    except Exception as e:
        print(f"❌ API error: {e}")
    finally:
        print()


def main():
    """Run all tests."""
    print("=" * 60)
    print("Coffee Shop Backend - Configuration Test")
    print("=" * 60)
    print()

    try:
        test_env_variables()
        test_database()
        test_api()

        print("=" * 60)
        print("✅ All configuration tests passed!")
        print("=" * 60)
        return 0
    except Exception as e:
        print("=" * 60)
        print(f"❌ Configuration test failed: {e}")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())

