import fileinput
import itertools
from collections import defaultdict

def manhattan(x, y, xx, yy):
    return abs(x -xx) + abs(y - yy)

def minmax(seq):
    s = list(seq)
    return min(s), max(s)

def part1():
    coords = [[id,[int(x), int(y)]] for id, [x, y] in zip(itertools.count(), map(lambda l: l.split(', '), fileinput.input()))]

    minx, maxx = minmax(x for id, [x, y] in coords)
    miny, maxy = minmax(y for id, [x, y] in coords)
    
    # assumming all cells touching the edge even with this margin will be infinite (may not be true!)
    margin = 50

    cells = {}
    for i in range(minx - margin, maxx + margin):
        for j in range(miny - margin, maxy + margin):
            isdraw = False
            best = float("infinity")
            best_id = -1
            for id, (xx, yy) in coords:
                d = manhattan(i, j, xx, yy)
            
                if d == best:
                    best_id = -1
                
                if d < best:
                    best = d
                    best_id = id
            cells[(i, j)] = best_id
    
    edge_cells = set()
    for i in range(minx - margin, maxx + margin):
        edge_cells.add(cells[(i, miny - margin)])
        edge_cells.add(cells[(i, maxy + margin - 1)])
    for j in range(miny - margin, maxy + margin):
        edge_cells.add(cells[(minx - margin, j)])
        edge_cells.add(cells[(maxx + margin -1, j)])

    cells_by_id = defaultdict(list)
    for k, v in cells.items():
        if v == -1 or v in edge_cells:
            continue
        cells_by_id[v].append(k)

    sorted_cells = sorted(((id, len(amt)) for id, amt in cells_by_id.items()), key=lambda x: x[1], reverse=True)
    
    print(sorted_cells[0][1])


def part2():
    coords = [[id,[int(x), int(y)]] for id, [x, y] in zip(itertools.count(), map(lambda l: l.split(', '), fileinput.input()))]

    minx, maxx = minmax(x for id, [x, y] in coords)
    miny, maxy = minmax(y for id, [x, y] in coords)
    
    # assumming all cells touching the edge even with this margin will be infinite (may not be true!)
    margin = 0

    cells = defaultdict(int)
    for i in range(minx - margin, maxx + margin):
        for j in range(miny - margin, maxy + margin):
            isdraw = False
            best = float("infinity")
            best_id = -1
            for id, (xx, yy) in coords:
                d = manhattan(i, j, xx, yy)
                cells[(i, j)] += d
    
    print(sum(1 for x in cells.values() if x < 10000))
part2()
