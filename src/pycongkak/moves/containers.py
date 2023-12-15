import dataclasses
import enum

from pycongkak.board.constants import PITS_PER_SIDE
from pycongkak.board.containers import PlayerNumber


@dataclasses.dataclass(frozen=True)
class PlayerMove:
    player_number: PlayerNumber | None
    pit_number: int

    def __post_init__(self):
        if self.pit_number > PITS_PER_SIDE - 1:
            raise ValueError(
                f"Pit selected ({self.pit_number}) is not within max number of pits: {PITS_PER_SIDE}"  # noqa: E501
            )


class MoveValidity(enum.StrEnum):
    VALID = "Valide Move Selected"
    PLAYER = "Invalid Player Moving"
    PIT = "Invalid Pit Selected"


@enum.unique
class BoardPerspective(enum.Enum):
    PLAYER = enum.auto()
    OPPONENT = enum.auto()


@enum.unique
class MoveCase(enum.Enum):
    NORMAL = enum.auto()
    FREE = enum.auto()
    STEAL = enum.auto()
    MISS = enum.auto()
