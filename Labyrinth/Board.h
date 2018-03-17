//
// Created by Alexander Onbysh on 3/17/18.
//

#ifndef LABYRINTH_BOARD_H
#define LABYRINTH_BOARD_H

# define WALL_CHAR '#'
# define FREE_CHAR '.'
# define WALL_INT  '-1'
# define FREE_INT  '-2'

#include <vector>
#include <fstream>

using namespace std;

class Board {
public:
    explicit Board(char *filePath);

    void set(unsigned long x, unsigned long y, int value);

    bool isFree(unsigned long x, unsigned long y);

    void setMaxPath(unsigned long length);

    unsigned long getMaxPath() const;

    unsigned long width() const;

    unsigned long height() const;

    bool operator<(const Board &left) const;

    friend ostream &operator<<(ostream &out, const Board &_board);


private:
    vector<vector<int>> parseFile(char *filePath);

    vector<vector<int>> board;
    unsigned long maxPath = 0;
};


#endif //LABYRINTH_BOARD_H
