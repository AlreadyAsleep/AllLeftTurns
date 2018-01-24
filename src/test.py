from src import maze, agents, graphics

m1 = maze.Maze(20)
m1 = maze.gen_from_maze_file("../maze_files/10by10.maze")
print(m1)
a1 = agents.LeftOrRight(m1)
a1.run(m1, 1)
a1 = agents.AllLeft(m1)
a1.run(m1)
graphics.show(a1, m1)
