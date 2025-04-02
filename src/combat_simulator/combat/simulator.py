"""Combat simulator logic for managing battles between characters."""
from typing import Optional, List
import json
from ..data.models import BattleState, Session
from sqlalchemy.orm import Session as SQLSession

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

    def save_state(self) -> int:
        """Save the current battle state to the database and return the state ID."""
        if not self.player or not self.enemy:
            raise ValueError("Cannot save state: Battle not set up.")
        with Session() as session:
            state = BattleState(
                player_name=self.player.name,
                player_health=self.player.health,
                player_attack=self.player.attack,
                enemy_name=self.enemy.name,
                enemy_health=self.enemy.health,
                enemy_attack=self.enemy.attack,
                turn_history=json.dumps(self.turn_history)
            )
            session.add(state)
            session.commit()
            return state.id

    def load_state(self, state_id: int) -> None:
        """Load a battle state from the database by ID."""
        with Session() as session:
            state = session.query(BattleState).filter_by(id=state_id).first()
            if not state:
                raise ValueError(f"No battle state found with ID {state_id}")
            self.player = Character(state.player_name, state.player_health, state.player_attack)
            self.enemy = Character(state.enemy_name, state.enemy_health, state.enemy_attack)
            self.turn_history = json.loads(state.turn_history)