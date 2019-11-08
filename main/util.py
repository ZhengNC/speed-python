# coding=utf-8
def rect1_in_rect2(rect1, rect2):
    if rect1.x >= rect2.x and rect1.x + rect1.width <= rect2.x + rect2.width:
        if rect1.y >= rect2.y and rect1.y + rect1.height <= rect2.y + rect2.height:
            return True
    return False


def rect1_in_rect2_dir(rect1, rect2):
    """判断 矩形1 是否在 矩形2 内，如果不在，返回在哪个方向出去了"""
    if rect1.x >= rect2.x and rect1.x + rect1.width <= rect2.x + rect2.width:
        if rect1.y >= rect2.y and rect1.y + rect1.height <= rect2.y + rect2.height:
            return "yes"
    if rect1.x < rect2.x:
        return "left"
    if rect1.x + rect1.width > rect2.x + rect2.width:
        return "right"
    if rect1.y < rect2.y:
        return "up"
    if rect1.y + rect1.height > rect2.y + rect2.height:
        return "down"


def is_collides_list(current_rect, other_rects):
    """判断当前方块是否和另一个集合里的方块碰撞"""
    for other_rect in other_rects:
        b = is_collides(current_rect, other_rect)
        if b:
            return True
    return False


def is_collides(current_rect, other_rect):
    """判断当前方块是否和另一个方块碰撞"""

    cx = current_rect.x  # 当前矩形的x坐标
    cy = current_rect.y  # 当前矩形的y坐标
    cw = current_rect.width  # 当前矩形的宽度
    ch = current_rect.height  # 当前矩形的高度

    ox = other_rect.x  # 其它矩形的x坐标
    oy = other_rect.y  # 其它矩形的y坐标
    ow = other_rect.width  # 其它矩形的宽度
    oh = other_rect.height  # 其它矩形的高度
    if (cx+cw <= ox or cx >= ox+ow) or (cy+ch <= oy or cy >= oy+oh):
        return False
    else:
        return True


