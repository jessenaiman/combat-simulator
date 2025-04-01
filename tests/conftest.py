# tests/conftest.py
import pytest
import sqlalchemy as sa

@pytest.fixture
def db_engine():
    engine = sa.create_engine("sqlite:///data/omega_project.db")
    yield engine
    engine.dispose()