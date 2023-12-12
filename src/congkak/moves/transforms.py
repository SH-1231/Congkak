import numpy as np

from congkak.board.containers import Player, BoardState
from congkak.moves.containers import PlayerMove, MoveCondition

def check_valid_move(
    board_state: BoardState,
    player_move: PlayerMove,
)->MoveCondition:
    if player_move.player_number != board_state.turn:
        return MoveCondition.PLAYER

    return

def move(
    board_state: BoardState,
    player_move: PlayerMove,
)->BoardState:
    return