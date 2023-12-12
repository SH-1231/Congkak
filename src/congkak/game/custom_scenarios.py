from congkak.board.containers import CustomGameScenarios, BoardState, PlayerNumber, Player
from congkak.board.constants import PITS_PER_SIDE, MARBLES_PER_PIT
import numpy as np

__all__ = [
    "CUSTOM_GAME_INDEX_TO_BOARD_STATE_MAPPING"
]
CUSTOM_GAME_INDEX_TO_BOARD_STATE_MAPPING = {
    CustomGameScenarios.NORMAL: BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0
        ),
        player_two=Player(
            number=PlayerNumber.TWO,
            score=0
        ),
        side_one=np.zeros(PITS_PER_SIDE),
        side_two=np.zeros(PITS_PER_SIDE)
    ),
    CustomGameScenarios.FREE_GO: BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0
        ),
        player_two=Player(
            number=PlayerNumber.TWO,
            score=0
        ),
        side_one=np.array([0 for _ in range(PITS_PER_SIDE-1)]+[1]),
        side_two=np.zeros(PITS_PER_SIDE)
    ),
    CustomGameScenarios.STEAL: BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0
        ),
        player_two=Player(
            number=PlayerNumber.TWO,
            score=0
        ),
        side_one=np.array([1] + [0 for _ in range(PITS_PER_SIDE-1)]),
        side_two=np.array([0] + [0 for _ in range(PITS_PER_SIDE-2)] + [0])
    ),
    CustomGameScenarios.LOSE_GO: BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0
        ),
        player_two=Player(
            number=PlayerNumber.TWO,
            score=0
        ),
        side_one=np.array([0 for _ in range(PITS_PER_SIDE-1)] + [2]),
        side_two=np.zeros(PITS_PER_SIDE)
    ),
    CustomGameScenarios.SCENARIO_1: BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0
        ),
        player_two=Player(
            number=PlayerNumber.TWO,
            score=0
        ),
        side_one=np.ones(PITS_PER_SIDE),
        side_two=np.ones(PITS_PER_SIDE)
    )
}