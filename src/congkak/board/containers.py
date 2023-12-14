from __future__ import annotations

import dataclasses
import enum

import numpy as np
import numpy.typing as npt
import pydantic


class PlayerNumber(enum.IntEnum):
    ONE = 1
    TWO = 2


@dataclasses.dataclass(frozen=True)
class Player:
    number: PlayerNumber
    score: int
    side: npt.NDArray[np.int32]

    def to_validator(self) -> PlayerValidator:
        return PlayerValidator(
            number=self.number, score=self.score, side=self.side.tolist()
        )


class PlayerValidator(pydantic.BaseModel):
    number: PlayerNumber
    score: int
    side: list[int]

    def to_player(self) -> Player:
        return Player(
            number=self.number,
            score=self.score,
            side=np.array(self.side, dtype=np.int32),
        )


@dataclasses.dataclass(frozen=True)
class BoardState:
    active: bool
    turn: PlayerNumber | None
    player_one: Player
    player_two: Player
    n_turns: int = 1

    def to_validator(self) -> BoardStateValidator:
        return BoardStateValidator(
            active=self.active,
            turn=self.turn if self.turn is not None else None,
            player_one=self.player_one.to_validator(),
            player_two=self.player_two.to_validator(),
            n_turns=self.n_turns,
        )

    @staticmethod
    def validate_json(json_for_validation: str) -> BoardState:
        return BoardStateValidator.model_validate_json(
            json_for_validation
        ).to_board_state()


class BoardStateValidator(pydantic.BaseModel):
    active: bool
    turn: PlayerNumber | None
    player_one: PlayerValidator
    player_two: PlayerValidator
    n_turns: int = 1

    def to_board_state(self) -> BoardState:
        return BoardState(
            active=self.active,
            turn=self.turn if self.turn is not None else None,
            player_one=self.player_one.to_player(),
            player_two=self.player_two.to_player(),
            n_turns=self.n_turns,
        )


@dataclasses.dataclass()
class GameData:
    concluded: bool
    rounds: int
    player_one: Player
    player_two: Player


@dataclasses.dataclass
class GameStatistics:
    winner: Player | None
    margin: int


@enum.unique
class CustomGameScenarios(enum.Enum):
    NORMAL = enum.auto()
    MOVE = enum.auto()
    FREE_GO = enum.auto()
    STEAL = enum.auto()
    LOSE_GO = enum.auto()
    SCENARIO_1 = enum.auto()
