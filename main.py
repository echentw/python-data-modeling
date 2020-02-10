from card import Card
from deck import Deck
from game import Game
from player import Player
from table import Table
from event import PlayerJoinEvent
from misc import Blinds

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
game.receive(PlayerJoinEvent(player, Table.Seat.THREE, 500))
print(game)
