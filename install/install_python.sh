#!/bin/bash
# install_python.sh
# Ensure Python 3.11 and pip are installed
python --version || (echo "Install Python manually" && exit 1)
python -m ensurepip --upgrade
python -m pip install --upgrade pip