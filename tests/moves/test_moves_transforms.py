import numpy as np
import pytest
from congkak.board.containers import BoardState, Player, PlayerNumber
from congkak.moves.containers import MoveValidity, PlayerMove
from congkak.moves.transforms import check_move_validity, move


def test_check_valid_move(
    board_state_example: BoardState,
) -> None:
    move_validity = check_move_validity(
        board_state=board_state_example,
        player_move=PlayerMove(player_number=PlayerNumber.ONE, pit_number=1),
    )
    assert move_validity == MoveValidity.VALID


def test_check_invalid_player(
    board_state_example: BoardState,
) -> None:
    move_validity = check_move_validity(
        board_state=board_state_example,
        player_move=PlayerMove(player_number=PlayerNumber.TWO, pit_number=0),
    )
    assert move_validity == MoveValidity.PLAYER


def test_check_invalid_pit(
    board_state_example: BoardState,
) -> None:
    move_validity = check_move_validity(
        board_state=board_state_example,
        player_move=PlayerMove(player_number=PlayerNumber.ONE, pit_number=0),
    )
    assert move_validity == MoveValidity.PIT


@pytest.mark.parametrize(
    "initial_board_state, player_move, expected_board_state",
    [
        (
            BoardState(
                active=True,
                turn=PlayerNumber.ONE,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=0,
                    side=np.array([1, 1, 0, 0, 0, 0, 0]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=0,
                    side=np.array([0, 0, 0, 0, 0, 0, 0]),
                ),
            ),
            PlayerMove(player_number=PlayerNumber.ONE, pit_number=0),
            BoardState(
                active=True,
                turn=PlayerNumber.TWO,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=0,
                    side=np.array([0, 2, 0, 0, 0, 0, 0]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=0,
                    side=np.array([0, 0, 0, 0, 0, 0, 0]),
                ),
            ),
        ),
        (
            BoardState(
                active=True,
                turn=PlayerNumber.ONE,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=0,
                    side=np.array([5, 1, 0, 0, 0, 0, 0]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=0,
                    side=np.array([0, 0, 0, 0, 0, 0, 0]),
                ),
            ),
            PlayerMove(player_number=PlayerNumber.ONE, pit_number=0),
            BoardState(
                active=True,
                turn=PlayerNumber.TWO,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=0,
                    side=np.array([0, 2, 1, 1, 1, 1, 0]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=0,
                    side=np.array([0, 0, 0, 0, 0, 0, 0]),
                ),
            ),
        ),
    ],
)
def test_move_normal(
    initial_board_state: BoardState,
    player_move: PlayerMove,
    expected_board_state: BoardState,
) -> None:
    new_board_state = move(board_state=initial_board_state, player_move=player_move)

    assert new_board_state.turn == expected_board_state.turn
    assert np.all(
        new_board_state.player_one.side == expected_board_state.player_one.side
    )
    assert np.all(
        new_board_state.player_two.side == expected_board_state.player_two.side
    )


