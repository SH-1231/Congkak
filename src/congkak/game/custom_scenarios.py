import enum

import numpy as np

from congkak.board.constants import PITS_PER_SIDE
from congkak.board.containers import BoardState, Player, PlayerNumber

__all__ = ["CUSTOM_GAME_INDEX_TO_BOARD_STATE_MAPPING"]


@enum.unique
class CustomGameScenario(enum.Enum):
    NORMAL = enum.auto()
    MOVE = enum.auto()
    FREE_GO = enum.auto()
    STEAL = enum.auto()
    LOSE_GO = enum.auto()
    SCENARIO_1 = enum.auto()


CUSTOM_GAME_INDEX_TO_BOARD_STATE_MAPPING = {
    CustomGameScenario.NORMAL: BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0,
            side=np.zeros(PITS_PER_SIDE, dtype=np.int32),
        ),
        player_two=Player(
            number=PlayerNumber.TWO,
            score=0,
            side=np.zeros(PITS_PER_SIDE, dtype=np.int32),
        ),
    ),
    CustomGameScenario.FREE_GO: BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0,
            side=np.array([0 for _ in range(PITS_PER_SIDE - 1)] + [1], dtype=np.int32),
        ),
        player_two=Player(
            number=PlayerNumber.TWO,
            score=0,
            side=np.zeros(PITS_PER_SIDE, dtype=np.int32),
        ),
    ),
    CustomGameScenario.STEAL: BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0,
            side=np.array([1] + [0 for _ in range(PITS_PER_SIDE - 1)], dtype=np.int32),
        ),
        player_two=Player(
            number=PlayerNumber.TWO,
            score=0,
            side=np.array(
                [0] + [0 for _ in range(PITS_PER_SIDE - 2)] + [0], dtype=np.int32
            ),
        ),
    ),
    CustomGameScenario.LOSE_GO: BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0,
            side=np.array([0 for _ in range(PITS_PER_SIDE - 1)] + [2], dtype=np.int32),
        ),
        player_two=Player(
            number=PlayerNumber.TWO,
            score=0,
            side=np.zeros(PITS_PER_SIDE, dtype=np.int32),
        ),
    ),
    CustomGameScenario.SCENARIO_1: BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0,
            side=np.array([1, 0, 0, 8, 3, 2, 1]),
        ),
        player_two=Player(
            number=PlayerNumber.TWO,
            score=0,
            side=np.array([1, 10, 3, 0, 2, 2, 2]),
        ),
    ),
}
