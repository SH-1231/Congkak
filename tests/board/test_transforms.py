from congkak.board.transforms import start_game, player_move
from congkak.board.containers import BoardState
import numpy as np

def test_start_game()->None:
    game = start_game()
    assert game.active is True
    assert np.all(game.side_one) == 0
    assert np.all(game.side_two) == 0
    assert game.player_one.score == 0
    assert game.player_two.score == 0
