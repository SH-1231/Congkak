import dataclasses
import enum

from congkak.board.constants import PITS_PER_SIDE
from congkak.board.containers import Player


@dataclasses.dataclass(frozen=True)
class PlayerMove:
    player_number: Player
    pit_number: int

    def __post_init__(self):
        if self.pit_number > PITS_PER_SIDE - 1:
            raise ValueError(
                f"Pit selected ({self.pit_number}) is not within max number of pits: {PITS_PER_SIDE}"
            )


class MoveValidity(enum.StrEnum):
    VALID = "Valide Move Selected"
    PLAYER = "Invalid Player Moving"
    PIT = "Invalid Pit Selected"


@enum.unique
class BoardPerspective(enum.Enum):
    PLAYER = enum.auto()
    OPPONENT = enum.auto()
