import pytest
from pycongkak.board.containers import PlayerNumber
from pycongkak.moves.containers import PlayerMove


def test_player_move() -> None:
    valid_move = PlayerMove(player_number=PlayerNumber.ONE, pit_number=0)
    assert valid_move.pit_number == 0
    with pytest.raises(ValueError):
        _invalid_move = PlayerMove(player_number=PlayerNumber.ONE, pit_number=7)
