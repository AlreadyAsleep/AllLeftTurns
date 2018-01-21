# File: agents.py
# Author: Ben Heil
# Version 1.2
# Since: 1/16/18
#
# ==================================================================================================================
#
# This file will contain distinct maze-solving agents that will inherit from the general 'Agent' class:
# - The first will be the 'AllLeft' agent:
#       * No memory
#       * Algorithm goes left when it can, prioritizes going straight over right turns, and turns around otherwise
#       * A sensor for direction, the amount of steps taken and x,y position
#       * The win condition for the agent is when its x coordinate is equal to the size of the maze minus 1
#           i.e. it is in the last row, so it must be the end
#
# - The second will be the 'LeftOrRight' agent
#       * Memory of the percentage chance that a move gets closer to the goal
#       * Algorithm will initially not favor one direction at each junction, but change percentages based off
#               previous point
#       * Same sensors as 'AllLeft' agent but added sensor for Euclidean distance from goal
#       * The win condition is identical to the 'AllLeft' agent
#
# - The third will be the 'AStar' agent
#       *
#
# ==================================================================================================================
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

    def think(self):
        """Decide how to proceed"""
        pass

    def run(self, maze):
        """Navigate through the maze"""
        pass


#  Class AllLeft Agent
# ==================================================================================================================
#
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
        return "\nAllLeft Agent: \nSteps taken: " + str(self.steps) + "\nCurrent Direction: " + self.direction + \
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
                self.direction = "up"
            elif self.direction == "right":
                self.location[0] += 1
                self.direction = "down"
            else:
                self.location[1] += 1
                self.direction = "right"
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
        if self.left:
            self.move("leftward")
        elif self.front:
            self.move("forward")
        elif self.right:
            self.move("rightward")
        else:
            self.move("turn around")

    def run(self, maze):
        while self.active:
            self.perceive(maze.adjacency)
            if self.active:
                self.think()
        print(self)


#  Class LeftOrRight Agent
# ==================================================================================================================
#

class LeftOrRight(AllLeft):
    distance_from_goal = 0
    run_counter = 0
    chances = {"leftward": 50, "rightward": 50}
    boolean_mapping = {"leftward": False, "rightward": False}
    learning_rate = 1
    goal_location = []
    start_location = []

    def __init__(self, maze):
        super().__init__(maze)
        for i in range(len(maze.adjacency[maze.size - 1])):
            if maze.adjacency[maze.size - 1][i] == 1:
                self.goal_location = [maze.size - 1, i]
        self.start_location = self.location.copy()

    def __str__(self):
        return "LeftOrRight agent: \nRun: " + str(self.run_counter) + "\nSteps: " + str(self.steps) \
               + "\nCurrent Chances: " + str(self.chances) + "\n"

    def think(self):
        # Find direction with the highest chance
        high = max(self.chances, key=lambda key: self.chances[key])
        low = min(self.chances, key=lambda key: self.chances[key])

        # see which directions are viable
        self.boolean_mapping["leftward"] = self.left
        self.boolean_mapping["rightward"] = self.right

        # move with priority given to the highest chanced move
        flag = ""
        if self.boolean_mapping[high]:
            self.move(high)
            flag = high
        elif self.front:
            self.move("forward")
        elif self.boolean_mapping[low]:
            self.move(low)
            flag = low
        else:
            self.move("turn around")

        # if that move brings us closer to the goal, increase that directions chance, and decrease others
        temp = self.distance_from_goal
        self.distance_from_goal = abs(self.location[0] - self.goal_location[0]) + \
            abs(self.location[1] - self.goal_location[1])

        if flag == "":
            pass
        else:
            multiplier = abs(temp - self.distance_from_goal)
            if temp <= self.distance_from_goal:
                self.chances[flag] -= self.learning_rate * multiplier
                for key in self.chances:
                    if key != flag:
                        self.chances[key] += self.learning_rate * multiplier
            else:
                self.chances[flag] += self.learning_rate * multiplier
                for key in self.chances:
                    if key != flag:
                        self.chances[key] -= self.learning_rate * multiplier

        # Normalize chance values
        for key in self.chances:
            if self.chances[key] > 100:
                self.chances[key] = 100
            elif self.chances[key] < 0:
                self.chances[key] = 0



    def run(self, maze, amt):
        for i in range(amt):
            self.run_counter += 1
            while self.active:
                print(self)
                self.perceive(maze.adjacency)
                self.think()
                if self.location[0] == self.goal_location[0] and \
                        self.location[1] == self.goal_location[1]:
                    self.active = False
            print(self)
            self.active = True
            self.location = self.start_location.copy()
            self.steps = 1
