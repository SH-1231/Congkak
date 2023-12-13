import numpy as np
import copy

from congkak.board.containers import BoardState, PlayerNumber, Player
from congkak.moves.containers import PlayerMove, MoveValidity, BoardPerspective
from congkak.board.transforms import active_player, opponent_player
from congkak.board.constants import PITS_PER_SIDE
import itertools

def check_move_validity(
    board_state: BoardState,
    player_move: PlayerMove,
)->MoveValidity:
    player = active_player(board_state)
    if player_move.player_number != board_state.turn:
        return MoveValidity.PLAYER
    elif player.side[player_move.pit_number] < 1:
        return MoveValidity.PIT
    else:
        return MoveValidity.VALID

def move(
    board_state: BoardState,
    player_move: PlayerMove,
)->BoardState:
    selected_pit = player_move.pit_number

    player = copy.deepcopy(active_player(board_state))
    opponent = copy.deepcopy(opponent_player(board_state))
    
    
    initial_number = player.side[selected_pit]
    initial_score_mapping = {
        BoardPerspective.PLAYER: player.score,
        BoardPerspective.OPPONENT: opponent.score
    }
    score = 0

    mapping:dict[int, Player] = {
    }
    board_sides = itertools.cycle([
        (BoardPerspective.PLAYER, player.side),
        (BoardPerspective.OPPONENT, opponent.side)
    ])
    

    # set selected pit = 0, taking marbles from this pit
    player.side[selected_pit] = 0
    mapping[BoardPerspective.PLAYER] = player
    mapping[BoardPerspective.OPPONENT] = opponent

    start_pit = selected_pit + 1
    spaces_to_end = PITS_PER_SIDE - start_pit
    overflow = initial_number - spaces_to_end
    
    while overflow >= 0:
        side_enum, side_player = next(board_sides)
        if side_enum == BoardPerspective.PLAYER:
            score += 1
            overflow -= 1
        additional = np.zeros(PITS_PER_SIDE, dtype=np.int32)
        additional[start_pit: ] = 1
        side_player += additional

        # resetting new values for loop
        start_pit = 0
        overflow -= PITS_PER_SIDE
        initial_number = PITS_PER_SIDE + overflow


        # saving data
        mapping[side_enum] = Player(
            number=mapping[side_enum].number,
            score=initial_score_mapping[side_enum],
            side=side_player
        )
        
    side_enum, side_player = next(board_sides)
    additional = np.zeros(PITS_PER_SIDE, dtype=np.int32)
    end_pit = PITS_PER_SIDE - 1 if overflow>0 else start_pit + initial_number
    additional[start_pit: end_pit] = 1
    side_player += additional
    mapping[side_enum] = Player(
        number=mapping[side_enum].number,
        score=initial_score_mapping[side_enum],
        side=side_player
    )

    for enum_n, player_n in mapping.items():
        if player_n.number == player.number:
            updated_player_n = add_score(player_n.number, score, player_n)
        else:
            updated_player_n = player_n
        mapping[enum_n] = updated_player_n
    
    if player.number == PlayerNumber.ONE:
        player_one = mapping[BoardPerspective.PLAYER]
        player_two = mapping[BoardPerspective.OPPONENT]
    else:
        player_one = mapping[BoardPerspective.OPPONENT]
        player_two = mapping[BoardPerspective.PLAYER]

    return BoardState(
        active=True,
        turn=opponent.number,
        player_one=player_one,
        player_two=player_two
    )

def add_score(
    player_number: PlayerNumber,
    score: int,
    player: Player,
)->Player:
    return Player(
        number=player.number,
        score=player.score + score,
        side=player.side

    )

def steal()->BoardState:
    pass
def free()->BoardState:
    pass
def miss()->BoardState:
    pass