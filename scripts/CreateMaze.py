import matplotlib.pyplot as plt
import numpy as np
import random

SIZE = 13

class CreateMaze():
    def __init__(self) -> None:
        self.width = SIZE
        self.height = SIZE

        self.create_pos = {}

        self.maze = [[0 for i in range(SIZE)] for i in range(SIZE)]
        # print(self.maze)

        self.check()
        self.maze_initialize()
        self.CCSP()

        self.loop()

    def check(self):
        if SIZE % 2 == 0:
            return

    # Calc Create Start Position
    def CCSP(self):
        for x in range(self.width):
            for y in range(self.height):
                if (x + 1) % 2 == 0 or (y + 1) % 2 == 0:
                # if (x + 1) % 2 == 0 and (y + 1) % 2 == 0:
                    # if not x == 0 and not y == 0:
                    pass
                    # self.create_pos[x, y] = False
                # elif not((x + 1) % 2 == 0 or (y + 1) % 2 == 0):
                    # if not x == 0 or not y == 0:
                    # self.create_pos[x, y] = False
                    # pass
                else:
                    if x == 0 or y == 0 or x == self.width - 1 or y == self.height - 1:
                        self.create_pos[x, y] = False
                    # pass
        # print(list(self.create_pos.keys()))

    def maze_initialize(self):
        for i in range(self.width):
            self.maze[0][i] = 1
            self.maze[self.height - 1][i] = 1

        for i in range(self.height):
            self.maze[i][0] = 1
            self.maze[i][self.width - 1] = 1

        # print(self.maze)

    def extend_wall(self, x, y):
        while(1):
            # 4方向の候補作成
            candidate = []
            count = 0
            # x ± 1: y ± 1
            if x + 1 < self.width:
                if self.maze[x + 1][y] == 0:
                    if self.maze[x + 2][y] == 0:
                        candidate.append([x + 2, y, 1])
                # if self.maze[x + 1][y] == 1:
                #     break
            if x - 1 > 0:
                if self.maze[x - 1][y] == 0:
                    if self.maze[x - 2][y] == 0:
                        candidate.append([x - 2, y, 2])
                # if self.maze[x - 1][y] == 1:
                #     break
            if y + 1 < self.height:                        
                if self.maze[x][y + 1] == 0:
                    if self.maze[x][y + 2] == 0:
                        candidate.append([x, y + 2, 3])
                # if self.maze[x][y + 1] == 1:
                #     break
            if y - 1 > 0:
                if self.maze[x][y - 1] == 0:
                    if self.maze[x][y - 2] == 0:
                        candidate.append([x, y - 2, 4])
                # if self.maze[x][y - 1] == 1: 
                #     break

            # if self.maze[x + 1][y] == 1:
            #     break
            # elif self.maze[x - 1][y] == 1:
            #     break
            # elif self.maze[x][y + 1] == 1:
            #     break
            # elif self.maze[x][y - 1] == 1: 
            #     break

            if len(candidate) == 0:
                # print("break")
                # if count > 0:
                #     self.create_pos[old_x, old_y] = False
                break
            
            x_ , y_, tag = random.choice(candidate)
            # self.create_pos.append([x_, y_])
            # self.create_pos[x_, y_] = False
            self.create_pos[x, y] = False

            if tag == 1:
                self.maze[x + 1][y] = 1
                self.maze[x + 2][y] = 1
            if tag == 2:
                self.maze[x - 1][y] = 1
                self.maze[x - 2][y] = 1
            if tag == 3:
                self.maze[x][y + 1] = 1
                self.maze[x][y + 2] = 1
            if tag == 4:
                self.maze[x][y - 1] = 1
                self.maze[x][y - 2] = 1
            
            old_x = x
            old_y = y
            x = x_
            y = y_     
            count += 1
        
    def loop(self):
        # debug
        # for i in range(10):
        while(1): 
            x, y = random.choice(list(self.create_pos.keys()))
            # print(x, y)
            if self.maze[x][y] == 1:
            # if self.maze[x][y] == 0 or self.maze[x][y] == 1:
                # self.maze[x][y] = 1
                self.create_pos[x, y] = True
                self.extend_wall(x, y)
            else:
                # if self.maze[x][y] == 1:
                self.create_pos[x, y] = True
                # pass
                # print("end")
                # # print(self.maze)
                # self.draw_maze()
                # break
            if all(list(self.create_pos.values())) == True:
                print("end")
                # print(self.maze)
                self.draw_maze()
                break
            # print(list(self.create_pos.values()))

    def draw_maze(self):
        img = self.maze
        plt.imshow(img)
        plt.show()


if __name__ == '__main__':
    create_maze = CreateMaze()
