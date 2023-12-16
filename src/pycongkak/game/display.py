from importlib import metadata

import numpy as np

from pycongkak.board.constants import PITS_PER_SIDE
from pycongkak.board.containers import BoardState, GameStatistics, Player, PlayerNumber
from pycongkak.moves.containers import BoardPerspective

__all__ = ["PYCONGKAK_DISPLAY_STRING"]
PYCONGKAK_DISPLAY_STRING = f"Pypycongkak@{metadata.version('pycongkak')} by Shaun Ho\n"


def int_to_string_with_min_spacing(integer: int, min_characters: int = 2) -> str:
    text = str(integer)
    whitespace_needed = max(0, min_characters - len(text))
    formatted_text = " " * whitespace_needed + text
    return formatted_text


def terminal_show_board(board_state: BoardState, fixed_board: bool = True) -> None:
    if fixed_board is False:
        mapping: dict[BoardPerspective, Player] = {}
        match board_state.turn:
            case PlayerNumber.ONE:
                mapping[BoardPerspective.PLAYER] = board_state.player_one
                mapping[BoardPerspective.OPPONENT] = board_state.player_two
            case PlayerNumber.TWO:
                mapping[BoardPerspective.PLAYER] = board_state.player_two
                mapping[BoardPerspective.OPPONENT] = board_state.player_one
            case _:
                raise ValueError("Unknown player turn")

        opponent = mapping[BoardPerspective.OPPONENT]
        player = mapping[BoardPerspective.PLAYER]
    else:
        opponent = board_state.player_two
        player = board_state.player_one

    opponent_side = opponent.side.tolist()
    player_side = np.flip(player.side).tolist()
    player_side_str_start = "\\-["
    opponent_side_str_start = "/-["
    for i in range(PITS_PER_SIDE):
        player_side_str_start += f"{int_to_string_with_min_spacing(player_side[i])},"
        opponent_side_str_start += (
            f"{int_to_string_with_min_spacing(opponent_side[i])},"
        )
    player_side_str = player_side_str_start[:-1] + "]-/"
    opponent_side_str = opponent_side_str_start[:-1] + "]-\\"

    spacing = "\n"
    turn_string = (
        f"Player {board_state.turn}'s go, {board_state.n_turns} turns remaining\n"
    )
    spacing = "\n"
    opponent_pit_number = "pit number:  1  2  3  4  5  6  7  \n"
    spacing = "\n"
    opponent_number = f"                   Player {opponent.number}\n"
    opponent_side = f"         {opponent_side_str}  [{opponent.score:02}]\n"
    dividing_line = "        <-------------------------->\n"
    player_side = f"   [{player.score:02}]  {player_side_str} \n"
    player_number = f"                   Player {player.number}\n"
    spacing = "\n"
    player_pit_number = "pit number:  7  6  5  4  3  2  1  \n"
    spacing = "\n"

    string_to_print = (
        PYCONGKAK_DISPLAY_STRING
        + spacing
        + turn_string
        + spacing
        + opponent_pit_number
        + spacing
        + opponent_number
        + opponent_side
        + dividing_line
        + player_side
        + player_number
        + spacing
        + player_pit_number
    )
    print(string_to_print)


def terminal_show_victory(game_statistics: GameStatistics):
    game_ended_string = "<-- Game Ended -->\n"
    if game_statistics.winner is not None:
        winner_string_1 = f"Winner: Player {game_statistics.winner.number}"
        winner_string_2 = f", scoring {game_statistics.winner.score}"
        string_to_print = (
            PYCONGKAK_DISPLAY_STRING
            + game_ended_string
            + winner_string_1
            + winner_string_2
        )
    else:
        draw_string = (
            f"Draw: Both players scored {game_statistics.player_one.score} marbles"
        )
        string_to_print = PYCONGKAK_DISPLAY_STRING + game_ended_string + draw_string

    print(string_to_print)


def terminal_show_quit():
    pass
