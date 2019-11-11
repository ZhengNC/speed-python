# coding=utf-8
def circle_in_rect(circle, rect):
    """判断圆形是否在矩形范围内，如果不在返回出了哪个方向"""
    result = {'in': False,
              'left': False,
              'right': False,
              'up': False,
              'down': False}
    if circle.x - circle.r >= rect.x and circle.x + circle.r <= rect.x + rect.width:
        if circle.y - circle.r >= rect.y and circle.y + circle.r <= rect.y + rect.height:
            result['in'] = True
            return result

    if circle.x - circle.r < rect.x:
        result['left'] = True

    if circle.x + circle.r > rect.x + rect.width:
        result['right'] = True

    if circle.y - circle.r < rect.y:
        result['up'] = True

    if circle.y + circle.r > rect.y + rect.height:
        result['down'] = True

    return result
