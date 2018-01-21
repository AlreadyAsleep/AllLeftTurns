import matplotlib.pyplot as plotter


def show(agent, maze):
    plotter.matshow(maze.adjacency, fignum=100, cmap=plotter.cm.gray)
    plotter.show()
