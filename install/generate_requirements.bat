# generate_requirements.bat (Windows)
@echo off
py -3 -m pip freeze > requirements.txt
echo Generated requirements.txt with exact versions