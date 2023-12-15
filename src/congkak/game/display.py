from importlib import metadata

import numpy as np

from congkak.board.constants import PITS_PER_SIDE
from congkak.board.containers import BoardState, Player, PlayerNumber
from congkak.moves.containers import BoardPerspective


def int_to_string_with_min_spacing(integer: int, min_characters: int = 2) -> str:
    text = str(integer)
    whitespace_needed = max(0, min_characters - len(text))
    formatted_text = " " * whitespace_needed + text
    return formatted_text


def terminal_show_board(
    board_state: BoardState,
) -> None:
    mapping: dict[BoardPerspective, Player] = {}
    match board_state.turn:
        case PlayerNumber.ONE:
            mapping[BoardPerspective.PLAYER] = board_state.player_one
            mapping[BoardPerspective.OPPONENT] = board_state.player_two
        case PlayerNumber.TWO:
            mapping[BoardPerspective.PLAYER] = board_state.player_two
            mapping[BoardPerspective.OPPONENT] = board_state.player_one
        case i:
            raise ValueError("Unknown player turn")

    opponent = mapping[BoardPerspective.OPPONENT]
    player = mapping[BoardPerspective.PLAYER]

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

    congkak_string_____ = f"PyCongkak@{metadata.version('congkak')} by Shaun Ho\n"
    spacing = "\n"
    turn_string________ = (
        f"Player {board_state.turn}'s go, {board_state.n_turns} turns remaining\n"
    )
    spacing = "\n"
    opponent_pit_number = "pit number:  1  2  3  4  5  6  7  \n"
    spacing = "\n"
    opponent_side______ = f"         {opponent_side_str}  [{opponent.score:02}]\n"
    dividing_line______ = "        <-------------------------->\n"
    player_side________ = f"   [{player.score:02}]  {player_side_str} \n"
    spacing = "\n"
    player_pit_number__ = "pit number:  7  6  5  4  3  2  1  \n"
    spacing = "\n"
    selector_text______ = "Please select a pit number [0-6]: "

    string_to_print = (
        congkak_string_____
        + spacing
        + turn_string________
        + spacing
        + opponent_pit_number
        + spacing
        + opponent_side______
        + dividing_line______
        + player_side________
        + spacing
        + player_pit_number__
        + spacing
        + selector_text______
    )
    print(string_to_print)
