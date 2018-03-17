#include <iostream>
#include "Solver.h"

using namespace std;

int main(int argc, char *argv[]) {
    if (argc != 2) {
        throw invalid_argument("Pass labyrinth file as a parameter");
    }
    char *file = const_cast<char *>("/Users/alexon/Projects/jderobot-gsoc-2018/Labyrinth/input.txt");
    Board board = Board(file);
    Board solved = solve(board);
    cout << solved.getMaxPath() << endl;
    cout << solved;
}