import dataclasses

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
