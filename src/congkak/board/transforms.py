from congkak.board.containers import BoardState, Player, GameStatistics
from congkak.game.custom_scenarios import (
    CUSTOM_GAME_INDEX_TO_BOARD_STATE_MAPPING,
    CustomGameScenario,
)

import numpy as np


def start_game(
    custom_game_scenario: CustomGameScenario = CustomGameScenario.NORMAL,
) -> BoardState:
    return CUSTOM_GAME_INDEX_TO_BOARD_STATE_MAPPING[custom_game_scenario]


def end_game(board_state: BoardState) -> BoardState:
    return BoardState(
        active=False,
        turn=None,
        player_one=board_state.player_one,
        player_two=board_state.player_two,
    )


def check_victory(board_state: BoardState) -> bool:
    # game ends when no marbles in pits remaining.
    game_over = (
        np.count_nonzero(board_state.player_one.side + board_state.player_two.side) == 0
    )
    return game_over


def check_winner(board_state: BoardState) -> GameStatistics:
    margin = board_state.player_one.score - board_state.player_two.score
    if margin > 0:
        winner = board_state.player_one
    elif margin < 0:
        winner = board_state.player_two
    else:
        winner = None

    return GameStatistics(winner=winner, margin=abs(margin))


def active_player(board_state: BoardState) -> Player:
    match board_state.turn:
        case board_state.player_one.number:
            return board_state.player_one
        case board_state.player_two.number:
            return board_state.player_two
        case _:
            raise ValueError("Only 2 players")


def opponent_player(board_state: BoardState) -> Player:
    match board_state.turn:
        case board_state.player_one.number:
            return board_state.player_two
        case board_state.player_two.number:
            return board_state.player_one
        case _:
            raise ValueError("Only 2 players")
