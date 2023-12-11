import dataclasses
import numpy as np
import numpy.typing as npt
import enum

from congkak.constants import PITS_PER_SIDE

enum.unique
class Player(enum.Enum):
    ONE = enum.auto()
    TWO = enum.auto()

@dataclasses.dataclass(frozen=True)
class PlayerMove:
    player: Player
    pit_number: int

    def __post_init__(self):
        if self.pit_number> PITS_PER_SIDE:
            raise ValueError(
                f"Pit selected ({self.pit_number}) is not within max number of pits: {PITS_PER_SIDE}"
            )

@dataclasses.dataclass(frozen=True)
class BoardState:
    active: bool
    turn: Player
    side_one: npt.NDArray[np.int32]
    side_two: npt.NDArray[np.int32]
    score_one: int
    score_two: int
