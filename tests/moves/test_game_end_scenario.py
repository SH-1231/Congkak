import numpy as np
from pycongkak.board.containers import BoardState, GameStatistics, Player, PlayerNumber
from pycongkak.board.transforms import check_victory, check_winner
from pycongkak.moves.transforms import move
from pycongkak.testing import dataclasses_instances_equal


def test_win_by_no_marbles_initial_board() -> None:
    initial_board = BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        n_turns=1,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0,
            side=np.array([0, 0, 0, 0, 0, 0, 1]),
        ),
        player_two=Player(
            number=PlayerNumber.TWO,
            score=10,
            side=np.array([0, 0, 0, 0, 2, 10, 2]),
        ),
    )

    state_1 = move(initial_board, 6)
    victory = check_victory(state_1)
    scenario_winner = check_winner(state_1)
    assert victory is True
    expected_winner = GameStatistics(
        winner=Player(
            PlayerNumber.TWO, score=10, side=np.array([0, 0, 0, 0, 2, 10, 2])
        ),
        player_two=Player(
            PlayerNumber.TWO, score=10, side=np.array([0, 0, 0, 0, 2, 10, 2])
        ),
        player_one=Player(
            PlayerNumber.ONE, score=1, side=np.array([0, 0, 0, 0, 0, 0, 0])
        ),
        margin=9,
    )
    assert dataclasses_instances_equal(scenario_winner, expected_winner)


def test_draw_when_no_marbles_initial_board() -> None:
    initial_board = BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        n_turns=1,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0,
            side=np.array([0, 0, 0, 0, 0, 0, 1]),
        ),
        player_two=Player(
            number=PlayerNumber.TWO,
            score=1,
            side=np.array([0, 0, 0, 0, 2, 10, 2]),
        ),
    )

    state_1 = move(initial_board, 6)
    victory = check_victory(state_1)
    scenario_winner = check_winner(state_1)
    assert victory is True
    expected_winner = GameStatistics(
        winner=None,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=1,
            side=np.array([0, 0, 0, 0, 0, 0, 0]),
        ),
        player_two=Player(
            number=PlayerNumber.TWO,
            score=1,
            side=np.array([0, 0, 0, 0, 2, 10, 2]),
        ),
        margin=0,
    )
    assert dataclasses_instances_equal(scenario_winner, expected_winner)
