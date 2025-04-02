"""Combat simulator logic for managing battles between characters."""
from typing import List, Optional


class Character:
    """A character in the combat simulator with health and attack attributes."""

    def __init__(self, name: str, health: int, attack: int) -> None:
        """Initialize a character with a name, health, and attack value."""
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage: int) -> None:
        """Reduce the character's health by the given damage amount."""
        self.health = max(0, self.health - damage)

    def is_alive(self) -> bool:
        """Check if the character is still alive (health > 0)."""
        return self.health > 0

class CombatSimulator:
    """A simulator for managing turn-based battles between two characters."""

    def __init__(self) -> None:
        """Initialize the combat simulator with no characters and an empty turn history."""
        self.player: Optional[Character] = None
        self.enemy: Optional[Character] = None
        self.turn_history: List[str] = []

    def setup_battle(self, player: Character, enemy: Character) -> None:
        """Set up a battle between a player and an enemy character."""
        self.player = player
        self.enemy = enemy
        self.turn_history = []
        self.turn_history.append(f"Battle started: {player.name} vs {enemy.name}")

    def simulate_turn(self) -> str:
        """Simulate a single turn of combat, updating health and turn history."""
        if not self.player or not self.enemy:
            self.turn_history.append("Error: Battle not set up.")
            return "Battle not set up."
        self.turn_history.append(f"{self.player.name} attacks {self.enemy.name} for {self.player.attack} damage")
        self.enemy.take_damage(self.player.attack)
        if self.enemy.is_alive():
            self.turn_history.append(f"{self.enemy.name} attacks {self.player.name} for {self.enemy.attack} damage")
            self.player.take_damage(self.enemy.attack)
        if not self.player.is_alive():
            self.turn_history.append(f"{self.player.name} is defeated!")
            return f"{self.player.name} is defeated!"
        if not self.enemy.is_alive():
            self.turn_history.append(f"{self.enemy.name} is defeated!")
            return f"{self.enemy.name} is defeated!"
        return "Battle continues."

    def get_turn_history(self) -> List[str]:
        """Return the history of turns in the current battle."""
        return self.turn_history
