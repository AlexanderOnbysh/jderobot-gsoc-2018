cmake_minimum_required(VERSION 3.8)
project(Labyrinth)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp Board.h Board.cpp Solver.h Solver.cpp)
add_executable(Labyrinth ${SOURCE_FILES})