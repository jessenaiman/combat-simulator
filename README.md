# Omega Project

A Python-based game project setup, designed for developers to build upon a stable foundation. This repository provides a streamlined installation process, testing framework, and coding standards for consistent development. It uses Arcade for rendering, pydantic for configuration, and SQLAlchemy with SQLite for save files, with modern tools for testing, linting, and documentation.

## Installation for Developers

### Prerequisites
- **System**: Windows, Linux, or Intel Mac (ARM-based systems may have issues; see Arcade requirements: https://api.arcade.academy/en/stable/install.html).
- **Python**: 3.11+ (download from python.org; on Windows, ensure "Add Python to PATH" is checked during install).
- **Graphics**: OpenGL 3.3+ support (most systems meet this; check Arcade docs if issues arise).

### Setup Steps

#### 1. Clone the Repository
Clone the project and navigate to its directory:
```bash
git clone https://github.com/yourusername/omega_project.git
cd omega_project
```

#### 2. Run Installation Scripts
The installation scripts are located in the `install/` folder and are locked for consistency across development environments. Do not modify these scripts in pull requests (see [Rules](#rules) below). If local adjustments are needed due to system-specific issues, make them locally without committing changes.

- **Linux/MacOS**:
  ```bash
  chmod +x install/*.sh
  ./install/install_python.sh
  ./install/install_core.sh
  ./install/install_database.sh
  ./install/install_dev.sh
  ./install/generate_requirements.sh
  ```
- **Windows**:
  ```cmd
  install\install_python.bat
  install\install_core.bat
  install\install_database.bat
  install\install_dev.bat
  install\generate_requirements.bat
  ```

#### 3. Verify Installation
Run the verification script to confirm Arcade and SQLite are functional:
- **Linux/MacOS**:
  ```bash
  ./install/verify_install.sh
  ```
- **Windows**:
  ```cmd
  install\verify_install.bat
  ```
- **Expected Output**:
  - Arcade: Prints `3.0.2`, opens a 600x600 white window (close manually).
  - SQLite: Prints a version (e.g., `3.45.2`).

#### 4. Run Sample Tests
Execute the provided tests to ensure the environment is set up correctly:
- **Linux/MacOS**:
  ```bash
  pytest tests/ -v
  ```
- **Windows**:
  ```cmd
  py -3 -m pytest tests/ -v
  ```
- **Expected Output**:
  ```
  tests/test_core.py::test_arcade_version PASSED
  tests/test_core.py::test_sqlalchemy_engine PASSED
  ```

## Project Structure and Conventions

### File Structure
```
omega_project/
├── install/               # Installation scripts (do not modify)
│   ├── install_*.sh       # Linux/MacOS scripts
│   ├── install_*.bat      # Windows scripts
│   ├── verify_install.sh  # Verification script (Linux/MacOS)
│   ├── verify_install.bat # Verification script (Windows)
├── src/                   # Source code
│   ├── omega_project/
│   │   ├── __init__.py
│   │   └── main.py
├── data/                  # SQLite database storage
│   └── omega_project.db
├── tests/                 # Test suite
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_core.py
├── docs/                  # Documentation
│   ├── conf.py
│   ├── index.rst
│   ├── requirements.txt
│   └── _static/
├── .github/               # CI configuration
│   ├── workflows/
│   │   └── ci.yml
├── .vscode/               # VS Code settings
│   ├── launch.json
│   ├── settings.json
│   └── tasks.json
├── .gitignore
├── .pre-commit-config.yaml
├── pyproject.toml         # Tool configurations
├── README.md
├── requirements.txt       # Generated dependencies
└── LICENSE                # MIT License
```

### Naming Conventions
- **Files**:
  - Use `snake_case` for Python files (e.g., `test_core.py`).
  - Configuration files may use extensions (e.g., `ci.yml`, `conf.py`).
- **Classes**:
  - Use `CamelCase` for class names (e.g., `GameManager`, `PlayerEntity`).
  - Prefix abstract base classes with `Abstract` (e.g., `AbstractSprite`).
- **Functions and Variables**:
  - Use `snake_case` for functions and variables (e.g., `load_config`, `player_speed`).
  - Constants should be `UPPER_SNAKE_CASE` (e.g., `MAX_SPEED`).
- **Tests**:
  - Test files should start with `test_` (e.g., `test_core.py`).
  - Test functions should start with `test_` (e.g., `test_arcade_version`).

For detailed Python standards, refer to the [Official Python Style Guide (PEP 8)](https://www.python.org/dev/peps/pep-0008/) and [Naming Conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions).

## Rules

- **Install Scripts**: The scripts in `install/` are locked and must not be modified in pull requests. They are designed to work across most development environments. If system-specific issues arise (e.g., OpenGL compatibility), make local adjustments without committing changes to these scripts. Contact the project owner for updates if necessary.
- **Pull Requests**: Focus on `src/`, `tests/`, and `docs/`. Changes to `install/` will be rejected unless explicitly approved by the project owner.

## Running the Project
- **Tests**: `pytest tests/ -v` (Linux/MacOS) or `py -3 -m pytest tests/ -v` (Windows).
- **Linting**: `pre-commit run --all-files`.
- **Game**: `python3 src/omega_project/main.py` (Linux/MacOS) or `py -3 src/omega_project/main.py` (Windows).
- **Docs**: `cd docs && sphinx-build -b html . _build/`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**MIT License**

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),