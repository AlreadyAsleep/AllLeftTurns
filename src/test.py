from src import maze, agents
m1 = maze.gen_from_maze_file("../maze_files/10by10.maze")
print(m1)

a1 = agents.LeftOrRight(m1)
a1.run(m1, 10)

a2 = agents.AllLeft(m1)
a2.run(m1)


