from congkak.board.containers import GameStatistics
from congkak.board.transforms import (
    check_victory,
    check_winner,
    end_game,
    start_game,
)
from congkak.game.custom_scenarios import CustomGameScenario
from congkak.moves.containers import PlayerMove
from congkak.moves.transforms import move


def run_congkak(
    custom_game_scenario: CustomGameScenario = CustomGameScenario.NORMAL,
) -> GameStatistics:
    board_state = start_game(custom_game_scenario=custom_game_scenario)
    game_history = [board_state]
    while board_state.active:
        pit_number = int(
            input(f"Player {board_state.turn}'s Go. Please select a pit (0-6):")
        )
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
