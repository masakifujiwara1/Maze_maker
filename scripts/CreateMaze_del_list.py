import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
from pynput import keyboard
# import tkinter

SIZE = 51

class CreateMaze():
    def __init__(self):
        self.width = SIZE
        self.height = SIZE

        self.create_pos = []
        self.pos_x = 1
        self.pos_y = 1

        self.maze = [[0 for i in range(SIZE)] for i in range(SIZE)]
        # print(self.maze)

        self.maze_initialize()
        self.CCSP()

        self.monitor = MonKeyBoard()
        self.monitor.start()

        self.loop()

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
                        # self.create_pos[x, y] = False
                        self.create_pos.append([x, y])
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
            # 4direction
            candidate = []
            count = 0

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
            # self.create_pos[x, y] = False
            self.create_pos.append([x, y])

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
            
            # old_x = x
            # old_y = y
            x = x_
            y = y_     
            # count += 1
        
    def loop(self):
        # check
        if SIZE % 2 == 0:
            return

        # debug
        # for i in range(10):
        while(1): 
            x, y = random.choice(self.create_pos)
            # print(x, y)
            if self.maze[x][y] == 1:
            # if self.maze[x][y] == 0 or self.maze[x][y] == 1:
                # self.maze[x][y] = 1
                # self.create_pos[x, y] = True
                self.extend_wall(x, y)
                del self.create_pos[0]
            else:
                # if self.maze[x][y] == 1:
                # self.create_pos[x, y] = True
                pass
                # print("end")
                # # print(self.maze)
                # self.draw_maze()
                # break
            if len(self.create_pos) == 0:
                print("end")
                # print(self.maze)
                self.draw_maze()
                break
            # print(list(self.create_pos.values()))

            # self.input_key()

    def make_start(self):
        self.maze[1][1] = 2
    
    def make_goal(self):
        self.maze[self.height - 2][self.width - 2] = 3

    def move(self, data):
        # keys = input()
        status = self.monitor.getstatus()
        # print(status)
        if status == "right":
            if not self.maze[self.pos_x][self.pos_y + 1] == 1:
                # if not(self.pos_x == 1 and self.pos_y == 1):
                self.maze[self.pos_x][self.pos_y] = 0
                self.pos_y += 1
                self.maze[self.pos_x][self.pos_y] = 4
        if status == "left":
            if not self.maze[self.pos_x][self.pos_y - 1] == 1:
                # if not(self.pos_x == 1 and self.pos_y == 1):
                self.maze[self.pos_x][self.pos_y] = 0
                self.pos_y -= 1
                self.maze[self.pos_x][self.pos_y] = 4
        if status == "up":
            if not self.maze[self.pos_x - 1][self.pos_y] == 1:
                # if not(self.pos_x == 1 and self.pos_y == 1):
                self.maze[self.pos_x][self.pos_y] = 0
                self.pos_x -= 1
                self.maze[self.pos_x][self.pos_y] = 4
        if status == "down":
            if not self.maze[self.pos_x + 1][self.pos_y] == 1:
                # if not(self.pos_x == 1 and self.pos_y == 1):
                self.maze[self.pos_x][self.pos_y] = 0
                self.pos_x += 1
                self.maze[self.pos_x][self.pos_y] = 4

        self.make_start()
        self.make_goal()
        img = self.maze
        plt.imshow(img)

        # self.monitor.listener = None
        # print(status)

    def draw_maze(self):
        self.make_start()
        self.make_goal()

        fig = plt.figure("Maze")
        # img = self.maze

        ani = animation.FuncAnimation(fig, self.move, interval = 100)

        # plt.imshow(img)
        plt.show()

class MonKeyBoard:
    def on_press(self,key):
        try:
            # print('press: {}\n'.format(key.char))
            # print('release: {}'.format(key))
            if( key == keyboard.Key.up):
                # print("up")
                # self.listener.stop()
                self.listener = "up"
            if( key == keyboard.Key.down):
                # print("up")
                # self.listener.stop()
                self.listener = "down"
            if( key == keyboard.Key.left):
                # print("up")
                # self.listener.stop()
                self.listener = "left"
            if( key == keyboard.Key.right):
                # print("up")
                # self.listener.stop()
                self.listener = "right"
            # pass
        except AttributeError:
            print('spkey press: {}'.format(key))
    
    def on_release(self,key):
        # print('release: {}'.format(key))
        # if( key == keyboard.Key.up):
        #     # print("up")
        #     # self.listener.stop()
        #     self.listener = "up"
        # if( key == keyboard.Key.down):
        #     # print("up")
        #     # self.listener.stop()
        #     self.listener = "down"
        # if( key == keyboard.Key.left):
        #     # print("up")
        #     # self.listener.stop()
        #     self.listener = "left"
        # if( key == keyboard.Key.right):
        #     # print("up")
        #     # self.listener.stop()
        #     self.listener = "right"
        # print(key)
        if( key == keyboard.Key.esc):
            print("StopKey")
            self.listener.stop()
            self.listener = None
            
    def start(self):
        self.listener = keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
        self.listener.start()
        
    def getstatus(self):
        # if(self.listener == "up"):
        #     return self.listener
        if(self.listener == None):
            return False       
        else:
            return self.listener
        # return True


if __name__ == '__main__':
    create_maze = CreateMaze()
