# install_core.bat (Windows)
@echo off
py -3 -m pip install ^
  arcade==3.0.2 ^
  pydantic==2.8.2 ^
  SQLAlchemy==2.0.35 ^
  toml==0.10.2 ^
  -U
echo Core dependencies installed: Arcade, pydantic, SQLAlchemy, toml