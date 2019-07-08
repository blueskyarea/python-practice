import random

class Maze():
    PATH = 0
    WALL = 1

    def __init__(self, width, height):
        self.maze = []
        self.width = width
        self.height = height
    
    def set_outer_wall(self):
        for y in range(0, self.height):
            row = []
            for x in range(0, self.width):
                if (x == 0 or y == 0 or x == self.width - 1 or y == self.height - 1):
                    cell = self.WALL
                else:
                    cell = self.PATH
                row.append(cell)
            self.maze.append(row)
        return self.maze

    def print_maze(self):
        for row in self.maze:
            for cell in row:
                if cell == self.PATH:
                    print(' ', end='')
                elif cell == self.WALL:
                    print('#', end='')
            print()

maze = Maze(20, 10)
maze.set_outer_wall()
maze.print_maze()
