//
// Created by Alexander Onbysh on 3/15/18.
//

#ifndef LABYRINTH_LABYRINTH_H
#define LABYRINTH_LABYRINTH_H

#include <vector>
#include "Board.h"

using namespace std;

Board solve(Board board);

Board DFS(Board board, int x, int y);


#endif //LABYRINTH_LABYRINTH_H