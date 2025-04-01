# install_everything.bat (Windows)
@echo off
echo Installing Python and pip...
py -3 --version || (echo Install Python 3.11+ from python.org && exit /b 1)
py -3 -m ensurepip --upgrade
py -3 -m pip install --upgrade pip

echo Installing core dependencies...
py -3 -m pip install ^
  arcade==3.0.2 ^
  pydantic==2.8.2 ^
  SQLAlchemy==2.0.35 ^
  toml==0.10.2 ^
  -U
echo Core dependencies installed: Arcade, pydantic, SQLAlchemy, toml

echo Setting up SQLite database environment...
mkdir data 2>nul
echo Created data/ directory for SQLite database (omega_project.db)

echo Installing development dependencies...
py -3 -m pip install ^
  pytest==8.3.3 ^
  pytest-sugar==1.0.0 ^
  hypothesis==6.115.0 ^
  coverage==7.6.4 ^
  ruff==0.6.8 ^
  mypy==1.11.2 ^
  pre-commit==3.8.0 ^
  sphinx==8.0.2 ^
  sphinxcontrib-mermaid==0.9.2 ^
  -U

echo Generating requirements.txt...
py -3 -m pip freeze > requirements.txt
echo Generated requirements.txt with exact versions

echo Installation complete. Run verify_install.bat to confirm setup.
echo If this script fails, refer to INSTALL.md or individual scripts (install_python.bat, install_core.bat, etc.) for detailed steps.