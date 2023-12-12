import numpy as np

from congkak.board.containers import Player, BoardState
from congkak.moves.containers import PlayerMove

def move(
    player_move: PlayerMove,
    board_state: BoardState,
)->BoardState:
    return