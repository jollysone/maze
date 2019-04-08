#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: jollysone@gmail.com
# 功能：迷宫的小格子

U_WALL = 1
R_WALL = 2
D_WALL = 4
L_WALL = 8
ALL_WALLS = 15
FRONT = 16
VISITED = 32

# 迷宫的小格子
class MazeRoom(object):
    room = None
    # 构造函数初始化
    def __init__(self):
        self.room = ALL_WALLS

    # 清除格子
    def clear(self):
        self.room = ALL_WALLS

    # 打破格子
    def breakWall(self, wall):
        self.room &= ~wall

    # 代表有墙
    def hasWall(self, wall):
        if self.room & wall == 0:
            return False
        else:
            return True

    # 代表没有墙
    def noWall(self,wall):
        if self.room & wall == 0:
            return True
        else:
            return False

    # 访问这个格子
    def visit(self):
        self.room |= VISITED

    # 返回是否已经访问了这个格子 访问了True 否则 False
    def visited(self):
        if self.room & VISITED == 0:
            return False
        else:
            return True

    # 设置在前面的格子
    def setFront(self):
        self.room |= FRONT

    # 是否格子在前面
    def isFront(self):
        if self.room & FRONT == 0:
            return False
        else:
            return True

    # 获得这个格子
    def getRoom(self):
        return self.room