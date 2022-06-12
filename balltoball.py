import pygame,sys
from math import *
pygame.init()
screen=pygame.display.set_mode((800,700))
x1,y1=100,600           #导弹的初始发射位置
x,y =500,200            #目标位置
velocity=0.8            #导弹速度
clock=pygame.time.Clock()
while True:
    x, y = pygame.mouse.get_pos()  # 获取鼠标位置，鼠标就是需要打击的目标
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
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255, 0, 0), (int(x1), int(y1)), 10)
    pygame.draw.circle(screen, (0, 0, 255), (x,y), 10)
    pygame.display.update()
