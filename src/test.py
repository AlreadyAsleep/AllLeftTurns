from src import maze
m1 = maze.Maze(10)
m1.make_maze()
print(m1)

m2 = maze.gen_from_maze_file("../maze_files/4by4.maze")
print(m2)


