# File: maze.py
# Author: Ben Heil
# Version 1.1
# Since: 1/15/18
#
# This file holds the class for the environment, called "Maze"
# It will hold a size variable and an adjacency matrix which will define walls, entrances, etc.
#
# Rules for mazes:
# - There should be one entrance located on the first row
# - There should be one exit located on the last row
# - The left-most and right-most columns should be all zeroes to indicate walls
# *see example files in "../maze_files/"
#


import numpy


class Maze:
    adjacency = [[]]
    size = 0

    def __init__(self, size):
        """Initializes maze to required NxN size"""
        self.size = size
        self.adjacency = numpy.zeros((size, size))

    def __str__(self):
        return "Maze: \n" + self.adjacency.__repr__()

    def build_from_random(self, size):
        if size % 2 != 0:
            size +=1
        m = Maze(size)
        m.adjacency = maze_generator(size, size, 1, 1)
        m.size = size + 1
        return m
# Files to generate mazes from should be of the form:
# | data |
# | data |
# | data |
#   ...
# 'size\n'
# size
#
# see the maze files in "../maze_files/" for examples
def gen_from_maze_file(file):
    data = open(file, "r")
    lines = data.readlines()
    m = Maze(int(lines[len(lines) - 1]))
    count = 0
    for line in lines:
        if line == "size\n":
            break
        current = line.split(" ")
        current = [int(i) for i in current]
        m.adjacency[count] = current
        count += 1
    return m


#
#   BORROWED AND EDITED CODE FROM : https://en.wikipedia.org/wiki/Maze_generation_algorithm
#
#
from numpy.random import random_integers as rand


def maze_generator(width=81, height=51, complexity=.75, density=.75):
    # Only odd shapes
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1])))
    density = int(density * ((shape[0] // 2) * (shape[1] // 2)))
    # Build actual maze
    Z = numpy.zeros(shape)
    # Fill borders
    Z[0, :] = Z[-1, :] = 1
    Z[:, 0] = Z[:, -1] = 1
    # Make aisles
    for i in range(density):
        x, y = rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2
        Z[y, x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_,x_ = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y_, x_] == 0:
                    Z[y_, x_] = 1
                    Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                    x, y = x_, y_
    # Added code to make compatible with existing implementation
    # Flip 1's and 0's
    for i in range(width + 1):
        for j in range(height + 1):
            if Z[i][j] == 1:
                Z[i][j] = 0
            elif Z[i][j] == 0:
                Z[i][j] = 1

    # Ensure second to last row doesn't cause loop
    ones = []
    for num in range(len(Z[height - 1])):
        if Z[height - 1][num] == 1:
            ones.append(num)
    if len(ones) < 3:
        Z[height - 1][rand(2, width - 2)] = 1

    # Add entrance
    ones.clear()
    for num in range(len(Z[1])):
        if Z[1][num] == 1:
            ones.append(num)
    Z[0][rand(ones[0], ones[len(ones) - 1])] = 1

    # Add exit
    ones.clear()
    for num in range(len(Z[height - 1])):
        if Z[height - 1][num] == 1:
            ones.append(num)
    Z[height][rand(ones[0], ones[len(ones) - 1])] = 1
    return Z
