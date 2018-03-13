import json
from itertools import product
from time import sleep

import numpy as np


class Board:
    def __init__(self, board_width: int, board_height: int):
        self._board = np.zeros((board_height, board_width)).astype(np.bool)

    def start(self):
        generation = 1
        while True:
            try:
                # clear the screen
                print("\033[H\033[J")
                print('Generation: {}'.format(generation))
                print(self)
                self.generation_step()
                sleep(0.1)
                generation += 1
            except KeyboardInterrupt:
                self.serialize('state.json')
                print('Save state to state.json')
                break

    def generation_step(self):
        """
        Calculate live cells for next generation.
        Update current board
        """
        new_board = np.zeros(self._board.shape).astype(np.bool)
        neighbours_matrix = self._count_neighbours()

        new_board[np.where((neighbours_matrix == 2) & self._board)] = True
        new_board[np.where((neighbours_matrix == 3) & self._board)] = True
        new_board[np.where((neighbours_matrix == 3) & (self._board == False))] = True
        self._board = new_board

    def _count_neighbours(self) -> np.ndarray:
        """
        For each cell calculate number of surrounding neighbours
        """
        neighbours_matrix = np.empty((self.height, self.width), dtype=np.uint)

        all_coordinates = product(range(self.height), range(self.width))
        for y, x in all_coordinates:
            neighbours_matrix[y, x] = self._alive_neighbours(x, y)
        return neighbours_matrix

    def _alive_neighbours(self, x: int, y: int) -> int:
        """
        Count live neighbours for given cell
        """
        x1 = np.max([0, x - 1])
        x2 = np.min([x + 2, self.width])
        y1 = np.max([0, y - 1])
        y2 = np.min([y + 2, self.height])

        neighbours = np.sum(self._board[y1:y2, x1:x2]) - self._board[y, x]
        return neighbours

    def set_state(self, x: int, y: int, state: bool):
        self._board[y, x] = state

    def serialize(self, path: str):
        state_dict = {
            'shape': (self.width, self.height),
            'live_cells': np.argwhere(self._board == 1).tolist()
        }
        with open(path, 'w') as f:
            json.dump(state_dict, f)

    @classmethod
    def deserialize(cls, json_file: str):
        with open(json_file) as f:
            state_dict = json.load(f)

        board = cls(*state_dict['shape'])
        for y, x in state_dict['live_cells']:
            board.set_state(x, y, True)
        return board

    @property
    def height(self) -> int:
        return self._board.shape[0]

    @property
    def width(self) -> int:
        return self._board.shape[1]

    def __repr__(self):
        repr = []
        for row in self._board:
            row_repr = ' '.join(['◾' if col else '◽' for col in row])
            repr.append(row_repr)
        return '\n'.join(repr)


if __name__ == '__main__':
    while True:
        menu = """
Welcome to Game Of Life!
Select pattern to start a game:
[1] Random
[2] Glider
[3] Spaceship
Chose one of 1, 2, 3: """
        print(menu, end='')
        choice = input().strip()
        if choice in ('1', '2', '3'):
            break

    if choice == '1':
        width, height = 30, 30
        board = Board(width, height)
        [board.set_state(x, y, np.random.choice([True, False])) for x in range(width) for y in range(height)]
    elif choice == '2':
        board = Board.deserialize('glider.json')
    else:
        board = Board.deserialize('spaceship.json')
    board.start()
