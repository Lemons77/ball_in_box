import random
import sympy
from ball_in_box.validate import validate

__all__ = ['ball_in_box']
"""
def get_max(blocks):
    from sympy.abc import x, y

    # area
    dx, dy = [-1.0, 1.0], [-1.0, 1.0]
    #blocks = []
    block_num = len(blocks)
    result = []

    def print_res():
        print("area: \n", dx, dy)
        print("blocks: \n", blocks)
        print("max circle: \n", result)
        return result

    def test(res):
        covering = False
        for b in blocks:
            if (b[0] - res[1][0]) ** 2 + (b[1] - res[1][1]) ** 2 < res[0] ** 2:
                covering = True
        return covering
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
"""

def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.
    
    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """

    # The following is an example implementation.
#    max_circle = get_max(blockers)
    circles = []
    for circle_index in range(m):
        #if  circle_index==0:
         #   circles.append((max_circle[1][0], max_circle[1][1], max_circle[0]))
          #  continue
        x = random.random()*2 - 1
        y = random.random()*2 - 1
        r = random.random()+0.25

        circles.append((x, y, r))
        while not validate(circles, blockers):
            x = random.random()*2 - 1
            y = random.random()*2 - 1
            r = random.random()+0.25
            circles[circle_index] = (x, y, r)


        circle_index += 1
    i=0.0
    max=0.0
    while i<10:
        a=0.0
        for circle in circles:
            a+=circle[2]**2
        if a>max:
            max=a
        circles = []
        for circle_index in range(5):
            # if  circle_index==0:
            #   circles.append((max_circle[1][0], max_circle[1][1], max_circle[0]))
            #  continue
            x = random.random() * 2 - 1
            y = random.random() * 2 - 1
            r = random.random() + 0.25

            circles.append((x, y, r))
            while not validate(circles, blockers):
                x = random.random() * 2 - 1
                y = random.random() * 2 - 1
                if circle_index==5:
                    r = random.random()+0.1
                else:
                     r = random.random() +0.25
                circles[circle_index] = (x, y, r)

            circle_index += 1
        i+=1
    return circles
