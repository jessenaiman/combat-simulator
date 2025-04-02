FROM python:3.13

# Set working directory
WORKDIR /app

# Update package lists and install essential tools
RUN apt-get update && apt-get install -y \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Ensure pip is up-to-date
RUN python3 -m ensurepip --upgrade \
    && python3 -m pip install --upgrade pip

# Verify Python version
RUN python3 --version

RUN python -m pip install \
arcade \
pydantic \
SQLAlchemy \
pytest \
pytest-sugar \
hypothesis \
coverage \
pytest-cov \
ruff \
mypy \
pre-commit \
sphinx \
sphinxcontrib-mermaid \
--root-user-action=ignore \
-U  # Upgrade if present

CMD ["bash"]