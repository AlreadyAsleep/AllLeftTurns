from src import maze, agents, graphics

m1 = maze.Maze(10)
m1 = m1.build_from_random(m1.size)
print(m1)
a1 = agents.AllLeft(m1)
a1.run(m1)
graphics.show(a1, m1)
