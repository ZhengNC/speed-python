# coding=utf-8
from sys import exit
from class_module import Rect, Circle, Car, Direction

import pygame

pygame.init()

# 创建时钟对象（可以控制游戏循环频率）
clock = pygame.time.Clock()

window = pygame.display.set_mode((600, 800), 0, 32)

pygame.display.set_caption("Speed")

# 自动记录游戏时间事件（精度为100毫秒）
GAME_TIME = pygame.USEREVENT + 1
# 每100毫秒记录一次游戏时间
pygame.time.set_timer(GAME_TIME, 100)

# 游戏背景
game_background = Rect(0, 0, window.get_width(), window.get_height())

# 战场区域
battlefield = Rect(0, 0, window.get_width(), window.get_height())

my_key_up = 0
my_key_down = 0
my_key_left = 0
my_key_right = 0

my_car = Car()

while True:
    # 设置fps
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                my_key_down = 1
            if event.key == pygame.K_UP:
                my_key_up = -1
            if event.key == pygame.K_LEFT:
                my_key_left = -1
            if event.key == pygame.K_RIGHT:
                my_key_right = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                my_key_down = 0
            if event.key == pygame.K_UP:
                my_key_up = 0
            if event.key == pygame.K_LEFT:
                my_key_left = 0
            if event.key == pygame.K_RIGHT:
                my_key_right = 0

    game_background.draw(pygame, window)

    vector_x = my_key_right + my_key_left
    vector_y = my_key_up + my_key_down
    if vector_x != 0 or vector_y != 0:
        action_direction = Direction(vector_x, vector_y)
        my_car.change_speed(action_direction.get_direction())

    # if my_key_right and my_key_down and not my_key_left and not my_key_up:
    #     my_car.change_speed(45)
    # else:
    #     if my_key_right and not my_key_left and not my_key_up and not my_key_down:
    #         my_car.change_speed(0)
    #     if my_key_down and not my_key_up and not my_key_left and not my_key_right:
    #         my_car.change_speed(90)
    #
    # if my_key_right and my_key_up and not my_key_left and not my_key_down:
    #     my_car.change_speed(315)
    # else:
    #     if my_key_up and not my_key_down and not my_key_left and not my_key_right:
    #         my_car.change_speed(270)
    #
    # if my_key_left and my_key_down and not my_key_up and not my_key_right:
    #     my_car.change_speed(135)
    # else:
    #     if my_key_left and not my_key_right and not my_key_up and not  my_key_down:
    #         my_car.change_speed(180)
    #
    # if my_key_left and my_key_up and not my_key_right and not my_key_down:
    #     my_car.change_speed(225)
    # if my_key_right:
    #     my_car.change_speed(0)
    # if my_key_left:
    #     my_car.change_speed(180)
    # if my_key_up:
    #     my_car.change_speed(270)
    # if my_key_down:
    #     my_car.change_speed(90)

    my_car.stop()

    my_car.move(pygame, window, battlefield)

    pygame.display.update()