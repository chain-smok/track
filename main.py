import pygame,sys
from math import *
from Ball import Ball

pygame.init()   
screen=pygame.display.set_mode((800,700))
x1,y1=100,600           #导弹的初始发射位置
x,y =500,200            #目标位置
velocity=1.1            #导弹速度
clock=pygame.time.Clock()
steps = []
myball = Ball(800,700,screen)
while True:
    myball.move()
    x, y = myball.xpos,myball.ypos # 获取运动小球的位置
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(300)
    distance=sqrt(pow(x1-x,2)+pow(y1-y,2))      #两点距离公式
    section=velocity               #每个时间片需要移动的距离
    sina=(y1-y)/distance
    cosa=(x-x1)/distance
    angle=atan2(y-y1,x-x1)              #两点线段的弧度值
    x1,y1=(x1+section*cosa,y1-section*sina)
    screen.fill((0, 0, 0))
    steps.append((int(x1), int(y1)))
    for step in steps:
        pygame.draw.circle(screen, (255, 0, 0), step, 10 )
    myball.draw_ball()
    # pygame.draw.circle(screen, (0, 0, 255), (x,y), 10)
    pygame.display.update()
