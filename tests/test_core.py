"""Core tests for the combat simulator project."""
import arcade
import sqlalchemy as sa


def test_arcade_version() -> None:
    """Verify Arcade library version."""
    assert arcade.__version__ == "3.0.2", f"Expected Arcade 3.0.2, got {arcade.__version__}"

def test_sqlalchemy_engine(db_engine: sa.engine.Engine) -> None:
    """Verify SQLite engine creation."""
    with db_engine.connect() as conn:
        result = conn.execute(sa.text("SELECT sqlite_version();")).scalar()
        assert result is not None, "SQLite version query returned None"
        assert result.startswith("3."), "SQLite version should be 3.x"
