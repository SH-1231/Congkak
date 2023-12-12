import numpy as np
from congkak.moves.transforms import move, check_move_validity
from congkak.moves.containers import PlayerMove, MoveValidity
from congkak.board.containers import BoardState, PlayerNumber

def test_check_valid_move(
    board_state_example: BoardState,
)->None:
    move_validity = check_move_validity(
        board_state=board_state_example,
        player_move=PlayerMove(
            player_number=PlayerNumber.ONE,
            pit_number=1
        )
    )
    assert move_validity == MoveValidity.VALID

def test_check_invalid_player(
    board_state_example: BoardState,
)->None:
    move_validity = check_move_validity(
        board_state=board_state_example,
        player_move=PlayerMove(
            player_number=PlayerNumber.TWO,
            pit_number=0
        )
    )
    assert move_validity == MoveValidity.PLAYER

def test_check_invalid_pit(
    board_state_example: BoardState,
)->None:
    move_validity = check_move_validity(
        board_state=board_state_example,
        player_move=PlayerMove(
            player_number=PlayerNumber.ONE,
            pit_number=0
        )
    )
    assert move_validity == MoveValidity.PIT

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