# File: agents.py
# Author: Ben Heil
# Version 1.0
# Since: 1/16/18
#
# This file will contain 3 distinct maze-solving agents that will inherit from the general 'Agent' class:
# - The first will be the 'AllLeft' agent:
#       * No memory
#       * Algorithm goes straight when it can, turns left when forced to turn, and turns around otherwise
#


class Agent:

    def __init__(self):
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
