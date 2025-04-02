"""Database models for the combat simulator."""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class BattleState(Base):
    """Represents a saved battle state in the database."""
    __tablename__ = "battle_states"

    id = Column(Integer, primary_key=True)
    player_name = Column(String, nullable=False)
    player_health = Column(Integer, nullable=False)
    player_attack = Column(Integer, nullable=False)
    enemy_name = Column(String, nullable=False)
    enemy_health = Column(Integer, nullable=False)
    enemy_attack = Column(Integer, nullable=False)
    turn_history = Column(String, nullable=False)  # Store as JSON string for simplicity

# Initialize the database
engine = create_engine("sqlite:///data/omega_project.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)