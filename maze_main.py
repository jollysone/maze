#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Jolly_Son
# 功能：主程序，包括按键处理等
from tkinter import *
import tkinter as tk
import maze_room
import maze_game
import maze_graphics

# 这个是设置迷宫规模
x = 10 # 迷宫的高
y = 10 # 迷宫的宽

# class SetMazeScale(tk.Frame):
#     def __init__(self, master):
#         super().__init__()
#         self.master = master
#         self.master.resizable(0, 0)
#         self.master.wm_title("DIY 我的迷宫!")
#         self.pack(fill=tk.BOTH, expand=1)
#
#     def create_widgets(self):
#         self.setupFrame = tk.Frame(self, borderwidth=2, relief="ridge")
#         self.widthLabel = tk.Label(self.setupFrame, text="设置迷宫宽:")
#         self.widthLabel.pack(side="left")
#         self.widthEntry = tk.Entry(self.setupFrame, width=2)
#         self.widthEntry.pack(side="left", fill="x", expand=True)
#
#         self.heightLabel = tk.Label(self.setupFrame, text="设置迷宫高:")
#         self.heightLabel.pack(side="left")
#         self.heightEntry = tk.Entry(self.setupFrame, width=2)
#         self.heightEntry.pack(side="left", fill="x", expand=True)
#
#         self.generateButton = tk.Button(self.setupFrame, text="生成!")
#         self.generateButton.bind("<Button-1>", self.new_maze)
#         self.generateButton.pack(side="left")
#
#     def new_maze(self, event):
#         global x,y
#         y = int(self.widthEntry.get())
#         x = int(self.heightEntry.get())



class Application(tk.Frame):
    # 这个是应用类
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.x = x
        self.y = y
        self.grid()
        self.field = self.createWidgets(x, y)
        self.game = maze_game.MazeGame(self.field, self.x - 2, self.y - 2)
        self.playGame()
        
    def createWidgets(self, x, y):
        yy = y * maze_graphics.ROOM_WIDTH_IN_PIX
        xx = x * maze_graphics.ROOM_HEIGHT_IN_PIX
        field = tk.Canvas(self, width=yy, height=xx, background=maze_graphics.BGC)
        field.grid()
        # print("Canvas: xx=", xx, " yy=", yy, " w=", field.winfo_reqwidth(), " h=", field.winfo_reqheight())
        # self.quitButton = tk.Button(self, text='Quit', command=self.stopGame)
        # self.quitButton.grid()
        # self.quitButton = tk.Button(self, text='Start', command=self.playGame)
        # self.quitButton.grid()
        self.textLabel = tk.Label(self, text="Use arrow keys, 'q' = quit")
        self.textLabel.grid()
        return field

    def addHandler(self, field):
        # 添加一个按键处理
        seq = '<Any-KeyPress>'
        field.bind_all(sequence=seq, func=self.handleKey, add=None)
        
    def initGame(self):
        # 设置游戏初始化
        self.game.clearGame()
        self.game.drawGame()

    def stopGame(self):
        # 杀死这个应用
        self.done = True
        self.quit()

    def handleKey(self, event):
        # 按键处理程序
        if False:
            print("handleKey: ", event.keysym, event.keycode, event.keysym_num)
        mv = None
        if event.keycode == 104: # Down
            mv = 'D'
        elif event.keycode == 100: # Left
            mv = 'L'
        elif event.keycode == 102: # Right
            mv = 'R'
        elif event.keycode == 98: # Up
            mv = 'U'
        elif event.keycode == 88: # KP_Down
            mv = 'D'
        elif event.keycode == 80: # KP_Up
            mv = 'U'
        elif event.keycode == 83: # KP_Left
            mv = 'L'
        elif event.keycode == 85: # KP_Right
            mv = 'R'
        elif event.keysym == 'Down': # ??_Down
            mv = 'D'
        elif event.keysym == 'Up': # ??_Up
            mv = 'U'
        elif event.keysym == 'Left': # ??_Left
            mv = 'L'
        elif event.keysym == 'Right': # ??_Right
            mv = 'R'
        elif event.keycode == 24: # 'Q' or 'q'
            self.stopGame()
            return
        else:
            return
        # Player's move
        if self.game.move(mv):
            # Solved - exit the program
            self.stopGame()
            
    def playGame(self):
        # 开始游戏
        self.initGame()
        self.addHandler(self.field)
        # return in App mainloop to play

def generateMaze():
    global x,y
    if width.get()=='' or height.get()=='':
        y,x = 15,15
    else:
        y = int(width.get())
        x = int(height.get())
    window.destroy()

def test(content): #如果你不加上==""的话，你就会发现删不完。总会剩下一个数字
    if content.isdigit() or (content==""):
        return True
    else:
        return False

window = tk.Tk()
window.title('DIY 我的迷宫！')
window.geometry('200x135')

v1 = StringVar()
v2 = StringVar()
testCMD = window.register(test)#需要将函数包装一下，必要的
widthLabel = tk.Label(text="设置迷宫高:")
widthLabel.pack()
width = tk.Entry(window,show=None,textvariable=v1,
		 validate='key',#发生任何变动的时候，就会调用validatecommand
		 validatecommand=(testCMD,'%P')
		)				#%P代表输入框的实时内容
#当validate为key的时候，获取输入框内容就不可以用get（）
#因为只有当validatecommand判断正确后，返回true。才会改变.get()返回的值.所以要用%P
width.pack()
heightLabel = tk.Label(text="设置迷宫宽:")
heightLabel.pack()
height = tk.Entry(window,show=None,textvariable=v2,
		 validate='key',#发生任何变动的时候，就会调用validatecommand
		 validatecommand=(testCMD,'%P'))
height.pack()
generate = tk.Button(window,text='生成迷宫',width=50,height=50,command=generateMaze)
generate.pack()
window.mainloop()


app = Application()
app.master.title('Maze-迷宫小游戏 v1.0')

app.mainloop()

# 打印测试
print("Game over")


window.destroy() # 某些 IDEs 需要这个
