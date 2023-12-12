import numpy as np
from congkak.moves.transforms import  check_move_validity
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

# def test_move_normal(
#     board_state_example: BoardState,
# )->None:
#     new_board_state = move(
#         board_state=board_state_example,
#         player_move=PlayerMove(
#             player_number=PlayerNumber.ONE,
#             pit_number=1
#         )
#     )
#     assert new_board_state == BoardState(
#         active=True,
#         turn=PlayerNumber.TWO,
#         player_one=Player(
#             number=PlayerNumber.ONE,
#             score=1
#         ),
#         player_two=Player(
#             number=PlayerNumber.TWO,
#             score=0
#         ),
#         side_one=np.array([0,0,1,0,0,0,1]),
#         side_two=np.array([0,0,0,0,0,0,1])
#     )