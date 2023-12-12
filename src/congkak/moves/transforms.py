import numpy as np

from congkak.board.containers import BoardState
from congkak.moves.containers import PlayerMove, MoveValidity
from congkak.board.transforms import side_from_player

def check_move_validity(
    board_state: BoardState,
    player_move: PlayerMove,
)->MoveValidity:
    player_side = side_from_player(
        board_state=board_state,
        player_number=player_move.player_number
    )
    if player_move.player_number != board_state.turn:
        return MoveValidity.PLAYER
    elif player_side[player_move.pit_number] < 1:
        return MoveValidity.PIT
    else:
        return MoveValidity.VALID

def move(
    board_state: BoardState,
    player_move: PlayerMove,
)->BoardState:
    return