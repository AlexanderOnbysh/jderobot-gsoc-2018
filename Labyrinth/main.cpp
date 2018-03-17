#include <iostream>
#include "Solver.h"

using namespace std;

int main(int argc, char *argv[]) {
    if (argc != 2) {
        throw invalid_argument("Pass labyrinth file as a parameter");
    }
    Board board = Board(argv[1]);
    Board solved = solve(board);
    cout << solved.getMaxPath() << endl;
    cout << solved;
}