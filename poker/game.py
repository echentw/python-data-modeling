from table import Table
from event import (
    Event,
    TableEvent,
    PlayerJoin,
    PlayerLeave,
    PlayerAction,
    Fold,
    Check,
    Call,
    Bet,
    Raise
)
from misc import ChipAmount, Blinds, Error


class Game:
    blinds: Blinds
    table: Table

    def __init__(self, blinds: Blinds):
        self.blinds = blinds
        self.table = Table()

    def receive(self, event: Event):
        if isinstance(event, TableEvent):
            self.handleTableEvent(event)
        elif isinstance(event, PlayerAction):
            self.handlePlayerAction(event)
        else:
            raise Error(f'unknown Event: {event}')

    def handleTableEvent(self, event: TableEvent):
        if isinstance(event, PlayerJoin):
            self.table.player_join(event.player, event.seat, event.buyin)
        elif isinstance(event, PlayerLeave):
            self.table.player_leave(event.player)
        else:
            raise Error(f'unknown TableEvent: {event}')

    def handlePlayerAction(self, action: PlayerAction):
        raise Error(f'unknown PlayerAction: {action}')

    def __repr__(self):
        return f'{{blinds: {self.blinds}, table: {self.table}}}'

    def __str__(self):
        return self.__repr__()