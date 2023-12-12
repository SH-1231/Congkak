import numpy as np

from congkak.board.containers import BoardState
from congkak.moves.containers import PlayerMove, MoveValidity
from congkak.board.transforms import active_player_side, opponent_player_side
from congkak.board.constants import PITS_PER_SIDE
import itertools

def check_move_validity(
    board_state: BoardState,
    player_move: PlayerMove,
)->MoveValidity:
    player_side = active_player_side(
        board_state=board_state,
        player_number=player_move.player_number
    )
    if player_move.player_number != board_state.turn:
        return MoveValidity.PLAYER
    elif player_side[player_move.pit_number] < 1:
        return MoveValidity.PIT
    else:
        return MoveValidity.VALID

# def move(
#     board_state: BoardState,
#     player_move: PlayerMove,
# )->BoardState:
#     active_player = board_state.turn
#     start_pit = player_move.pit_number

#     active_side = active_player_side(board_state)
#     opponent_side = opponent_player_side(board_state)
    
#     # single
#     initial_number = start_pit[start_pit]
#     spaces_to_end = PITS_PER_SIDE - start_pit
#     overflow = initial_number - spaces_to_end
#     while overflow >= 0:
#         current_side = next(board_sides)
#         additional = np.zeros(PITS_PER_SIDE)
#         additional[start_pit: ] = 1
#         start_pit = 0
#         overflow -= PITS_PER_SIDE
#         current_side += additional

#     additional = np.zeros(PITS_PER_SIDE)
#     end_pit = PITS_PER_SIDE - 1 if overflow>0 else start_pit + initial_number
#     additional[start_pit: end_pit] = 1
#     current_side += additional
    
#     return

def steal()->BoardState:
    pass
def free()->BoardState:
    pass
def miss()->BoardState:
    pass