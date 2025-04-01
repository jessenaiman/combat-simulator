# tests/test_core.py
import arcade
import sqlalchemy as sa
import pytest

def test_arcade_version():
    """Verify Arcade library version."""
    assert arcade.__version__ == "3.0.2", f"Expected Arcade 3.0.2, got {arcade.__version__}"

def test_sqlalchemy_engine(db_engine):
    """Verify SQLite engine creation."""
    with db_engine.connect() as conn:
        result = conn.execute(sa.text("SELECT sqlite_version();")).scalar()
    assert result.startswith("3."), "SQLite version should be 3.x"