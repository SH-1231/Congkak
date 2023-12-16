from importlib import metadata

import numpy as np
import pytest
from pycongkak.board.containers import BoardState, GameStatistics, Player, PlayerNumber
from pycongkak.game.display import (
    int_to_string_with_min_spacing,
    terminal_show_board,
    terminal_show_victory,
)

pycongkak_string = f"Pypycongkak@{metadata.version('pycongkak')} by Shaun Ho\n"


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
    spacing = "\n"
    turn_string = "Player 1's go, 3 turns remaining\n"
    spacing = "\n"
    opponent_pit_number = "pit number:  1  2  3  4  5  6  7  \n"
    spacing = "\n"
    opponent_number = "                   Player 2\n"
    opponent_side = "         /-[ 1, 2, 3, 4, 5, 6, 7]-\\  [05]\n"
    dividing_line = "        <-------------------------->\n"
    player_side = "   [10]  \\-[ 7, 6, 5, 4, 3, 2, 1]-/ \n"
    player_number = "                   Player 1\n"
    spacing = "\n"
    player_pit_number = "pit number:  7  6  5  4  3  2  1  \n"
    spacing = "\n"
    selector_text = "Please select a pit number [0-6]: \n"

    expected_string = (
        pycongkak_string
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
        + spacing
        + selector_text
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
    pycongkak_string = f"Pypycongkak@{metadata.version('pycongkak')} by Shaun Ho\n"
    spacing = "\n"
    turn_string = "Player 2's go, 3 turns remaining\n"
    spacing = "\n"
    opponent_pit_number = "pit number:  1  2  3  4  5  6  7  \n"
    spacing = "\n"
    opponent_number = "                   Player 2\n"
    opponent_side = "         /-[ 1, 2, 3, 4, 5, 6, 7]-\\  [05]\n"
    dividing_line = "        <-------------------------->\n"
    player_side = "   [10]  \\-[ 7, 6, 5, 4, 3, 2, 1]-/ \n"
    player_number = "                   Player 1\n"
    spacing = "\n"
    player_pit_number = "pit number:  7  6  5  4  3  2  1  \n"
    spacing = "\n"
    selector_text = "Please select a pit number [0-6]: \n"

    expected_string = (
        pycongkak_string
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
        + spacing
        + selector_text
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
    pycongkak_string = f"Pypycongkak@{metadata.version('pycongkak')} by Shaun Ho\n"
    spacing = "\n"
    turn_string = "Player 2's go, 3 turns remaining\n"
    spacing = "\n"
    opponent_pit_number = "pit number:  1  2  3  4  5  6  7  \n"
    spacing = "\n"
    opponent_number = "                   Player 1\n"
    opponent_side = "         /-[ 1, 2, 3, 4, 5, 6, 7]-\\  [10]\n"
    dividing_line = "        <-------------------------->\n"
    player_side = "   [05]  \\-[ 7, 6, 5, 4, 3, 2, 1]-/ \n"
    player_number = "                   Player 2\n"
    spacing = "\n"
    player_pit_number = "pit number:  7  6  5  4  3  2  1  \n"
    spacing = "\n"
    selector_text = "Please select a pit number [0-6]: \n"

    expected_string = (
        pycongkak_string
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
        + spacing
        + selector_text
    )
    capture_result = capsys.readouterr()
    expected_print_statement = capture_result.out
    assert expected_print_statement == expected_string


def test_terminal_show_victory(capsys: pytest.CaptureFixture) -> None:
    game_stats = GameStatistics(
        winner=Player(
            number=PlayerNumber.ONE, score=10, side=np.array([0, 0, 0, 0, 0, 0, 0])
        ),
        player_one=Player(
            number=PlayerNumber.ONE, score=10, side=np.array([0, 0, 0, 0, 0, 0, 0])
        ),
        player_two=Player(
            number=PlayerNumber.TWO, score=1, side=np.array([0, 0, 0, 0, 0, 0, 0])
        ),
        margin=10,
    )

    terminal_show_victory(game_stats)
    capture_result = capsys.readouterr()
    expected_print_statement = capture_result.out
    game_ended_string = "<-- Game Ended -->\n"
    winner_string_1 = "Winner: Player 1"
    winner_string_2 = ", scoring 10\n"

    expected_string = (
        pycongkak_string + game_ended_string + winner_string_1 + winner_string_2
    )
    assert expected_print_statement == expected_string


def test_terminal_show_draw(capsys: pytest.CaptureFixture) -> None:
    game_stats = GameStatistics(
        winner=None,
        player_one=Player(
            number=PlayerNumber.ONE, score=10, side=np.array([0, 0, 0, 0, 0, 0, 0])
        ),
        player_two=Player(
            number=PlayerNumber.TWO, score=10, side=np.array([0, 0, 0, 0, 0, 0, 0])
        ),
        margin=10,
    )

    terminal_show_victory(game_stats)
    capture_result = capsys.readouterr()
    expected_print_statement = capture_result.out
    game_ended_string = "<-- Game Ended -->\n"
    draw_string = "Draw: Both players scored 10 marbles\n"

    expected_string = pycongkak_string + game_ended_string + draw_string
    assert expected_print_statement == expected_string
