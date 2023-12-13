import dataclasses
import enum

import numpy as np
import numpy.typing as npt


@enum.unique
class PlayerNumber(enum.Enum):
    ONE = enum.auto()
    TWO = enum.auto()


@dataclasses.dataclass
class Player:
    number: PlayerNumber
    score: int
    side: npt.NDArray[np.int32]


@dataclasses.dataclass(frozen=True)
class BoardState:
    active: bool
    turn: PlayerNumber | None
    player_one: Player
    player_two: Player


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
    NORMAL = enum.auto()
    MOVE = enum.auto()
    FREE_GO = enum.auto()
    STEAL = enum.auto()
    LOSE_GO = enum.auto()
    SCENARIO_1 = enum.auto()