@pytest.mark.parametrize(
    "initial_board_state, player_move, expected_board_state",
    [
        (
            BoardState(
                active=True,
                turn=PlayerNumber.ONE,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=0,
                    side=np.array([0, 0, 0, 0, 0, 3, 1]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=0,
                    side=np.array([0, 0, 0, 0, 0, 0, 0]),
                ),
            ),
            PlayerMove(player_number=PlayerNumber.ONE, pit_number=5),
            BoardState(
                active=True,
                turn=PlayerNumber.TWO,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=1,
                    side=np.array([0, 0, 0, 0, 0, 0, 2]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=0,
                    side=np.array([1, 0, 0, 0, 0, 0, 0]),
                ),
            ),
        ),
        (
            BoardState(
                active=True,
                turn=PlayerNumber.ONE,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=0,
                    side=np.array([8, 0, 0, 0, 0, 0, 0]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=0,
                    side=np.array([0, 0, 0, 0, 0, 0, 0]),
                ),
            ),
            PlayerMove(player_number=PlayerNumber.ONE, pit_number=0),
            BoardState(
                active=True,
                turn=PlayerNumber.TWO,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=1,
                    side=np.array([0, 1, 1, 1, 1, 1, 1]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=0,
                    side=np.array([1, 0, 0, 0, 0, 0, 0]),
                ),
            ),
        ),
        (
            BoardState(
                active=True,
                turn=PlayerNumber.ONE,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=0,
                    side=np.array([14, 4, 2, 3, 4, 5, 7]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=0,
                    side=np.array([0, 0, 0, 0, 0, 0, 0]),
                ),
            ),
            PlayerMove(player_number=PlayerNumber.ONE, pit_number=0),
            BoardState(
                active=True,
                turn=PlayerNumber.TWO,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=1,
                    side=np.array([0, 5, 3, 4, 5, 6, 8]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=0,
                    side=np.array([1, 1, 1, 1, 1, 1, 1]),
                ),
            ),
        ),
        (
            BoardState(
                active=True,
                turn=PlayerNumber.ONE,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=0,
                    side=np.array([16, 4, 2, 3, 4, 5, 7]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=0,
                    side=np.array([0, 0, 0, 0, 0, 0, 0]),
                ),
            ),
            PlayerMove(player_number=PlayerNumber.ONE, pit_number=0),
            BoardState(
                active=True,
                turn=PlayerNumber.TWO,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=1,
                    side=np.array([1, 6, 3, 4, 5, 6, 8]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=0,
                    side=np.array([1, 1, 1, 1, 1, 1, 1]),
                ),
            ),
        ),
        (
            BoardState(
                active=True,
                turn=PlayerNumber.ONE,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=0,
                    side=np.array([23, 1, 1, 1, 1, 1, 1]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=0,
                    side=np.array([0, 0, 0, 0, 0, 0, 0]),
                ),
            ),
            PlayerMove(player_number=PlayerNumber.ONE, pit_number=0),
            BoardState(
                active=True,
                turn=PlayerNumber.TWO,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=2,
                    side=np.array([1, 3, 3, 3, 3, 3, 3]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=0,
                    side=np.array([2, 1, 1, 1, 1, 1, 1]),
                ),
            ),
        ),
    ],
)
def test_move_score(
    initial_board_state: BoardState,
    player_move: PlayerMove,
    expected_board_state: BoardState,
) -> None:
    new_board_state = move(board_state=initial_board_state, player_move=player_move)

    assert new_board_state.turn == expected_board_state.turn
    assert np.all(
        new_board_state.player_one.side == expected_board_state.player_one.side
    )
    assert np.all(
        new_board_state.player_two.side == expected_board_state.player_two.side
    )
    assert new_board_state.player_one.score == expected_board_state.player_one.score
    assert new_board_state.player_two.score == expected_board_state.player_two.score


@pytest.mark.parametrize(
    "initial_board_state, player_move, expected_board_state",
    [
        (
            BoardState(
                active=True,
                turn=PlayerNumber.ONE,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=0,
                    side=np.array([0, 0, 0, 0, 0, 2, 1]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=0,
                    side=np.array([0, 0, 0, 0, 0, 0, 0]),
                ),
            ),
            PlayerMove(player_number=PlayerNumber.ONE, pit_number=5),
            BoardState(
                active=True,
                turn=PlayerNumber.ONE,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=1,
                    side=np.array([0, 0, 0, 0, 0, 0, 2]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=0,
                    side=np.array([0, 0, 0, 0, 0, 0, 0]),
                ),
            ),
        ),
        (
            BoardState(
                active=True,
                turn=PlayerNumber.ONE,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=0,
                    side=np.array([7, 1, 2, 3, 4, 5, 6]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=0,
                    side=np.array([1, 2, 3, 4, 5, 6, 7]),
                ),
            ),
            PlayerMove(player_number=PlayerNumber.ONE, pit_number=0),
            BoardState(
                active=True,
                turn=PlayerNumber.ONE,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=1,
                    side=np.array([0, 2, 3, 4, 5, 6, 7]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=0,
                    side=np.array([1, 2, 3, 4, 5, 6, 7]),
                ),
            ),
        ),
        (
            BoardState(
                active=True,
                turn=PlayerNumber.TWO,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=1,
                    side=np.array([7, 1, 2, 3, 4, 5, 6]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=0,
                    side=np.array([1, 2, 3, 4, 5, 6, 7]),
                ),
            ),
            PlayerMove(player_number=PlayerNumber.TWO, pit_number=3),
            BoardState(
                active=True,
                turn=PlayerNumber.TWO,
                player_one=Player(
                    number=PlayerNumber.ONE,
                    score=1,
                    side=np.array([7, 1, 2, 3, 4, 5, 6]),
                ),
                player_two=Player(
                    number=PlayerNumber.TWO,
                    score=1,
                    side=np.array([1, 2, 3, 0, 6, 7, 8]),
                ),
            ),
        ),
    ],
)
def test_move_free_go(
    initial_board_state: BoardState,
    player_move: PlayerMove,
    expected_board_state: BoardState,
) -> None:
    new_board_state = move(board_state=initial_board_state, player_move=player_move)

    assert new_board_state.turn == expected_board_state.turn
    assert np.all(
        new_board_state.player_one.side == expected_board_state.player_one.side
    )
    assert np.all(
        new_board_state.player_two.side == expected_board_state.player_two.side
    )
    assert new_board_state.player_one.score == expected_board_state.player_one.score
    assert new_board_state.player_two.score == expected_board_state.player_two.score
