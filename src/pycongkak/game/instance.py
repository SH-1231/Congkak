from pycongkak.board.transforms import (
    check_victory,
    check_winner,
    end_game,
    start_game,
)
from pycongkak.game.display import (
    PYCONGKAK_DISPLAY_STRING,
    terminal_show_board,
    terminal_show_victory,
)
from pycongkak.moves.containers import MoveValidity
from pycongkak.moves.transforms import check_move_validity, move


def run_pycongkak() -> None:
    print(PYCONGKAK_DISPLAY_STRING)
    fixed_board_input = input("Run Pypycongkak with fixed board? (yes/no) [yes]")
    match fixed_board_input:
        case "yes":
            fixed_board = True
        case "no":
            fixed_board = False
        case _:
            fixed_board = True
    board_state = start_game()
    game_history = [board_state]
    while board_state.active:
        invalid_string = True
        print_invalid = False
        while invalid_string:
            terminal_show_board(board_state, fixed_board=fixed_board)
            invalid_print = "Invalid Pit Selected" if print_invalid is True else ""
            selector_text = (
                "Please select a pit number [1-7], or enter 'quit' to quit: "
            )
            print(invalid_print)
            print(selector_text)
            user_input = input()
            if user_input == "quit":
                exit()
            else:
                pit_number = int(user_input) - 1

                match check_move_validity(board_state, pit_number):
                    case MoveValidity.VALID:
                        invalid_string = False
                        print_invalid = False
                    case _:
                        invalid_string = True
                        print_invalid = True

        board_state = move(board_state=board_state, pit_number=pit_number)

        game_history.append(board_state)
        victory = check_victory(board_state)
        if victory:
            game_statistics = check_winner(board_state)
            board_state = end_game(board_state)
            terminal_show_victory(game_statistics)
