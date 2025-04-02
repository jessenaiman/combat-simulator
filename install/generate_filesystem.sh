# Create source directories
cd src/omega_project
mkdir audio combat commands data entities event game items narrative progression scenes shared simulation systems utils world
for dir in audio combat commands data entities event game items narrative progression scenes shared simulation systems utils world; do
    echo '"""Package for '"$dir"' functionality."""' > "$dir/__init__.py"
done

# Move existing files
mv simulator.py combat/
mv models.py data/

# Create test directories
cd ../../tests
mkdir combat data
for dir in combat data; do
    echo '"""Tests for '"$dir"' functionality."""' > "$dir/__init__.py"
done

# Move test_simulator.py to tests/combat/
mv test_simulator.py combat/