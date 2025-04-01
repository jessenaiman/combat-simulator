# install_python.bat (Windows)
@echo off
py -3 --version || (echo Install Python 3.11+ from python.org && exit /b 1)
py -3 -m ensurepip --upgrade
py -3 -m pip install --upgrade pip