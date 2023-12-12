import dataclasses
import numpy as np
import numpy.typing as npt
import enum

from congkak.board.constants import PITS_PER_SIDE

enum.unique
class PlayerNumber(enum.Enum):
    ONE = enum.auto()
    TWO = enum.auto()
@dataclasses.dataclass
class Player:
    number: PlayerNumber
    score: int


@dataclasses.dataclass(frozen=True)
class BoardState:
    active: bool
    turn: PlayerNumber | None
    player_one: Player
    player_two: Player
    side_one: npt.NDArray[np.int32]
    side_two: npt.NDArray[np.int32]

@dataclasses.dataclass()
class GameData:
    concluded: bool
    rounds: int
    player_one: Player
    player_two: Player
    
@dataclasses.dataclass
class GameStatistics:
    winner: Player | None
    margin: int

@enum.unique
class CustomGameScenarios(enum.Enum):
    NORMAL= enum.auto()
    MOVE= enum.auto()
    FREE_GO= enum.auto()
    STEAL= enum.auto()
    LOSE_GO= enum.auto()
    SCENARIO_1= enum.auto()