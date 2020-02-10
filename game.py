from table import Table
from event import (
    Event,
    PlayerJoinEvent,
    PlayerLeaveEvent
)
from misc import ChipAmount, Blinds


class Game:
    blinds: Blinds
    table: Table

    def __init__(self, blinds: Blinds):
        self.blinds = blinds
        self.table = Table()

    def receive(self, event: Event):
        if isinstance(event, PlayerJoinEvent):
            self.table.player_join(event.player, event.seat, event.buyin)
        elif isinstance(event, PlayerLeaveEvent):
            self.table.player_leave(event.player)
        else:
            # TODO: raise exception
            pass

    def __repr__(self):
        return f'{{blinds: {self.blinds}, table: {self.table}}}'

    def __str__(self):
        return self.__repr__()
