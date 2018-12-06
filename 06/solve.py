import fileinput
import itertools

def part1():
    coords = [[id,[int(x), int(y)]] for id, [x, y] in zip(itertools.count(), map(lambda l: l.split(', '), fileinput.input()))]
    print(coords)

def part2():
    line = fileinput.input().readline().strip()
    reactants = set(c.lower() for c in line)
    best = len(line)

    for r in reactants:
        line_copy = line.replace(r, '').replace(r.upper(), '')
        reduced = react(line_copy)
        if len(reduced) < best:
            best = len(reduced)
    print(best)

part1()
