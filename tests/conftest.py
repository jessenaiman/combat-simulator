"""Configuration for pytest, providing fixtures for tests."""
import os
from typing import Iterator

import pytest
import sqlalchemy as sa


@pytest.fixture
def db_engine() -> Iterator[sa.engine.Engine]:
    """Fixture to provide a SQLite database engine for tests."""
    os.makedirs("data", exist_ok=True)
    engine = sa.create_engine("sqlite:///data/omega_project.db")
    yield engine
    engine.dispose()
