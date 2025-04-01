# verify_install.bat (Windows)
@echo off
echo Verifying Arcade:
py -3 -c "import arcade; print(arcade.__version__); arcade.open_window(600, 600, 'Test'); arcade.set_background_color(arcade.color.WHITE); arcade.run()"
echo Verifying SQLite:
py -3 -c "import sqlalchemy as sa; e = sa.create_engine('sqlite:///data/omega_project.db'); c = e.connect(); print(c.execute(sa.text('SELECT sqlite_version();')).scalar()); c.close()"