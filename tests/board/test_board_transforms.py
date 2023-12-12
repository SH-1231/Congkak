from congkak.board.transforms import start_game, end_game, check_victory, check_winner, active_player_side
from congkak.board.containers import BoardState, Player, PlayerNumber
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

def test_check_winner(
    player_one_win_board_state: BoardState,
    player_two_win_board_state: BoardState
)->None:
    player_one_win = check_winner(player_one_win_board_state)
    player_two_win = check_winner(player_two_win_board_state)

    assert player_one_win.winner.number == PlayerNumber.ONE
    assert player_one_win.margin > 0
    assert player_two_win.winner.number == PlayerNumber.TWO
    assert player_two_win.margin > 0

def test_side_from_player_move(
    board_state_example: BoardState,
)->None:
    assert np.all(active_player_side(board_state_example, PlayerNumber.ONE) == board_state_example.side_one)
    assert np.all(active_player_side(board_state_example, PlayerNumber.TWO) == board_state_example.side_two)