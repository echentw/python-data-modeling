ChipAmount = int

class Error(Exception):
    """Base class for exceptions in this project"""
    pass

class Blinds:
    small: ChipAmount
    big: ChipAmount
    ante: ChipAmount

    def __init__(self, small: ChipAmount, big: ChipAmount, ante: ChipAmount):
        self.small = small
        self.big = big
        self.ante = ante

    def __repr__(self):
        return f'(small: {self.small}, big: {self.big}, ante: {self.ante})'

    def __str__(self):
        return self.__repr__()
