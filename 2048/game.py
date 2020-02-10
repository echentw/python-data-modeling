from typing import List, Optional, Tuple
import random
from enum import Enum
import copy


class Block:
    value: int

    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return self.__repr__()

    def maybe_merge(self, other):
        if self.value == other.value:
            return Block(2 * self.value)
        else:
            return None


class Square:
    row: int
    col: int

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __repr__(self):
        return f'({self.row}, {self.col})'

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        return Square(self.row + other.row, self.col + other.col)


class Translation(Square):
    pass


class Direction(Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'

    def translation(self) -> Translation:
        if self == self.UP:
            return Translation(-1, 0)
        elif self == self.DOWN:
            return Translation(1, 0)
        elif self == self.LEFT:
            return Translation(0, -1)
        elif self == self.RIGHT:
            return Translation(0, 1)
        else:
            raise Exception(f'Unknown Direction: {self}')

    def opposite(self):
        if self == Direction.UP:
            return Direction.DOWN
        elif self == Direction.DOWN:
            return Direction.UP
        elif self == Direction.LEFT:
            return Direction.RIGHT
        elif self == Direction.RIGHT:
            return Direction.LEFT
        else:
            raise Exception(f'Unknown Direction: {self}')


class Error(Exception):
    pass


class Grid(List[List[Optional[Block]]]):
    def is_in_bounds(self, square: Square) -> bool:
        num_rows = len(self)
        num_cols = len(self[0])
        return (
            square.row >= 0 and
            square.col >= 0 and
            square.row < num_rows and
            square.col < num_cols
        )

    def get(self, square: Square) -> Optional[Block]:
        return self[square.row][square.col]

    def place_block(self, square: Square, block: Optional[Block]):
        self[square.row][square.col] = block

    def clear_square(self, square: Square):
        self.place_block(square, None)

    def is_occupied(self, square: Square) -> bool:
        if not self.is_in_bounds(square):
            return False
        return self.get(square) is not None


class Game:
    grid: Grid
    num_rows: int
    num_cols: int

    def __init__(self, num_rows: int, num_cols: int):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.grid = Grid([[None for _ in range(num_cols)] for _ in range(num_rows)])
        self.spawn_random_block()

    def handle_direction(self, direction: Direction):
        self.grid = self.get_new_grid_state(self.grid, direction)
        self.spawn_random_block()

    def get_new_grid_state(self, grid: Grid, direction: Direction) -> Grid:
        num_rows = len(grid)
        num_cols = len(grid[0])
        new_grid = copy.deepcopy(grid)

        iteration_order: Tuple[List[int], List[int]]

        if direction == Direction.UP:
            iteration_order = (list(range(num_rows)), list(range(num_cols)))
        elif direction == Direction.DOWN:
            iteration_order = (list(reversed(range(num_rows))), list(range(num_cols)))
        elif direction == Direction.LEFT:
            iteration_order = (list(range(num_rows)), list(range(num_cols)))
        elif direction == Direction.RIGHT:
            iteration_order = (list(range(num_rows)), list(reversed(range(num_cols))))
        else:
            raise Exception(f'Unknown Direction: {self}')

        for row in iteration_order[0]:
            for col in iteration_order[1]:
                self.maybe_slide_block(new_grid, Square(row, col), direction)

        return new_grid

    def maybe_slide_block(self, grid: Grid, square: Square, direction: Direction):
        moving_block = grid.get(square)
        grid.clear_square(square)

        if moving_block is None:
            return

        target_square = square + direction.translation()
        while grid.is_in_bounds(target_square) and not grid.is_occupied(target_square):
            target_square += direction.translation()

        if grid.is_occupied(target_square):
            target_block = grid.get(target_square)
            merged: Optional[Block] = moving_block.maybe_merge(target_block)
            if merged is not None:
                grid.place_block(target_square, merged)
                return

        target_square += direction.opposite().translation()
        grid.place_block(target_square, moving_block)

    def spawn_random_block(self):
        value = 2 if random.random() > 0.5 else 4
        square = self.get_random_empty_square()
        self.grid[square.row][square.col] = Block(value)

    def get_random_empty_square(self) -> Square:
        empty_squares = [
            Square(row, col)
            for row in range(self.num_rows)
            for col in range(self.num_cols)
            if self.grid[row][col] is None
        ]
        return random.choice(empty_squares)

    def __repr__(self):
        lines: List[str] = []
        for row in range(self.num_rows):
            line = '\t'.join([str(self.grid[row][col].value) if self.grid[row][col] is not None else '-' for col in range(self.num_cols)])
            lines.append(line)
        return '\n'.join(lines)

    def __str__(self):
        return self.__repr__()


def parse_input(user_input: str) -> Direction:
    direction = Direction(user_input)
    if direction is not None:
        return direction
    else:
        raise Error(f'Unable to parse "{user_input}" into a Direction"')


def main():
    game = Game(4, 4)
    print('------------------------------------')
    print(game)
    print('------------------------------------')

    user_input = input()

    while user_input != 'stop':
        direction = parse_input(user_input)
        game.handle_direction(direction)

        print('------------------------------------')
        print(game)
        print('------------------------------------')

        user_input = input()


if __name__ == '__main__':
    main()