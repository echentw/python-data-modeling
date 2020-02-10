class Player:
    identifier: str

    def __init__(self, identifier: str):
        self.identifier = identifier

    def __repr__(self):
        return self.identifier

    def __str__(self):
        return self.__repr__()
