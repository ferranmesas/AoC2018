import fileinput
import re

class Star():
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
    
    def step(self):
        self.x += self.dx
        self.y += self.dy
    
    def unstep(self):
        self.x -= self.dx
        self.y -= self.dy

    def __repr__(self):
        return f'Star({self.x}, {self.y}, {self.dx}, {self.dy})'

parser = re.compile(r'^position=< *(-?[0-9]+),  *(-?[0-9]+)> velocity=< *(-?[0-9]+),  *(-?[0-9]+)>$')

def get_bbox(stars):
    minx = min(s.x for s in stars)
    maxx = max(s.x for s in stars)
    miny = min(s.y for s in stars)
    maxy = max(s.y for s in stars)
    return minx, maxx, miny, maxy

def render(stars):
    minx, maxx, miny, maxy = get_bbox(stars)
    dx = maxx - minx
    dy = maxy - miny
    text_box = [['.'] * (dx + 1) for _ in range(dy+1)]

    for s in stars:
        text_box[s.y - miny][s.x - minx] = '#'
    return '\n'.join(''.join(line) for line in text_box)
    
def solve():
    stars = []
    for line in fileinput.input():
        s = Star(*map(int, parser.match(line).groups()))
        stars.append(s)

    steps = 0
    best_bbox_area = float('infinity')
    while True:
        minx, maxx, miny, maxy = get_bbox(stars)

        bbox_area = abs(maxx - minx) + abs(maxy - miny)
        if bbox_area > best_bbox_area:
            for s in stars:
                s.unstep()
            print(render(stars))
            print(steps - 1)
            break
        best_bbox_area = bbox_area

        for s in stars:
            s.step()
        steps += 1
solve()