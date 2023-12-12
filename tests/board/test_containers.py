from congkak.board.containers import PlayerMove, BoardState, PlayerNumber, Player
import numpy as np

def test_player_move()->None:
    player_move = PlayerMove(
        player_number=PlayerNumber.ONE,
        pit_number=0
    )
    assert player_move.pit_number == 0
    assert player_move.player_number == PlayerNumber.ONE

def test_board_state()-> None:
    from congkak.board.constants import PITS_PER_SIDE
    board_state = BoardState(
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
        side_one=np.random.rand(PITS_PER_SIDE),
        side_two=np.random.rand(PITS_PER_SIDE),
    )

    assert board_state.side_one.shape == board_state.side_two.shape
    assert board_state.player_one.score >= 0
    assert board_state.player_two.score >= 0