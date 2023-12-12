from congkak.board.containers import BoardState, PlayerNumber, Player, GameStatistics
from congkak.board.constants import PITS_PER_SIDE, MARBLES_PER_PIT
from congkak.game.custom_scenarios import CUSTOM_GAME_INDEX_TO_BOARD_STATE_MAPPING, CustomGameScenario

import numpy as np
import numpy.typing as npt

def start_game(
    custom_game_scenario: int = CustomGameScenario.NORMAL
)->BoardState:
    return CUSTOM_GAME_INDEX_TO_BOARD_STATE_MAPPING[custom_game_scenario]
def end_game(
    board_state: BoardState
)->BoardState:
    return BoardState(
        active=False,
        turn=None,
        player_one=board_state.player_one,
        player_two=board_state.player_two,
        side_one=board_state.side_one,
        side_two=board_state.side_two
    )

def check_victory(
    board_state: BoardState
)->bool:
    # game ends when no marbles in pits remaining.
    game_over = np.count_nonzero(board_state.side_one + board_state.side_two) == 0
    return game_over

def check_winner(
    board_state: BoardState
)->GameStatistics:

    margin = board_state.player_one.score - board_state.player_two.score
    if margin > 0:
        winner = board_state.player_one
    elif margin < 0:
        winner = board_state.player_two
    else:
        winner = None

    return GameStatistics(
        winner=winner,
        margin=abs(margin)
    )

def active_player_side(
    board_state: BoardState,
    player_number: PlayerNumber,
)->npt.NDArray[np.int32]:
    match player_number:
        case PlayerNumber.ONE:
            return board_state.side_one
        case PlayerNumber.TWO:
            return board_state.side_two
        case _:
            raise ValueError(
                "Only 2 sides"
            )
def opponent_player_side(
    board_state: BoardState,
    player_number: PlayerNumber,
)->npt.NDArray[np.int32]:
    match player_number:
        case PlayerNumber.ONE:
            return board_state.side_one
        case PlayerNumber.TWO:
            return board_state.side_two
        case _:
            raise ValueError(
                "Only 2 sides"
            )