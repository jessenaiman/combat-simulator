#!/bin/bash
# install_core.sh
# Assumes virtual environment is active; suppresses root user warning
pip install \
  arcade \
  pydantic \
  SQLAlchemy \
  --root-user-action=ignore \
  -U  # Upgrade if present
echo "Core dependencies installed: Arcade, pydantic, SQLAlchemy"
echo "Note: JSON handling uses Python's built-in 'json' module."