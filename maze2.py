
from tkinter import *
import tkinter as tk
x = 30
maze = [[0,0,1],[0,1,0],[0,2,1],[0,3,1],[0,4,1],[0,5,0],
        [1,0,1],[1,1,0],[1,2,1],[1,3,1],[1,4,1],[1,5,0],
        [2,0,1],[2,1,0],[2,2,1],[2,3,1],[2,4,0],[2,5,0],
        [3,0,1],[3,1,1],[3,2,1],[3,3,1],[3,4,1],[3,5,0],
        [4,0,1],[4,1,0],[4,2,1],[4,3,1],[4,4,0],[4,5,0],
        [5,0,1],[5,1,0],[5,2,1],[5,3,1],[5,4,1],[5,5,0]
        ]
# for i in range(0, x):
#     maze.append([])  # 增加一行
#     for j in range(0, y):
#         maze[i].append(rm)
class Draw(object):
    def __init__(self):
        self.x = x


    def Maze(self,maze):
        field = tk.Canvas( background='#fff000000')
        for i in range(6):
            for j in range(6):
                print(i+j)
                if maze[i+j][2] == 1:
                    print(maze[i][2])
                    field.create_rectangle(10 + i * x, 10 + j * x, 10 + i * x + x, 10 + j * x + x, fill='black')
                    print(10 + i * x, 10 + j * x, 10 + i * x + x, 10 + j * x + x)
                elif maze[i+j][2] == 0:
                    print(maze[i][2])
                    field.create_rectangle(10 + i * x, 10 + j * x, 10 + i * x + x, 10 + j * x + x, fill='white')
                    print(10 + i * x, 10 + j * x, 10 + i * x + x, 10 + j * x + x)

        field.grid()



if __name__ == '__main__':
    window = tk.Tk()
    window.title('我的迷宫！')
    app = Draw()
    app.Maze(maze)
    window.mainloop()
    # window.destroy() # 某些 IDEs 需要这个