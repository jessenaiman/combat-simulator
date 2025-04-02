# install_python.sh (Linux/MacOS)
#!/bin/bash
if ! command -v python3.13 &> /dev/null; then
    echo "Install Python 3.13+ from python.org"
    exit 1
fi
python --version
python -m ensurepip --upgrade
python -m pip install --upgrade pip