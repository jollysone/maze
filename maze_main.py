#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Jolly_Son
# 功能：主程序，包括按键处理等

from tkinter import *
import tkinter as tk
import maze_game
import maze_graphics

# 这个是设置迷宫规模
x = 10 # 初始化迷宫的高
y = 10 # 初始化迷宫的宽

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.x = x
        self.y = y
        self.grid()
        self.field = self.createWidgets(x, y)
        self.game = maze_game.MazeGame(self.field, self.x-2, self.y-2)
        self.playGame()
        
    def createWidgets(self, x, y):
        yy = y * maze_graphics.ROOM_WIDTH_IN_PIX
        xx = x * maze_graphics.ROOM_HEIGHT_IN_PIX
        field = tk.Canvas(self, width=yy, height=xx, background=maze_graphics.BGC)
        field.grid()
        print("Canvas: xx=", xx, " yy=", yy, " w=", field.winfo_reqwidth(), " h=", field.winfo_reqheight())
        self.quitButton = tk.Button(self, text='不想玩了', command=self.stopGame)
        self.quitButton.grid()
        self.quitButton = tk.Button(self, text='重开一盘', command=self.playGame)
        self.quitButton.grid()
        self.quitButton = tk.Button(self, text='悄悄看看答案', command=self.createWidgets)
        self.quitButton.grid()
        self.textLabel = tk.Label(self, text="使用'↑' '↓' '←' '→'进行游戏，蓝点是入口，红点是出口处")
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
        y,x = 12,12
    else:
        y = int(width.get())+2
        x = int(height.get())+2
    window.destroy()

def test(content): #如果你不加上==""的话，你就会发现删不完。总会剩下一个数字
    if content.isdigit() or (content==""):
        return True
    else:
        return False

window = tk.Tk()
window.title('DIY 我的迷宫！')
window.geometry('200x155')

v1 = StringVar()
v2 = StringVar()
v1.set('10')
v2.set('10')
testCMD = window.register(test)#需要将函数包装一下，必要的
widthLabel = tk.Label(text="设置迷宫高:").pack()
width = tk.Entry(window,show=None,textvariable=v1,
		 validate='key',#发生任何变动的时候，就会调用validatecommand
		 validatecommand=(testCMD,'%P')
		)		#%P代表输入框的实时内容
#当validate为key的时候，获取输入框内容就不可以用get（）
#因为只有当validatecommand判断正确后，返回true。才会改变.get()返回的值.所以要用%P
width.pack()
heightLabel = tk.Label(text="设置迷宫宽:").pack()
height = tk.Entry(window,show=None,textvariable=v2,validate='key',validatecommand=(testCMD,'%P'))
height.pack()
tk.Label(fg='red',font=("微软雅黑",8),text="推荐迷宫 10*10 或 15*15 ").pack()
generate = tk.Button(window,text='生成迷宫',width=50,height=50,command=generateMaze).pack()
tips = tk.Label(text="推荐迷宫 10*10 或 15*15 ")
tips.pack()
window.mainloop()

app = Application()
app.master.title('Maze-迷宫小游戏 v1.0')
app.mainloop()

window.destroy() # 某些 IDEs 需要这个
