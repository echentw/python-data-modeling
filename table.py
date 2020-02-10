from enum import Enum
from typing import Dict, Optional

from player import Player
from misc import ChipAmount


class Table:
    class Seat(Enum):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6

    seating: Dict[Seat, Optional[Player]]
    stacks: Dict[Player, ChipAmount]

    def __init__(self):
        self.seating = {}
        for seat in self.Seat:
            self.seating[seat] = None
        self.stacks = {}

    def player_join(self, player: Player, seat: Seat, buyin: ChipAmount):
        if self.seating[seat] is not None:
            # TODO: throw an exception
            pass
        else:
            self.seating[seat] = player
            self.stacks[player] = buyin

    def player_leave(self, player: Player):
        self.stacks.pop(player, None)
        for seat, seated_player in self.seating.items():
            if seated_player == player:
                self.seating[seat] = None
        # TODO: throw an exception if the player is not at the table

    def __repr__(self):
        table = [
            None if self.seating[seat] is None else (
                self.seating[seat],
                self.stacks[ self.seating[seat] ]
            )
            for seat in self.Seat
        ]
        return str(table)

    def __str__(self):
        return self.__repr__()
