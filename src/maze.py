# File: maze.py
# Author: Ben Heil
# Version 1.0
# Since: 1/15/18
#
# This file holds the class for the environment, called "Maze"
# It will hold a size variable and an adjacency matrix which will define walls, entrances, etc.
# It will have the ability to create a random Maze on its own or
#   read in a *.maze file and generate a maze from that


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

    def make_maze(self):
        """Populates the maze with obstacles"""
        self.adjacency[0][random.randint(0, self.size - 1)] = 1  # creates the entry to the maze
        self.adjacency[self.size - 1][random.randint(0, self.size - 1)] = 1  # creates an exit to the maze
        for i in range(1, self.size - 2):
            for j in range(self.size - 1):
                self.adjacency[i][j] = random.randint(0, 100) % 2  # will place a zero if even and a one if not



