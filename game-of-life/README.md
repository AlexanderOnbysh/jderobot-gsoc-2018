# Game of life

## Problem 
### Conway’s Game of Life
The Game of Life is a cellular automaton design by the British mathematician John
Horton Conway in 1970. The target of this challenge is to implement the Game of Life in
python. Your application will be executed from a terminal and it should refresh the grid in
each iteration with information about the game and the evolution of the patterns. When the
application starts the user should choose a pattern to start the game. A configuration file
(json format) stores all configurable options of game.

## Run
```bash
python game.py
```

## Run tests
```bash
python -m unittest tests/test_board.py
```