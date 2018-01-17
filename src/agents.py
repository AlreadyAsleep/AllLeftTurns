# File: agents.py
# Author: Ben Heil
# Version 1.0
# Since: 1/16/18
#
# This file will contain 3 distinct maze-solving agents that will inherit from the general 'Agent' class:
# - The first will be the 'AllLeft' agent:
#       * No memory
#       * Algorithm goes straight when it can, turns left when forced to turn, and turns around otherwise
#       * A sensor for direction, the amount of steps taken and x,y position
#       * The win condition for the agent is when its x coordinate is equal to the size of the maze
#           i.e. it is in the last row, so it must be the end
#


class Agent:

    def __init__(self, maze):
        """Basic Constructor"""
        pass

    def __str__(self):
        """String Representation"""
        pass

    def move(self, direction):
        """Advance the agent in a direction """
        pass

    def perceive(self, directions, x, y):
        """Perceive the environment"""
        pass


class AllLeft(Agent):

    # sensors
    direction = ""
    steps = 0
    location = (0, 0)
    end = 0
    active = False

    # inherited methods
    def __init__(self, maze):
        self.direction = "down"
        self.steps = 1
        for i in range(len(maze.adjacency[0])):
            if maze.adjacency[0][i] == 1:
                self.location = (0, i)
        self.end = maze.size
        self.active = True

    def __str__(self):
        return "\nAllLeft Agent:\nSteps taken: " + str(self.steps) + "\nCurrent Direction: " + self.direction + \
               "\nLocation: " + str(self.location)

    def move(self, direction):
        pass

    def perceive(self, directions, x, y):
        if self.location[0] == self.end:
            pass
        elif self.direction == "down":
            pass
        elif self.direction == "left":
            pass
        elif self.direction == "right":
            pass
        elif self.direction == "up":
            pass
