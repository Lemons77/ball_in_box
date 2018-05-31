import random
import sympy
from .validate import validate

__all__ = ['ball_in_box']

def get_max(blocks):
    from sympy.abc import x, y

    # area
    dx, dy = [-1.0, 1.0], [-1.0, 1.0]
    #blocks = []
    block_num = len(blocks)
    result = []

    def print_res():
        '''
        print("area: \n", dx, dy)
        print("blocks: \n", blocks)
        print("max circle: \n", result)
        '''
        return result

    def test(res):
        not_covering = True
        for b in blocks:
            if (b[0] - res[1][0]) ** 2 + (b[1] - res[1][1]) ** 2 < res[0] ** 2:
                not_covering = False
        return not_covering

    '''
    def get_block():
        bx = random.uniform(dx[0], dx[1])
        by = random.uniform(dy[0], dy[1])
        return [bx, by]
    
    
    # max: 3
    block_num = random.randint(1, 3)
    blocks.insert(0, get_block())
    i = block_num
    while i > 1:
        i -= 1
        b = get_block()
        for block in blocks:
            if block == b:
                continue
        blocks.insert(i, b)
    '''

    pos, r = [], []

    def max_of_r():
        i = 0
        max_r = 0
        while i < len(r):
            if r[max_r] <= r[i]:
                max_r = i
            i += 1
        if i == 0:
            return None
        return [r[max_r], pos[max_r]]

    # for 1 block
    for block in blocks:
        x0, y0 = block[0], block[1]
        p = [sympy.solve(
            [(x - x0) ** 2 + (y - y0) ** 2 - (1 - x) ** 2, (x - x0) ** 2 + (y - y0) ** 2 - (1 - y) ** 2, x - y],
            [x, y]), sympy.solve(
            [(x - x0) ** 2 + (y - y0) ** 2 - (1 - x) ** 2, (x - x0) ** 2 + (y - y0) ** 2 - (1 + y) ** 2, x + y],
            [x, y]), sympy.solve(
            [(x - x0) ** 2 + (y - y0) ** 2 - (1 + x) ** 2, (x - x0) ** 2 + (y - y0) ** 2 - (1 + y) ** 2, x - y],
            [x, y]), sympy.solve(
            [(x - x0) ** 2 + (y - y0) ** 2 - (1 + x) ** 2, (x - x0) ** 2 + (y - y0) ** 2 - (1 - y) ** 2, x + y],
            [x, y])]
        i = 0
        for p_ in p:
            for p__ in p_:
                if 1 >= p__[0] >= -1 and 1 >= p__[1] >= -1:
                    if i < 2:
                        r_ = 1 - p__[0]
                    else:
                        r_ = 1 + p__[0]
                    if 1 >= r_ >= 0:
                        p_ = p__
                        if test([r_, p_]):
                            r.append(r_)
                            pos.append(p_)
                        break
            i += 1
    result = max_of_r()
    if result is not None:
        return print_res()
    # for 2 blocks
    pos, r = [], []
    i, j = 0, 0
    while i < block_num:
        j = i + 1
        while j < block_num:
            b1, b2 = blocks[i], blocks[j]
            x1, y1, x2, y2 = b1[0], b1[1], b2[0], b2[1]
            p = [sympy.solve(
                [(x - x1) ** 2 + (y - y1) ** 2 - (1 - x) ** 2, (x - x2) ** 2 + (y - y2) ** 2 - (1 - x) ** 2],
                [x, y]), sympy.solve(
                [(x - x1) ** 2 + (y - y1) ** 2 - (1 + y) ** 2, (x - x2) ** 2 + (y - y2) ** 2 - (1 + y) ** 2],
                [x, y]), sympy.solve(
                [(x - x1) ** 2 + (y - y1) ** 2 - (1 + x) ** 2, (x - x2) ** 2 + (y - y2) ** 2 - (1 + x) ** 2],
                [x, y]), sympy.solve(
                [(x - x1) ** 2 + (y - y1) ** 2 - (1 - y) ** 2, (x - x2) ** 2 + (y - y2) ** 2 - (1 - y) ** 2],
                [x, y])]
            k = 0
            for p_ in p:
                for p__ in p_:
                    if 1 >= p__[0] >= -1 and 1 >= p__[1] >= -1:
                        if k == 0:
                            r_ = 1 - p__[0]
                        elif k == 1:
                            r_ = 1 + p__[1]
                        elif k == 2:
                            r_ = 1 + p__[0]
                        elif k == 3:
                            r_ = 1 - p__[1]
                        if 1 >= r_ >= 0:
                            p_ = p__
                            if test([r_, p_]):
                                r.append(r_)
                                pos.append(p_)
                            break
                k += 1
            j += 1
        i += 1
    result = max_of_r()
    if result is not None:
        return print_res()
    # for more blocks
    # todo


def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.
    
    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """

    # The following is an example implementation.
    max_circle = get_max(blockers)
    circles = []
    r_rate = 0.25

    def create_circles(rate):
        for circle_index in range(m):
            if  circle_index==0:
                circles.append((max_circle[1][0], max_circle[1][1], max_circle[0]))
                continue
            if circle_index == m-1:
                rate = 0.1
            x = random.random()*2 - 1
            y = random.random()*2 - 1
            r = random.random()*rate
            circles.append((x, y, r))
            while not validate(circles, blockers):
                x = random.random()*2 - 1
                y = random.random()*2 - 1
                r = random.random()*rate
                circles[circle_index] = (x, y, r)
        return circles

    return create_circles(r_rate)
    # todo
    circles_group = []
    max_sum, pos = 0, 0
    for index in range(2):
        tmp = 0
        circles = create_circles(r_rate)
        circles_group.append(circles)
        for circle in circles:
            tmp += circle[2]
        if tmp > max_sum:
            max_sum = tmp
            pos = index
    return circles_group[pos]
