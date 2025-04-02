from typing import List, Optional


class Character:
    def __init__(self, name: str, health: int, attack: int) -> None:
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage: int) -> None:
        self.health = max(0, self.health - damage)

    def is_alive(self) -> bool:
        return self.health > 0

class CombatSimulator:
    def __init__(self) -> None:
        self.player: Optional[Character] = None
        self.enemy: Optional[Character] = None
        self.turn_history: List[str] = []

    def setup_battle(self, player: Character, enemy: Character) -> None:
        self.player = player
        self.enemy = enemy
        self.turn_history = []
        self.turn_history.append(f"Battle started: {player.name} vs {enemy.name}")

    def simulate_turn(self) -> str:
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
        return self.turn_history
