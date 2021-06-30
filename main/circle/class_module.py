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
    def __init__(self, circle=Circle(50.0, 50.0, 10.0)):
        """direction为x轴方向为0度顺时针方向的角度"""
        self.circle = circle
        self.speed = 0
        self.direction = Direction()
        self.circle.color = [100, 150, 226]
        self.speed_x = math.cos(self.direction.get_direction()*math.pi/180) * self.speed
        self.speed_y = math.sin(self.direction.get_direction()*math.pi/180) * self.speed
        self.a = 0.2  # 动力（加速度，不变的）
        self.a_s = 0.02  # 阻力（反向加速度，随速度的变化动态变化）

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
        a_r = self.a - self.a_s
        a_x = 0.0
        a_y = 0.0
        if action_direction == 0:
            a_x = a_r
        elif action_direction == 90:
            a_y = a_r
        elif action_direction == 180:
            a_x = -a_r
        elif action_direction == 270:
            a_y = -a_r
        else:
            a_x = math.cos(action_direction*math.pi/180) * a_r
            a_y = math.sin(action_direction*math.pi/180) * a_r
        self.set_speed_x(self.speed_x + a_x)
        self.set_speed_y(self.speed_y + a_y)

    def stop(self):
        if self.speed - self.a_s < 0:
            self.set_speed(0)
        else:
            self.set_speed(self.speed - self.a_s)

    def move(self, pygame, surface, battlefield):
        self.a_s = math.pow(self.speed/25, 2)*2
        if self.a_s < 0.02:
            self.a_s = 0.02
        self.circle.x += self.speed_x
        self.circle.y += self.speed_y
        in_result = util.circle_in_rect(self.circle, battlefield)
        collide_loss = 0.5
        # if in_result != "yes":
        if not in_result['in']:
            print("碰撞前")
            print("speed_x  " + str(self.speed_x))
            print("speed_y  " + str(self.speed_y))
            if in_result['up'] or in_result['down']:
                if abs(self.speed_y) <= collide_loss:
                    self.set_speed_y(0.0)
                else:
                    if self.speed_y > 0:
                        self.set_speed_y(-(self.speed_y - collide_loss))
                    else:
                        self.set_speed_y(-(self.speed_y + collide_loss))
            if in_result['left'] or in_result['right']:
                if abs(self.speed_x) <= collide_loss:
                    self.set_speed_x(0.0)
                else:
                    if self.speed_x > 0:
                        self.set_speed_x(-(self.speed_x - collide_loss))
                    else:
                        self.set_speed_x(-(self.speed_x + collide_loss))
            print("碰撞后")
            print("speed_x  " + str(self.speed_x))
            print("speed_y  " + str(self.speed_y))
        if self.circle.x - self.circle.r < battlefield.x:
            self.circle.x = battlefield.x + self.circle.r
        if self.circle.x + self.circle.r > battlefield.x + battlefield.width:
            self.circle.x = battlefield.x + battlefield.width - self.circle.r
        if self.circle.y - self.circle.r < battlefield.y:
            self.circle.y = battlefield.y + self.circle.r
        if self.circle.y + self.circle.r > battlefield.y + battlefield.height:
            self.circle.y = battlefield.y + battlefield.height - self.circle.r
        self.circle.draw(pygame, surface)