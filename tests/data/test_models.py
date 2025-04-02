"""Tests for database models."""
import pytest
from combat_simulator.data.models import BattleState, Session

def test_battle_state_creation() -> None:
    """Test creating a battle state in the database."""
    with Session() as session:
        state = BattleState(
            player_name="Hero",
            player_health=100,
            player_attack=20,
            enemy_name="Goblin",
            enemy_health=50,
            enemy_attack=10,
            turn_history="[]"
        )
        session.add(state)
        session.commit()
        assert state.id is not None