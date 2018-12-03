import fileinput
import re
from collections import defaultdict

r = re.compile(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$')

def parse(line):
    return map(int, r.match(line).groups())

def part1():
    cells = defaultdict(int)
    for line in fileinput.input():
        id, l, t, w, h = parse(line)
        for x in range(l, l+w):
            for y in range(t, t+h):
                cells[(x, y)] += 1
    
    print(sum(v >= 2 for v in cells.values()))

def intervals_overlap(s1, l1, s2, l2):
    return (s1 < s2 + l2) and ( s1 + l1 > s2)

def areas_overlap(l1, t1, w1, h1, l2, t2, w2, h2):
    return (
        intervals_overlap(l1, w1, l2, w2) and
        intervals_overlap(t1, h1, t2, h2)
    )

def part2():
    claims = {}
    for line in fileinput.input():
        id, *coords = parse(line)
        claims[id] = coords

    for id, coords in claims.items():
        for otherid, othercoords in claims.items():
            if id == otherid:
                continue
            if areas_overlap(*coords, *othercoords):
                break
        else:
            print(id)
part2()