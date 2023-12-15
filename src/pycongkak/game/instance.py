from pycongkak.board.containers import GameStatistics
from pycongkak.board.transforms import (
    check_victory,
    check_winner,
    end_game,
    start_game,
)
from pycongkak.game.display import terminal_show_board
from pycongkak.moves.transforms import move


def run_pycongkak() -> GameStatistics:
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
        terminal_show_board(board_state, fixed_board=fixed_board)
        pit_number = int(input())
        board_state = move(board_state=board_state, pit_number=pit_number)

        game_history.append(board_state)
        victory = check_victory(board_state)
        if victory:
            game_statistics = check_winner(board_state)
            board_state = end_game(board_state)
    return game_statistics


if __name__ == "__main__":
    run_pycongkak()
