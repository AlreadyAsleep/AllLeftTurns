from src import maze, agents
m1 = maze.gen_from_maze_file("../maze_files/4by4.maze")
print(m1)

a1 = agents.AllLeft(m1)
print(a1)


