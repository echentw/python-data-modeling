from typing import List

from card import Card


class Deck:
    cards: List[Card]

    def __init__(self):
        self.cards = []
        for suit in Card.Suit:
            for rank in Card.Rank:
                self.cards.append(Card(rank, suit))

    def draw(self) -> Card:
        return self.cards.pop()

    def __repr__(self):
        return repr(self.cards)

    def __str__(self):
        return self.__repr__()
