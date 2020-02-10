from enum import Enum, unique


class Card:
    @unique
    class Rank(Enum):
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        TEN = 10
        JACK = 11
        QUEEN = 12
        KING = 13
        ACE = 14

        def __repr__(self):
            if self.value < 11:
                return str(self.value)
            else:
              return {
                11: 'jack',
                12: 'queen',
                13: 'king',
                14: 'ace',
                }[self.value]

        def __str__(self):
            return self.__repr__()


    @unique
    class Suit(Enum):
        SPADES = 'spades'
        HEARTS = 'hearts'
        CLUBS = 'clubs'
        DIAMONDS = 'diamonds'

        def __repr__(self):
            return self.value

        def __str__(self):
            return self.__repr__()

    rank: Rank
    suit: Suit

    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f'{self.rank} of {self.suit}'

    def __str__(self):
        return self.__repr__()
