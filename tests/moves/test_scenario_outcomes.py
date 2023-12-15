import numpy as np
import pytest
from pycongkak.board.containers import BoardState, GameStatistics, Player, PlayerNumber
from pycongkak.board.transforms import check_victory, check_winner
from pycongkak.moves.transforms import move
from pycongkak.testing import dataclasses_instances_equal


@pytest.fixture
def custom_initial_board() -> BoardState:
    return BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0,
            side=np.array([1, 0, 0, 5, 3, 2, 1]),
        ),
        player_two=Player(
            number=PlayerNumber.TWO,
            score=0,
            side=np.array([0, 0, 0, 0, 2, 10, 2]),
        ),
    )


def test_custom_scenario(custom_initial_board: BoardState) -> None:
    state_1 = move(custom_initial_board, 6)
    state_2 = move(state_1, 5)
    state_3 = move(state_2, 6)
    state_4 = move(state_3, 4)
    state_5 = move(state_4, 6)
    state_6 = move(state_5, 0)
    state_7 = move(state_6, 6)
    state_8 = move(state_7, 5)
    state_9 = move(state_8, 1)
    state_10 = move(state_9, 3)
    state_11 = move(state_10, 0)
    state_12 = move(state_11, 1)
    state_13 = move(state_12, 6)
    state_14 = move(state_13, 2)
    state_15 = move(state_14, 3)
    state_16 = move(state_15, 0)
    state_17 = move(state_16, 4)
    state_18 = move(state_17, 5)
    state_19 = move(state_18, 6)
    state_20 = move(state_19, 0)
    state_21 = move(state_20, 1)
    state_22 = move(state_21, 2)
    state_23 = move(state_22, 3)
    state_24 = move(state_23, 4)
    state_25 = move(state_24, 5)
    state_26 = move(state_25, 6)
    victory = check_victory(state_26)
    scenario_winner = check_winner(state_26)
    assert victory is True
    expected_winner = GameStatistics(
        winner=Player(PlayerNumber.ONE, score=19, side=np.array([0, 0, 0, 0, 0, 0, 0])),
        loser=Player(PlayerNumber.TWO, score=7, side=np.array([0, 0, 0, 0, 0, 0, 0])),
        margin=12,
    )
    assert dataclasses_instances_equal(scenario_winner, expected_winner)
