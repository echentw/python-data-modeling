from player import Player
from table import Table
from misc import ChipAmount

class Event:
    pass


class PlayerJoinEvent(Event):
    player: Player
    seat: Table.Seat
    buyin: ChipAmount

    def __init__(self, player: Player, seat: Table.Seat, buyin: ChipAmount):
        self.player = player
        self.seat = seat
        self.buyin = buyin


class PlayerLeaveEvent(Event):
    player: Player

    def __init__(self, player: Player):
        self.player = player
