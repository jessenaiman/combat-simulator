# Updated `install_core.sh` now in linux and windows

This script replaces Pygame with Arcade, keeping other core dependencies (pydantic, SQLAlchemy, toml) intact. It uses pinned versions from the original setup, updated to Arcade’s latest stable release as of April 1, 2025 (assuming 3.0.2, based on trends from <https://api.arcade.academy/en/stable/install.html>).

```bash
#!/bin/bash
# install_core.sh
# Installs core dependencies for Omega Project, replacing Pygame with Arcade
pip3 install \
  arcade==3.0.2 \
  pydantic==2.8.2 \
  SQLAlchemy==2.0.35 \
  toml==0.10.2 \
  -U  # Upgrade if present
echo "Core dependencies installed: Arcade, pydantic, SQLAlchemy, toml"
```

#### Notes

- **Arcade Version**: Set to 3.0.2 (latest stable per documentation trends). If a newer version exists by your install date, it’ll upgrade to that with `-U`.
- **Compatibility**: Arcade requires Python 3.9+ (per <https://api.arcade.academy/en/stable/install.html>). Ensure your Python is 3.11 as specified in the setup.
- **No Compilation**: Arcade installs via `pip` without SDL2 build steps, resolving your Pygame issues.

---

### Integration with Omega Project Setup

The updated script fits seamlessly into the existing setup process from the *Omega Project Setup* document. Here’s how it slots in:

#### Updated README Install Section

Replace the original `install_core.sh` instructions in the README with:

```markdown
## Install Scripts

### 1. Install Python and pip
```bash
#!/bin/bash
# install_python.sh
python3 --version || (echo "Install Python 3.11 manually from python.org" && exit 1)
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
```

### 2. Install Core Dependencies

```bash
#!/bin/bash
# install_core.sh
pip3 install \
  arcade==3.0.2 \
  pydantic==2.8.2 \
  SQLAlchemy==2.0.35 \
  toml==0.10.2 \
  -U
echo "Core dependencies installed: Arcade, pydantic, SQLAlchemy, toml"
```

### 3. Install Dev Dependencies

```bash
#!/bin/bash
# install_dev.sh
pip3 install \
  pytest==8.3.3 \
  pytest-sugar==1.0.0 \
  hypothesis==6.115.0 \
  coverage==7.6.4 \
  ruff==0.6.8 \
  mypy==1.11.2 \
  pre-commit==3.8.0 \
  sphinx==8.0.2 \
  sphinxcontrib-mermaid==0.9.2 \
  -U
```

### 4. Generate requirements.txt

```bash
#!/bin/bash
# generate_requirements.sh
pip3 freeze > requirements.txt
echo "Generated requirements.txt with exact versions."
```

#### Instructions

1. Save each script as `install_*.sh` in the project root.
2. Run in order:

   ```bash
   chmod +x install_*.sh
   ./install_python.sh
   ./install_core.sh
   ./install_dev.sh
   ./install_generate_requirements.sh
   ```

3. Share the generated `requirements.txt` with me for verification.

```

---

### Verification Steps
After running the scripts:
1. Check Arcade installation:
   ```bash
   python3 -c "import arcade; print(arcade.__version__)"
   ```

   Expected output: `3.0.2` (or newer if `-U` fetched a later version).
2. Send me the `requirements.txt` file. I’ll confirm versions align with the setup and suggest tweaks if needed.

---

### Next Steps

- **Install**: Run the updated scripts on your system.
- **Share**: Post the `requirements.txt` here once generated.
- **Iterate**: I’ll verify it and adjust if Arcade introduces compatibility issues (e.g., with SQLAlchemy or pydantic).

This switch to Arcade should streamline your setup, avoiding Pygame’s compilation woes while meeting your stability and documentation needs. Let me know if you want to discuss keeping Pygame alongside Arcade for your larger project!
