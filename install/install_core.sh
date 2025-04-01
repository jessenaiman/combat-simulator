#!/bin/bash
# install_core.sh
# Installs core dependencies for Omega Project with Arcade
pip3 install \
  arcade==3.0.2 \
  pydantic==2.8.2 \
  SQLAlchemy==2.0.35 \
  toml==0.10.2 \
  -U  # Upgrade if present
echo "Core dependencies installed: Arcade, pydantic, SQLAlchemy, toml"