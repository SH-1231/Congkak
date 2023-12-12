import numpy as np
from congkak.moves.transforms import move, check_valid_move
from congkak.moves.containers import PlayerMove
from congkak.board.containers import BoardState, PlayerNumber

def test_check_valid_move(
    board_state_example: BoardState,
)->None:
    valid_move = check_valid_move(
        board_state=board_state_example,
        player_move=PlayerMove(
            player_number=PlayerNumber.TWO,
            pit_number=0
        )
    )
def test_move(
    board_state_example: BoardState,
)->None:
    test = move(
        board_state=board_state_example,
        player_move=PlayerMove(
            player_number=PlayerNumber.ONE,
            pit_number=1
        )
    )