cd src\omega_project
mkdir audio combat commands data entities event game items narrative progression scenes shared simulation systems utils world
for %d in (audio combat commands data entities event game items narrative progression scenes shared simulation systems utils world) do (
    echo """Package for %d functionality.""" > %d\__init__.py
)

:: Move existing files
move simulator.py combat\
move models.py data\

cd ..\..\tests
mkdir combat data
for %d in (combat data) do (
    echo """Tests for %d functionality.""" > %d\__init__.py
)

:: Move test_simulator.py to tests/combat/
move test_simulator.py combat\