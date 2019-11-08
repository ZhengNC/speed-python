# coding=utf-8
from sys import exit
from class_module import Rect, Car

import pygame
import util

pygame.init()

# 创建时钟对象（可以控制游戏循环频率）
clock = pygame.time.Clock()

window = pygame.display.set_mode((600, 1000), 0, 32)

pygame.display.set_caption("Speed")

# 自动记录游戏时间事件（精度为100毫秒）
GAME_TIME = pygame.USEREVENT + 1
# 每100毫秒记录一次游戏时间
pygame.time.set_timer(GAME_TIME, 100)

# 游戏背景
game_background = Rect(0, 0, window.get_width(), window.get_height())

# 战场区域
battlefield = Rect(0, 0, window.get_width(), window.get_height())

my_key_up = False
my_key_down = False
my_key_left = False
my_key_right = False

my_car = Car(rect=Rect(200, 200, 10, 10))

my_key_up1 = False
my_key_down1 = False
my_key_left1 = False
my_key_right1 = False

my_car1 = Car(rect=Rect(200, 200, 10, 10))
my_car1.rect.color = [100, 150, 226]
while True:
    # 设置fps
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                my_key_down = True
            if event.key == pygame.K_UP:
                my_key_up = True
            if event.key == pygame.K_LEFT:
                my_key_left = True
            if event.key == pygame.K_RIGHT:
                my_key_right = True

            if event.key == pygame.K_s:
                my_key_down1 = True
            if event.key == pygame.K_w:
                my_key_up1 = True
            if event.key == pygame.K_a:
                my_key_left1 = True
            if event.key == pygame.K_d:
                my_key_right1 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                my_key_down = False
            if event.key == pygame.K_UP:
                my_key_up = False
            if event.key == pygame.K_LEFT:
                my_key_left = False
            if event.key == pygame.K_RIGHT:
                my_key_right = False

            if event.key == pygame.K_s:
                my_key_down1 = False
            if event.key == pygame.K_w:
                my_key_up1 = False
            if event.key == pygame.K_a:
                my_key_left1 = False
            if event.key == pygame.K_d:
                my_key_right1 = False

    if my_key_up == True:
        my_car.change_speed_y(0)

    if my_key_down == True:
        my_car.change_speed_y(1)

    if my_key_left == True:
        my_car.change_speed_x(0)

    if my_key_right == True:
        my_car.change_speed_x(1)

    if my_key_up1 == True:
        my_car1.change_speed_y(0)

    if my_key_down1 == True:
        my_car1.change_speed_y(1)

    if my_key_left1 == True:
        my_car1.change_speed_x(0)

    if my_key_right1 == True:
        my_car1.change_speed_x(1)

    my_car.stop()
    my_car1.stop()

    game_background.draw(pygame, window)

    my_car.move(pygame, window, battlefield)
    my_car1.move(pygame, window, battlefield)

    pygame.display.update()