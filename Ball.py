from random import randint
import pygame

class Ball:

    def __init__(self, width,height,screen):
        self.scrnwidth = width
        self.scrnheight = height
        self.screen = screen
        self.reset()
        self.color = (randint(0,255),randint(0,255),randint(0,255))

    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color, (self.xpos, self.ypos), self.radius)

    def reset(self):
        self.radius = randint(2, 10)
        self.xpos = randint(self.radius, int(self.scrnwidth)-self.radius)
        self.ypos = randint(self.radius, int(self.scrnheight)-self.radius)
        self.xvelocity = randint(1, 2)
        self.yvelocity = randint(1, 2)
        self.color = (randint(0,255),randint(0,255),randint(0,255))

    def move(self):
        # 进行相应的移动，如果坐标超过屏幕边缘则向相反方向移动
        # 让球的x坐标和y坐标，按照向量的大小进行增加，表示球的运行，向下和向右

        self.xpos += self.xvelocity
        self.ypos += self.yvelocity

        # 如果球的y坐标大于等于屏幕高度和球的半径的差，则调整球的运行y轴方向朝上
        if self.ypos >= self.scrnheight - self.radius:
            self.yvelocity = -self.yvelocity

        # 如果球的y坐标小于等于屏幕高度和球的半径的差，则调整球的y轴运行方向朝下
        if self.ypos <= self.radius:
            self.yvelocity = abs(self.yvelocity)

        # 如果球的x坐标大于等于屏幕宽度和球的半径差，则调整球的运行x轴方向朝左
        if self.xpos >= self.scrnwidth - self.radius:
            self.xvelocity = -self.xvelocity

        # 如果球的x坐标小于等于屏幕宽度和球半径的差，则调整球的运行x轴方向朝右
        if self.xpos <= self.radius:
            self.xvelocity = abs(self.xvelocity)
