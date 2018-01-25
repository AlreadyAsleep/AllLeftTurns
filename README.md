# All Left Turns
An AI program in python that generates and solves mazes

### Agents
  - <b>"AllLeft" agent:</b>
       * No memory
       * Algorithm goes left when it can, prioritizes going straight over right turns, and turns around otherwise
       * A sensor for direction, the amount of steps taken and x,y position
       * The win condition for the agent is when its x coordinate is equal to the size of the maze minus 1
           i.e. it is in the last row, so it must be the end
 
 - <b>"LeftOrRight" agent</b>
      * Memory of the percentage chance that a move gets closer to the goal
      * Algorithm will initially not favor one direction at each junction, but change percentages based off
               previous point
      * Same sensors as 'AllLeft' agent but added sensor for Euclidean distance from goal
      * The win condition is identical to the 'AllLeft' agent

### Environment:

<b>Rules for mazes:</b>
 - There should be one entrance located on the first row
 - There should be one exit located on the last row
 - The left-most and right-most columns should be all zeroes to indicate walls
 *see example files in "../maze_files/"

### Outcomes:

Eventually, more robust agents and environments will be included in this project. This is currently the foundation for later research.
### Sources:
[Wikipedia](https://en.wikipedia.org/wiki/Maze_generation_algorithm)

### Other References:
[The original GANs](https://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf)

[Some code ideas](http://blog.aylien.com/introduction-generative-adversarial-networks-code-tensorflow/)

[An implementation idea](http://cs231n.stanford.edu/reports/2017/pdfs/322.pdf)

