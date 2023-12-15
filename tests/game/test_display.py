from importlib import metadata

import numpy as np
import pytest
from pycongkak.board.containers import BoardState, Player, PlayerNumber
from pycongkak.game.display import int_to_string_with_min_spacing, terminal_show_board


def test_print_with_min_spacing() -> None:
    assert int_to_string_with_min_spacing(12) == "12"
    assert int_to_string_with_min_spacing(2) == " 2"


def test_terminal_show_board_player_one(capsys: pytest.CaptureFixture) -> None:
    terminal_show_board(
        board_state=BoardState(
            active=True,
            turn=PlayerNumber.ONE,
            player_one=Player(
                number=PlayerNumber.ONE, score=10, side=np.array([1, 2, 3, 4, 5, 6, 7])
            ),
            player_two=Player(
                number=PlayerNumber.TWO, score=5, side=np.array([1, 2, 3, 4, 5, 6, 7])
            ),
            n_turns=3,
        )
    )
    pycongkak_string_____ = f"Pypycongkak@{metadata.version('pycongkak')} by Shaun Ho\n"
    spacing = "\n"
    turn_string________ = "Player 1's go, 3 turns remaining\n"
    spacing = "\n"
    opponent_pit_number = "pit number:  1  2  3  4  5  6  7  \n"
    spacing = "\n"
    opponent_number____ = "                   Player 2\n"
    opponent_side______ = "         /-[ 1, 2, 3, 4, 5, 6, 7]-\\  [05]\n"
    dividing_line______ = "        <-------------------------->\n"
    player_side________ = "   [10]  \\-[ 7, 6, 5, 4, 3, 2, 1]-/ \n"
    player_number______ = "                   Player 1\n"
    spacing = "\n"
    player_pit_number__ = "pit number:  7  6  5  4  3  2  1  \n"
    spacing = "\n"
    selector_text______ = "Please select a pit number [0-6]: \n"

    expected_string = (
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
    capture_result = capsys.readouterr()
    expected_print_statement = capture_result.out
    assert expected_print_statement == expected_string


def test_terminal_show_board_player_two(capsys: pytest.CaptureFixture) -> None:
    terminal_show_board(
        board_state=BoardState(
            active=True,
            turn=PlayerNumber.TWO,
            player_one=Player(
                number=PlayerNumber.ONE, score=10, side=np.array([1, 2, 3, 4, 5, 6, 7])
            ),
            player_two=Player(
                number=PlayerNumber.TWO, score=5, side=np.array([1, 2, 3, 4, 5, 6, 7])
            ),
            n_turns=3,
        ),
        fixed_board=True,
    )
    pycongkak_string_____ = f"Pypycongkak@{metadata.version('pycongkak')} by Shaun Ho\n"
    spacing = "\n"
    turn_string________ = "Player 2's go, 3 turns remaining\n"
    spacing = "\n"
    opponent_pit_number = "pit number:  1  2  3  4  5  6  7  \n"
    spacing = "\n"
    opponent_number____ = "                   Player 2\n"
    opponent_side______ = "         /-[ 1, 2, 3, 4, 5, 6, 7]-\\  [05]\n"
    dividing_line______ = "        <-------------------------->\n"
    player_side________ = "   [10]  \\-[ 7, 6, 5, 4, 3, 2, 1]-/ \n"
    player_number______ = "                   Player 1\n"
    spacing = "\n"
    player_pit_number__ = "pit number:  7  6  5  4  3  2  1  \n"
    spacing = "\n"
    selector_text______ = "Please select a pit number [0-6]: \n"

    expected_string = (
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
    capture_result = capsys.readouterr()
    expected_print_statement = capture_result.out
    assert expected_print_statement == expected_string

    terminal_show_board(
        board_state=BoardState(
            active=True,
            turn=PlayerNumber.TWO,
            player_one=Player(
                number=PlayerNumber.ONE, score=10, side=np.array([1, 2, 3, 4, 5, 6, 7])
            ),
            player_two=Player(
                number=PlayerNumber.TWO, score=5, side=np.array([1, 2, 3, 4, 5, 6, 7])
            ),
            n_turns=3,
        ),
        fixed_board=False,
    )
    pycongkak_string_____ = f"Pypycongkak@{metadata.version('pycongkak')} by Shaun Ho\n"
    spacing = "\n"
    turn_string________ = "Player 2's go, 3 turns remaining\n"
    spacing = "\n"
    opponent_pit_number = "pit number:  1  2  3  4  5  6  7  \n"
    spacing = "\n"
    opponent_number____ = "                   Player 1\n"
    opponent_side______ = "         /-[ 1, 2, 3, 4, 5, 6, 7]-\\  [10]\n"
    dividing_line______ = "        <-------------------------->\n"
    player_side________ = "   [05]  \\-[ 7, 6, 5, 4, 3, 2, 1]-/ \n"
    player_number______ = "                   Player 2\n"
    spacing = "\n"
    player_pit_number__ = "pit number:  7  6  5  4  3  2  1  \n"
    spacing = "\n"
    selector_text______ = "Please select a pit number [0-6]: \n"

    expected_string = (
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
    capture_result = capsys.readouterr()
    expected_print_statement = capture_result.out
    assert expected_print_statement == expected_string
