# coding=utf-8
def circle_in_rect(circle, rect):
    """判断圆形是否在矩形范围内，如果不在返回出了哪个方向"""
    if circle.x - circle.r >= rect.x and circle.x + circle.r <= rect.x + rect.width:
        if circle.y - circle.r >= rect.y and circle.y + circle.r <= rect.y + rect.height:
            return "yes"

    if circle.x - circle.r < rect.x:
        return "left"
    if circle.x + circle.r > rect.x + rect.width:
        return "right"
    if circle.y - circle.r < rect.y:
        return "up"
    if circle.y + circle.r > rect.y + rect.height:
        return "down"
