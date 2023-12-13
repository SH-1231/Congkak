from congkak.board.containers import BoardState, PlayerNumber, Player
from congkak.moves.containers import PlayerMove
import numpy as np


def test_player_move() -> None:
    player_move = PlayerMove(player_number=PlayerNumber.ONE, pit_number=0)
    assert player_move.pit_number == 0
    assert player_move.player_number == PlayerNumber.ONE


def test_board_state() -> None:
    from congkak.board.constants import PITS_PER_SIDE

    board_state = BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0,
            side=np.random.randint(10, size=PITS_PER_SIDE),
        ),
        player_two=Player(
            number=PlayerNumber.TWO,
            score=0,
            side=np.random.randint(10, size=PITS_PER_SIDE),
        ),
    )

    assert board_state.player_one.side.shape == board_state.player_two.side.shape
    assert board_state.player_one.score >= 0
    assert board_state.player_two.score >= 0
