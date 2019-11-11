# coding=utf-8
import math
import util


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


class Circle:
    """基本圆形"""
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.color = [255, 255, 255]

    def draw(self, pygame, surface):
        circle = [self.x-self.r, self.y-self.r, self.r*2, self.r*2]
        pygame.draw.ellipse(surface, self.color, circle, 0)


class Direction:
    """x轴方向顺时针的角度（x正方向向右，y正方向向下）"""
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        self.direction = self.get_direction()

    def get_direction(self):
        x = self.x
        y = self.y
        z = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
        if x > 0:
            if y > 0:
                return math.acos(x / z) / (math.pi / 180)
            if y < 0:
                return 360 - math.acos(x / z) / (math.pi / 180)
            if y == 0:
                return 0
        if x < 0:
            if y > 0:
                return 180 - math.acos(-x / z) / (math.pi / 180)
            if y < 0:
                return 180 + math.acos(-x / z) / (math.pi / 180)
            if y == 0:
                return 180
        if x == 0:
            if y > 0:
                return 90
            if y < 0:
                return 270
            if y == 0:
                return 0


class Car:
    def __init__(self, circle=Circle(50.0, 50.0, 10.0), speed_max=10.0):
        """direction为x轴方向为0度顺时针方向的角度"""
        self.circle = circle
        self.speed = 0
        self.direction = Direction()
        self.circle.color = [100, 150, 226]
        self.speed_x = math.cos(self.direction.get_direction()*math.pi/180) * self.speed
        self.speed_y = math.sin(self.direction.get_direction()*math.pi/180) * self.speed
        self.a = 0.0
        self.speed_max = speed_max

    def set_speed_x(self, speed_x):
        self.speed_x = speed_x
        self.speed = math.sqrt(math.pow(self.speed_x, 2) + math.pow(self.speed_y, 2))
        self.direction.x = self.speed_x

    def set_speed_y(self, speed_y):
        self.speed_y = speed_y
        self.speed = math.sqrt(math.pow(self.speed_x, 2) + math.pow(self.speed_y, 2))
        self.direction.y = speed_y

    def set_speed(self, speed):
        self.speed = speed
        self.speed_x = math.cos(self.direction.get_direction()*math.pi/180) * self.speed
        self.speed_y = math.sin(self.direction.get_direction()*math.pi/180) * self.speed

    def change_speed(self, action_direction):
        self.a = (1.0 - abs(self.speed)/self.speed_max)/10.0
        a_x = 0.0
        a_y = 0.0
        if action_direction == 0:
            a_x = self.a
        elif action_direction == 90:
            a_y = self.a
        elif action_direction == 180:
            a_x = -self.a
        elif action_direction == 270:
            a_y = -self.a
        else:
            a_x = math.cos(action_direction*math.pi/180) * self.a
            a_y = math.sin(action_direction*math.pi/180) * self.a
        self.set_speed_x(self.speed_x + a_x)
        self.set_speed_y(self.speed_y + a_y)

    def stop(self):
        if self.speed - 0.02 < 0:
            self.set_speed(0)
        else:
            self.set_speed(self.speed - 0.02)

    def move(self, pygame, surface, battlefield):
        self.circle.x += self.speed_x
        self.circle.y += self.speed_y
        in_result = util.circle_in_rect(self.circle, battlefield)
        if in_result != "yes":
            if in_result == "up" or in_result == "down":
                self.set_speed_y(-self.speed_y)
            if in_result == "left" or in_result == "right":
                self.set_speed_x(-self.speed_x)
        if self.circle.x - self.circle.r < battlefield.x:
            self.circle.x = battlefield.x + self.circle.r
        if self.circle.x + self.circle.r > battlefield.x + battlefield.width:
            self.circle.x = battlefield.x + battlefield.width - self.circle.r
        if self.circle.y - self.circle.r < battlefield.y:
            self.circle.y = battlefield.y + self.circle.r
        if self.circle.y + self.circle.r > battlefield.y + battlefield.height:
            self.circle.y = battlefield.y + battlefield.height - self.circle.r
        self.circle.draw(pygame, surface)