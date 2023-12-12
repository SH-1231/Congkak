from congkak.board.containers import GameStatistics
from congkak.board.transforms import start_game, check_victory, check_winner, end_game, check_winner
from congkak.moves.transforms import move
from congkak.moves.containers import PlayerMove


def run_congkak()->GameStatistics:
    board_state = start_game()
    game_history = [board_state]
    while board_state.active:
        pit_number = input(f"Player {board_state.turn}'s Go. Please select a pit (0-6):")
        board_state = move(
            board_state=board_state,
            player_move=PlayerMove(
                player_number=board_state.turn,
                pit_number=pit_number
            )
        )
        game_history.append(board_state)
        victory = check_victory(board_state)
        if victory:
            game_statistics = check_winner(board_state)
            board_state = end_game(board_state)
    return game_statistics
        