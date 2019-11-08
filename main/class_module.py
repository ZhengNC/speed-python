# coding=utf-8
import util
import random
import math


class Rect:
    """基本矩形"""
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = [255, 255, 255]

    def draw(self, pygame, surface):
        rect = [self.x, self.y, self.width, self.height]
        pygame.draw.rect(surface, self.color, rect, 0)


class Car:
    def __init__(self, rect=Rect(0, 0, 30, 30), speed_x=0.0, speed_y=0.0):
        self.rect = rect
        self.rect.color = [138, 43, 226]
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.speed_x_max = 10.0
        self.speed_y_max = 10.0
        self.a_x = 0.0
        self.a_y = 0.0

    def stop(self):
        """受到自然阻力的减速效果"""
        if self.speed_x > 0:
            self.speed_x -= 0.02
            if self.speed_x < 0:
                self.speed_x = 0
        if self.speed_x < 0:
            self.speed_x += 0.02
            if self.speed_x > 0:
                self.speed_x = 0
        if self.speed_y > 0:
            self.speed_y -= 0.02
            if self.speed_y < 0:
                self.speed_y = 0
        if self.speed_y < 0:
            self.speed_y += 0.02
            if self.speed_y > 0:
                self.speed_y = 0

    def change_speed_x(self, action):
        """x方向的改变"""
        self.a_x = (1.0 - abs(self.speed_x)/self.speed_x_max)/10.0
        if action == 1:
            self.speed_x += self.a_x
        if action == 0:
            self.speed_x -= self.a_x

    def change_speed_y(self, action):
        """y方向的改变"""
        self.a_y = (1.0 - abs(self.speed_y)/self.speed_y_max)/10.0
        if action == 1:
            self.speed_y += self.a_y
        if action == 0:
            self.speed_y -= self.a_y

    def move(self, pygame, surface, battlefield):

        # print("a_x  "+str(self.a_x))
        # print("speed_x  "+str(self.speed_x))
        # print("a_y  "+str(self.a_y))
        # print("speed_y  "+str(self.speed_y))
        # print "------------------"
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        in_result = util.rect1_in_rect2_dir(self.rect, battlefield)
        collide_loss = 0.5
        if in_result != "yes":
            print "碰撞前"
            print "speed_x  " + str(self.speed_x)
            print "speed_y  " + str(self.speed_y)
            if in_result == "up" or in_result == "down":
                if abs(self.speed_y) <= collide_loss:
                    self.speed_y = 0.0
                else:
                    self.speed_y = -self.speed_y
                    if self.speed_y > 0:
                        self.speed_y -= collide_loss
                    else:
                        self.speed_y += collide_loss
            if in_result == "left" or in_result == "right":
                if abs(self.speed_x) <= collide_loss:
                    self.speed_x = 0.0
                else:
                    self.speed_x = -self.speed_x
                    if self.speed_x > 0:
                        self.speed_x -= collide_loss
                    else:
                        self.speed_x += collide_loss
            print "碰撞后"
            print "speed_x  " + str(self.speed_x)
            print "speed_y  " + str(self.speed_y)
        if self.rect.x < battlefield.x:
            self.rect.x = battlefield.x
        if self.rect.x + self.rect.width > battlefield.x + battlefield.width:
            self.rect.x = battlefield.x + battlefield.width - self.rect.width
        if self.rect.y < battlefield.y:
            self.rect.y = battlefield.y
        if self.rect.y + self.rect.height > battlefield.y + battlefield.height:
            self.rect.y = battlefield.y + battlefield.height - self.rect.height
        self.rect.draw(pygame, surface)


