from player import Player
from table import Table
from misc import ChipAmount


class Event:
    pass


class TableEvent(Event):
    pass


class PlayerJoin(TableEvent):
    player: Player
    seat: Table.Seat
    buyin: ChipAmount

    def __init__(self, player: Player, seat: Table.Seat, buyin: ChipAmount):
        self.player = player
        self.seat = seat
        self.buyin = buyin


class PlayerLeave(TableEvent):
    player: Player

    def __init__(self, player: Player):
        self.player = player


class PlayerAction(Event):
    pass


class Fold(PlayerAction):
    player: Player

    def __init__(self, player: Player):
        self.player = player


class Check(PlayerAction):
    player: Player

    def __init__(self, player: Player):
        self.player = player


class Call(PlayerAction):
    player: Player

    def __init__(self, player: Player):
        self.player = player


class Bet(PlayerAction):
    player: Player
    amount: ChipAmount

    def __init__(self, player: Player, amount: ChipAmount):
        self.player = player
        self.amount = amount


class Raise(PlayerAction):
    player: Player
    to_amount: ChipAmount

    def __init__(self, player: Player, to_amount: ChipAmount):
        self.player = player
        self.to_amount = to_amount