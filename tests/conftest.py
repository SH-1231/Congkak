import json

import numpy as np
import pytest
from pycongkak.board.containers import BoardState, Player, PlayerNumber


@pytest.fixture
def board_state_example() -> BoardState:
    return BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE, score=0, side=np.array([0, 1, 0, 0, 0, 0, 1])
        ),
        player_two=Player(
            number=PlayerNumber.TWO, score=0, side=np.array([0, 0, 0, 0, 0, 0, 1])
        ),
    )


@pytest.fixture
def board_state_example_json() -> str:
    board_state = {
        "active": True,
        "turn": PlayerNumber.ONE,
        "player_one": {
            "number": PlayerNumber.ONE,
            "score": 0,
            "side": [0, 1, 0, 0, 0, 0, 1],
        },
        "player_two": {
            "number": PlayerNumber.TWO,
            "score": 0,
            "side": [0, 0, 0, 0, 0, 0, 1],
        },
        "n_turns": 1,
    }
    return json.dumps(board_state, separators=(",", ":"))


@pytest.fixture
def board_state_endgame_example() -> BoardState:
    return BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=1,
            side=np.array([0, 0, 0, 0, 0, 0, 0]),
        ),
        player_two=Player(
            number=PlayerNumber.TWO, score=1, side=np.array([0, 0, 0, 0, 0, 0, 0])
        ),
    )


@pytest.fixture
def player_one_win_board_state():
    return BoardState(
        active=False,
        turn=None,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=1,
            side=np.array([0, 0, 0, 0, 0, 0, 0]),
        ),
        player_two=Player(
            number=PlayerNumber.TWO, score=0, side=np.array([0, 0, 0, 0, 0, 0, 0])
        ),
    )


@pytest.fixture
def player_two_win_board_state():
    return BoardState(
        active=False,
        turn=None,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0,
            side=np.array([0, 0, 0, 0, 0, 0, 0]),
        ),
        player_two=Player(
            number=PlayerNumber.TWO, score=1, side=np.array([0, 0, 0, 0, 0, 0, 0])
        ),
    )


@pytest.fixture
def extra_turn_board_state_example() -> BoardState:
    return BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=1,
            side=np.array([0, 0, 0, 0, 0, 0, 1]),
        ),
        player_two=Player(
            number=PlayerNumber.TWO, score=1, side=np.array([0, 1, 0, 0, 0, 0, 0])
        ),
    )


@pytest.fixture
def steal_board_state_example() -> BoardState:
    return BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=1,
            side=np.array([0, 1, 0, 0, 0, 0, 0]),
        ),
        player_two=Player(
            number=PlayerNumber.TWO, score=1, side=np.array([0, 1, 0, 0, 1, 0, 0])
        ),
    )


@pytest.fixture
def lose_go_board_state_example() -> BoardState:
    return BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=1,
            side=np.array([0, 0, 0, 0, 0, 0, 2]),
        ),
        player_two=Player(
            number=PlayerNumber.TWO, score=1, side=np.array([0, 0, 0, 1, 0, 0, 0])
        ),
    )
