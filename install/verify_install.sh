# verify_install.sh (Linux/MacOS)
#!/bin/bash
echo "Verifying Arcade:"
python -c "import arcade; print(arcade.__version__); arcade.open_window(600, 600, 'Test'); arcade.set_background_color(arcade.color.WHITE); arcade.run()"
echo "Verifying SQLite:"
python -c "import sqlalchemy as sa; e = sa.create_engine('sqlite:///data/omega_project.db'); c = e.connect(); print(c.execute(sa.text('SELECT sqlite_version();')).scalar()); c.close()"