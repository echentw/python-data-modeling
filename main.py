from typing import List

from card import Card
from deck import Deck
from game import Game
from player import Player
from table import Table
from event import PlayerJoin, Bet, Event
from misc import Blinds, Error

def main():
    rank = Card.Rank.TWO
    card = Card(Card.Rank.TWO, Card.Suit.SPADES)
    deck = Deck()
    player = Player('eric')

    blinds = Blinds(2, 5, 0)
    game = Game(blinds)

    print(rank)
    print([card])
    print(deck)

    print(game)

    events: List[Event] = [
        PlayerJoin(player, Table.Seat.THREE, 500),
        Bet(player, 200),
    ]

    for event in events:
        try:
            game.receive(event)
        except Error as e:
            print(f'game failed to handle event because {e}')
        except e:
            raise e


if __name__ == '__main__':
    main()


