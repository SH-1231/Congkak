from congkak.board.containers import GameStatistics
from congkak.board.transforms import (
    check_victory,
    check_winner,
    end_game,
    start_game,
)
from congkak.game.display import terminal_show_board
from congkak.moves.containers import PlayerMove
from congkak.moves.transforms import move


def run_congkak() -> GameStatistics:
    board_state = start_game()
    game_history = [board_state]
    while board_state.active:
        terminal_show_board(board_state)
        pit_number = int(input())
        board_state = move(
            board_state=board_state,
            player_move=PlayerMove(
                player_number=board_state.turn, pit_number=pit_number
            ),
        )
        game_history.append(board_state)
        victory = check_victory(board_state)
        if victory:
            game_statistics = check_winner(board_state)
            board_state = end_game(board_state)
    return game_statistics


if __name__ == "__main__":
    run_congkak()
