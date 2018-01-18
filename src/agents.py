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

    def perceive(self, directions):
        """Perceive the environment"""
        pass


class AllLeft(Agent):

    # sensors
    direction = ""
    steps = 0
    location = [0, 0]
    end = 0
    active = False
    front = False
    left = False
    right = False

    # inherited methods
    def __init__(self, maze):
        self.direction = "down"
        self.steps = 1
        for i in range(len(maze.adjacency[0])):
            if maze.adjacency[0][i] == 1:
                self.location = [0, i]
        self.end = maze.size - 1
        self.active = True
        self.front = True

    def __str__(self):
        return "\nAllLeft Agent:\nSteps taken: " + str(self.steps) + "\nCurrent Direction: " + self.direction + \
               "\nLocation: " + str(self.location)

    def move(self, direction):
        self.steps += 1
        if direction == "forward":
            if self.direction == "down":
                self.location[0] += 1
            elif self.direction == "left":
                self.location[1] -= 1
            elif self.direction == "right":
                self.location[1] += 1
            else:
                self.location[0] -= 1
        elif direction == "leftward":
            if self.direction == "down":
                self.location[1] += 1
                self.direction = "right"
            elif self.direction == "left":
                self.location[0] += 1
                self.direction = "down"
            elif self.direction == "right":
                self.location[0] -= 1
                self.direction = "up"
            else:
                self.location[1] -= 1
                self.direction = "left"
        elif direction == "rightward":
            if self.direction == "down":
                self.location[1] -= 1
                self.direction = "left"
            elif self.direction == "left":
                self.location[0] -= 1
                self.direction + "up"
            elif self.direction == "right":
                self.location[0] += 1
                self.direction = "down"
            else:
                self.location[1] += 1
                self.direction = "up"
        else:  # turn around
            if self.direction == "down":
                self.direction = "up"
            elif self.direction == "left":
                self.direction = "right"
            elif self.direction == "right":
                self.direction = "left"
            else:
                self.direction = "down"

    def perceive(self, directions):
        if self.location[0] == self.end:
            self.active = False
        elif self.direction == "down":
            if directions[self.location[0] + 1][self.location[1]] == 1:
                self.front = True
            else:
                self.front = False
            if directions[self.location[0]][self.location[1] + 1] == 1:
                self.left = True
            else:
                self.left = False
            if directions[self.location[0]][self.location[1] - 1] == 1:
                self.right = True
            else:
                self.right = False
        elif self.direction == "left":
            if directions[self.location[0]][self.location[1] - 1] == 1:
                self.front = True
            else:
                self.front = False
            if directions[self.location[0] + 1][self.location[1]] == 1:
                self.left = True
            else:
                self.left = False
            if directions[self.location[0] - 1][self.location[1]] == 1:
                self.right = True
            else:
                self.right = False
        elif self.direction == "right":
            if directions[self.location[0]][self.location[1] + 1] == 1:
                self.front = True
            else:
                self.front = False
            if directions[self.location[0] - 1][self.location[1]] == 1:
                self.left = True
            else:
                self.left = False
            if directions[self.location[0] + 1][self.location[1]] == 1:
                self.right = True
            else:
                self.right = False
        elif self.direction == "up":
            if directions[self.location[0] - 1][self.location[1]] == 1:
                self.front = True
            else:
                self.front = False
            if directions[self.location[0]][self.location[1] - 1] == 1:
                self.left = True
            else:
                self.left = False
            if directions[self.location[0]][self.location[1] + 1] == 1:
                self.right = True
            else:
                self.right = False

    def think(self):
        if self.front:
            self.move("forward")
        elif self.left:
            self.move("leftward")
        elif self.right:
            self.move("rightward")
        else:
            self.move("turn around")

    def run(self, maze):
        while self.active:
            print(self)
            self.perceive(maze.adjacency)
            self.think()
