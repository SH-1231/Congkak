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
    
    mapping = {
        BoardPerspective.PLAYER: player,
        BoardPerspective.OPPONENT: opponent
    }

    board_sides = itertools.cycle([
        (BoardPerspective.PLAYER, np.zeros(player.side.shape)),
        (BoardPerspective.OPPONENT, np.zeros(opponent.side.shape))
    ])
    

    # set selected pit = 0, taking marbles from this pit
    player.side[selected_pit] = 0
    mapping[BoardPerspective.PLAYER] = player

    start_pit = selected_pit + 1
    spaces_to_end = PITS_PER_SIDE - start_pit
    overflow = initial_number - spaces_to_end
    
    while overflow >= 0:
        side_enum, side_player = next(board_sides)
        additional = np.zeros(PITS_PER_SIDE)
        additional[start_pit+1: ] = 1
        start_pit = 0
        overflow -= PITS_PER_SIDE
        
    side_enum, side_player = next(board_sides)
    additional = np.zeros(PITS_PER_SIDE)
    end_pit = PITS_PER_SIDE - 1 if overflow>0 else start_pit + initial_number
    additional[start_pit: end_pit] = 1
    side_player += additional
    mapping[side_enum] = Player(
        number=None,
        score=0,
        side=mapping[side_enum].side + side_player
    )
    
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

def steal()->BoardState:
    pass
def free()->BoardState:
    pass
def miss()->BoardState:
    pass