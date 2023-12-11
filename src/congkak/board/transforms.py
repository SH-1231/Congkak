from congkak.board.containers import BoardState, PlayerNumber, PlayerMove, Player
from congkak.board.constants import PITS_PER_SIDE, MARBLES_PER_PIT

import numpy as np

def start_game()->BoardState:
    return BoardState(
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
        side_two=np.zeros(PITS_PER_SIDE),
        side_one=np.zeros(PITS_PER_SIDE)
    )

def check_victory(
    board_state: BoardState
)->bool:
    # game ends when no marbles in pits remaining.
    game_over = np.count_nonzero(board_state.side_one + board_state.side_two) == 0
    return game_over
