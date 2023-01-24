import matplotlib.pyplot as plt

SIZE = 5

class CreateMaze():
    def __init__(self) -> None:
        self.width = SIZE
        self.height = SIZE

        self.create_pos = []

        self.maze = [[0 for i in range(SIZE)] for i in range(SIZE)]
        print(self.maze)

        self.check()
        self.maze_initialize()
        self.CCSP()

    def check(self):
        if SIZE % 2 == 0:
            return

    # Calc Create Start Position
    def CCSP(self):
        for x in range(self.width):
            for y in range(self.height):
                if x % 2 == 0 and y % 2 == 0:
                    self.create_pos.append([x, y])

        print(self.create_pos)

    def maze_initialize(self):
        for i in range(self.width):
            self.maze[0][i] = 1
            self.maze[self.height - 1][i] = 1

        for i in range(self.height):
            self.maze[i][0] = 1
            self.maze[i][self.width - 1] = 1

        print(self.maze)

if __name__ == '__main__':
    create_maze = CreateMaze()
