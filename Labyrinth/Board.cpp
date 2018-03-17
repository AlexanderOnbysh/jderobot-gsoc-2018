//
// Created by Alexander Onbysh on 3/17/18.
//
#include "Board.h"


Board::Board(char *filePath) {
    this->board = parseFile(filePath);
}

void Board::set(unsigned long x, unsigned long y, int value) {
    this->board[y][x] = value;
}


bool Board::isFree(unsigned long x, unsigned long y) {
    return this->board[y][x] == FREE_INT;
}

void Board::setMaxPath(unsigned long length) {
    this->maxPath = length;
}

unsigned long Board::getMaxPath() const {
    return this->maxPath;
}

unsigned long Board::width() const {
    return this->board[0].size();
}

unsigned long Board::height() const {
    return this->board.size();
}

vector<vector<int>> Board::parseFile(char *filePath) {
    vector<vector<int>> rows;
    ifstream file;
    string line;
    file.open(filePath);
    while (getline(file, line)) {
        vector<int> row;
        for (char i : line) {
            switch (i) {
                case WALL_CHAR:
                    row.push_back(WALL_INT);
                    break;
                case FREE_CHAR:
                    row.push_back(FREE_INT);
                default:
                    break;
//                    throw invalid_argument("Unknown symbol in file");
            }
        }
        rows.push_back(row);
    }
    return rows;
}

bool Board::operator<(const Board &left) const {
    return maxPath < left.getMaxPath();
}

ostream &operator<<(ostream &out, const Board &_board) {
    for (unsigned int y = 0; y < _board.height(); y++) {
        for (unsigned int x = 0; x < _board.width(); x++) {
            switch (_board.board[y][x]) {
                case FREE_INT:
                    out << FREE_CHAR;
                    break;
                case WALL_INT:
                    out << WALL_CHAR;
                    break;
                default:
                    out << _board.board[y][x];
            }
        }
        out << endl;
    }
}
