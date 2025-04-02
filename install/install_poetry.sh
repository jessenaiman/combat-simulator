#!/bin/bash
set -e  # Exit on error

echo "Verifying Python 3.11+ is installed..."
if ! command -v python3 &> /dev/null || ! python3 --version | grep -q "3.1[1-9]"; then
    echo "Python 3.11+ is required. Please install it from python.org and ensure it is available as 'python3'."
    exit 1
fi
python3 --version

echo "Ensuring pip is installed and up-to-date..."
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip

echo "Installing Poetry..."
python3 -m pip install "poetry>=1.8.3" --upgrade
python3 -m poetry --version

echo "Setting up project directory structure..."
mkdir -p data src/omega_project tests
cd src/omega_project
for dir in audio combat commands data entities event game items narrative progression scenes shared simulation systems utils world; do
    mkdir -p "$dir"
    echo '"""Package for '"$dir"' functionality."""' > "$dir/__init__.py"
done
cd ../../tests
for dir in combat data; do
    mkdir -p "$dir"
    echo '"""Tests for '"$dir"' functionality."""' > "$dir/__init__.py"
done
cd ..

echo "Initializing Poetry project..."
python3 -m poetry init --name "omega_project" --author "Your Name" --python "^3.11" --no-interaction

echo "Adding core dependencies with minimum versions..."
python3 -m poetry add "arcade>=3.0.2" "pydantic>=2.8.2" "SQLAlchemy>=2.0.35"

echo "Adding development dependencies with minimum versions..."
python3 -m poetry add --group dev "pytest>=8.3.3" "pytest-sugar>=1.0.0" "hypothesis>=6.115.0" "coverage>=7.6.4" "ruff>=0.6.8" "mypy>=1.11.2" "pre-commit>=3.8.0" "sphinx>=8.0.2" "sphinxcontrib-mermaid>=0.9.2" "pytest-cov>=5.0.0"

echo "Installing all dependencies..."
python3 -m poetry install

echo "Creating data directory for SQLite database..."
mkdir -p data
echo "Created data/ directory for SQLite database (omega_project.db)"

echo "Installation complete. Verify setup with the following commands:"
echo "  - Check Arcade: poetry run python -c \"import arcade; print(arcade.__version__)\""
echo "  - Check SQLite: poetry run python -c \"import sqlalchemy as sa; e = sa.create_engine('sqlite:///data/omega_project.db'); c = e.connect(); print(c.execute(sa.text('SELECT sqlite_version();')).