from importlib import metadata

import numpy as np

from pycongkak.board.constants import PITS_PER_SIDE
from pycongkak.board.containers import BoardState, Player, PlayerNumber
from pycongkak.moves.containers import BoardPerspective


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

    pycongkak_string_____ = f"Pypycongkak@{metadata.version('pycongkak')} by Shaun Ho\n"
    spacing = "\n"
    turn_string________ = (
        f"Player {board_state.turn}'s go, {board_state.n_turns} turns remaining\n"
    )
    spacing = "\n"
    opponent_pit_number = "pit number:  1  2  3  4  5  6  7  \n"
    spacing = "\n"
    opponent_number____ = f"                   Player {opponent.number}\n"
    opponent_side______ = f"         {opponent_side_str}  [{opponent.score:02}]\n"
    dividing_line______ = "        <-------------------------->\n"
    player_side________ = f"   [{player.score:02}]  {player_side_str} \n"
    player_number______ = f"                   Player {player.number}\n"
    spacing = "\n"
    player_pit_number__ = "pit number:  7  6  5  4  3  2  1  \n"
    spacing = "\n"
    selector_text______ = "Please select a pit number [0-6]: "

    string_to_print = (
        pycongkak_string_____
        + spacing
        + turn_string________
        + spacing
        + opponent_pit_number
        + spacing
        + opponent_number____
        + opponent_side______
        + dividing_line______
        + player_side________
        + player_number______
        + spacing
        + player_pit_number__
        + spacing
        + selector_text______
    )
    print(string_to_print)
