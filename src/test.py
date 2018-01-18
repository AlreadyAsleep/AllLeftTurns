from src import maze, agents
'''
m1 = maze.gen_from_maze_file("../maze_files/4by4.maze")
print(m1)


a1 = agents.LeftOrRight(m1)
a1.run(m1, 100)

a2 = agents.AllLeft(m1)
a2.run(m1)
'''
m1 = maze.Maze(26)
m1.adjacency = maze.maze_generator(m1.size, m1.size, 1, 1)
print(m1)

a2 = agents.AllLeft(m1)
a2.run(m1)

a1 = agents.LeftOrRight(m1)
a1.run(m1, 1)

