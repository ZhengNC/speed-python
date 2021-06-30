# coding=utf-8
import math

x = 1.0
y = 2.0
h = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
j_x = math.acos(x/h)/(math.pi/180)
j_y = math.asin(y/h)/(math.pi/180)
j_a = math.atan(y/x)/(math.pi/180)

print("h "+str(h))
print("j_x "+str(j_x))
print("j_y "+str(j_y))
print("j_a "+str(j_a))