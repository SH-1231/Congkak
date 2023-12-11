from congkak.containers import PlayerMove, BoardState, Player
import numpy as np

def test_player_move()->None:
    player_move = PlayerMove(
        player=Player.ONE,
        pit_number=0
    )
    assert player_move.pit_number == 0
    assert player_move.player == Player.ONE

def test_board_state()-> None:
    from congkak.constants import PITS_PER_SIDE
    board_state = BoardState(
        active=True,
        turn=Player.ONE,
        side_one=np.random.rand(PITS_PER_SIDE),
        side_two=np.random.rand(PITS_PER_SIDE),
        score_one=0,
        score_two=0
    )

    assert board_state.side_one.shape == board_state.side_two.shape
    assert board_state.score_one >= 0
    assert board_state.score_two >= 0