from unittest import TestCase

import numpy as np

from game import Board


class TestBoard(TestCase):
    def setUp(self):
        self.width, self.height = 6, 5
        self.board = Board(self.width, self.height)

    def test_init(self):
        width, height = 6, 7
        expected = np.zeros((7, 6))
        board = Board(width, height)
        np.testing.assert_array_equal(board.state, expected)

    def test_width(self):
        self.assertEqual(self.width, self.board.width)

    def test_height(self):
        self.assertEqual(self.height, self.board.height)

    def test_state(self):
        np.testing.assert_array_equal(self.board.state, np.zeros((self.height, self.width)))

    def test_set_state(self):
        self.board.set_state(0, 0, True)
        self.board.set_state(1, 2, True)
        expected = np.zeros((self.height, self.width))
        expected[0, 0] = 1
        expected[2, 1] = 1
        np.testing.assert_array_equal(self.board.state, expected)

    def test_alive_neighbours(self):
        self.board.set_state(0, 0, True)
        self.board.set_state(1, 0, True)
        self.board.set_state(3, 2, True)
        self.board.set_state(2, 2, True)
        self.assertEqual(3, self.board._alive_neighbours(1, 1))

    def test_count_neighbours(self):
        self.board.set_state(0, 0, True)
        self.board.set_state(1, 0, True)
        self.board.set_state(3, 2, True)
        self.board.set_state(2, 2, True)

        expected = np.array([[1, 1, 1, 0, 0, 0],
                             [2, 3, 3, 2, 1, 0],
                             [0, 1, 1, 1, 1, 0],
                             [0, 1, 2, 2, 1, 0],
                             [0, 0, 0, 0, 0, 0]])
        np.testing.assert_array_equal(self.board._count_neighbours(), expected)

    def test_generation_step(self):
        self.board.set_state(0, 0, True)
        self.board.set_state(1, 0, True)
        self.board.set_state(3, 2, True)
        self.board.set_state(2, 2, True)
        expected = np.array([[0, 0, 0, 0, 0, 0],
                             [0, 1, 1, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0]])
        self.board.generation_step()
        np.testing.assert_array_equal(self.board.state, expected)

    def test_repr(self):
        expected = '◽ ◽ ◽ ◽ ◽ ◽\n◽ ◽ ◽ ◽ ◽ ◽\n◽ ◽ ◽ ◽ ◽ ◽\n◽ ◽ ◽ ◽ ◽ ◽\n◽ ◽ ◽ ◽ ◽ ◽'
        self.assertEqual(str(self.board), expected)
