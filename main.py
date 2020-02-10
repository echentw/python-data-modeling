from card import Card
from deck import Deck


rank = Card.Rank.TWO
card = Card(Card.Rank.TWO, Card.Suit.SPADES)
deck = Deck()

print(rank)
print([card])
print(deck)
