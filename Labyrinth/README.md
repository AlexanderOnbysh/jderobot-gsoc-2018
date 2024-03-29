# Labyrinth

## Problem
Labyrinth
Lets imagine you have a labyrinth described as walls (#) and holes (.) where you cannot
pass through the walls and you can move to adjacent holes. Diagonal adjacencies will
not be taken into account, only vertical and horizontal.
Your applications should find the largest pathway moving only between holes, reading
the labyrinth schema from a txt file, using only standard libraries of c++11. All the lines in
the input file will have the same number of elements. Your application should save the
schema of the largest detected pathway, overwriting the holes (.) with the order in which
the hole has been visited.

## Example

input:
```
##.##.#
#..##.#
#.#####
#..####
#######
```

output:
```
6
##0##.#
#21##.#
#3#####
#45####
#######
```

## Build & run
```
cmake .
make
Labyrinth ./input.txt
```