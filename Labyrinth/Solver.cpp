//
// Created by Alexander Onbysh on 3/15/18.
//

#include "Solver.h"
using namespace std;

Board DFS(Board board, int x, int y) {
    // If access goes out of boundaries
    if (x < 0 | x > board.width() - 1 | y < 0 | y > board.height() - 1) {
        return board;
    }

    auto _x = static_cast<unsigned long>(x);
    auto _y = static_cast<unsigned long>(y);

    // Find max path in four directions
    if (board.isFree(_x, _y)) {
        board.set(_x, _y, static_cast<int>(board.getMaxPath() + 1));
        board.setMaxPath(board.getMaxPath() + 1);

        Board left_max = DFS(board, x - 1, y);
        Board right_max = DFS(board, x + 1, y);
        Board upper_max = DFS(board, x, y + 1);
        Board down_max = DFS(board, x, y - 1);

        return max(max(left_max, right_max), max(upper_max, down_max));
    }
    return board;
}

Board solve(Board board) {
    Board max_path = board;

    for (unsigned int x = 0; x < board.width(); x++) {
        for (unsigned int y = 0; y < board.height(); y++) {
            if (x == 0 | y == 0 | x == board.width() - 1 | y == board.height() - 1) {
                max_path = max(max_path, DFS(board, x, y));
            }
        }
    }
    return max_path;
}
