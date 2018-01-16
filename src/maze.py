# File: maze.py
# Author: Ben Heil
# Version 1.0
# Since: 1/15/18
#
# This file holds the class for the environment, called "Maze"
# It will hold a size variable and an adjacency matrix which will define walls, entrances, etc.
# It will have the ability to create a random Maze on its own or
#   read in a *.maze file and generate a maze from that
#
# Rules for mazes:
# - There should be one entrance located on the first row
# - There should be one exit located on the last row
# - The left-most and right-most columns should be all zeroes to indicate walls
# *see example files in "../maze_files/"
#


import numpy
import random


class Maze:

    adjacency = [[]]
    size = 0

    def __init__(self, size):
        """Initializes maze to required NxN size"""
        self.size = size
        self.adjacency = numpy.zeros((size, size))

    def __str__(self):
        return self.adjacency.__repr__()

    # This is not finished
    def make_maze(self):
        """Populates the maze with obstacles"""
        self.adjacency[0][random.randint(0, self.size - 1)] = 1  # creates the entry to the maze
        self.adjacency[self.size - 1][random.randint(0, self.size - 1)] = 1  # creates an exit to the maze
        for i in range(1, self.size - 2):
            for j in range(self.size - 1):
                self.adjacency[i][j] = random.randint(0, 100) % 2  # will place a zero if even and a one if not

# Files to generate mazes from should be of the form:
# | data |
# | data |
# | data |
#   ...
# length
#
# see the maze files in "../maze_files/ for examples
def gen_from_maze_file(file):
    data = open(file, "r")
    lines = data.readlines()
    m = Maze(int(lines[len(lines) - 1]))
    count = 0
    for line in lines:
        if len(line) == 1:
            break
        current = line.split(" ")
        current = [int(i) for i in current]
        m.adjacency[count] = current
        count += 1
    return m

