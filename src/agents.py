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


from src import maze

class Agent:

    def __init__(self):
        """Basic Constructor"""
