"""Tests for the combat simulator logic."""
from omega_project.simulator import Character, CombatSimulator


def test_character_take_damage() -> None:
    """Test that a character takes damage correctly."""
    char = Character("Hero", 100, 10)
    char.take_damage(30)
    assert char.health == 70
    char.take_damage(80)
    assert char.health == 0

def test_combat_simulator_turn() -> None:
    """Test a single turn where one character defeats another."""
    sim = CombatSimulator()
    player = Character("Hero", 100, 20)
    enemy = Character("Goblin", 50, 10)
    sim.setup_battle(player, enemy)
    result = sim.simulate_turn()
    assert result == "Goblin is defeated!"
    assert player.health == 100  # Enemy defeated before attacking
    history = sim.get_turn_history()
    assert history == [
        "Battle started: Hero vs Goblin",
        "Hero attacks Goblin for 20 damage",
        "Goblin is defeated!"
    ]

def test_combat_simulator_uninitialized() -> None:
    """Test that an uninitialized simulator handles turns correctly."""
    sim = CombatSimulator()
    result = sim.simulate_turn()
    assert result == "Battle not set up."
    assert sim.get_turn_history() == ["Error: Battle not set up."]

def test_combat_simulator_multiple_turns() -> None:
    """Test multiple turns in a battle with ongoing combat."""
    sim = CombatSimulator()
    player = Character("Hero", 100, 10)
    enemy = Character("Goblin", 50, 5)
    sim.setup_battle(player, enemy)
    result = sim.simulate_turn()  # Hero: 95, Goblin: 40
    assert result == "Battle continues."
    result = sim.simulate_turn()  # Hero: 90, Goblin: 30
    assert result == "Battle continues."
    history = sim.get_turn_history()
    assert len(history) == 5  # Start + 2 turns (attack + counterattack each)
