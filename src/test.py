from src import maze, agents

'''
a1 = agents.LeftOrRight(m1)
a1.run(m1, 100)

a2 = agents.AllLeft(m1)
a2.run(m1)
'''

m1 = maze.Maze(10)
m1 = m1.build_from_random(m1.size)
print(m1)
a1 = agents.AllLeft(m1)
a1.run(m1)
a1 = agents.LeftOrRight(m1)
a1.run(m1, 1)

'''
a2 = agents.AllLeft(m1)
a2.run(m1)

a1 = agents.LeftOrRight(m1)
a1.run(m1, 1)
'''
