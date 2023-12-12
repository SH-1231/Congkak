from congkak.board.transforms import start_game, end_game, check_victory
from congkak.board.containers import BoardState
import numpy as np

def test_start_game()->None:
    game = start_game()
    assert game.active is True
    assert np.all(game.side_one) == 0
    assert np.all(game.side_two) == 0
    assert game.player_one.score == 0
    assert game.player_two.score == 0

def test_end_game(
        board_state_example: BoardState
    )->None:
    non_active_board = end_game(board_state_example)
    assert non_active_board.active is False

def test_check_victory(
    board_state_example: BoardState,
    board_state_endgame_example:BoardState
)->None:
    game_ended_false = check_victory(board_state_example)
    game_ended_true = check_victory(board_state_endgame_example)
    assert game_ended_false is False
    assert game_ended_true is True