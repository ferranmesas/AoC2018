import fileinput
from collections import Counter

def tick(forest):
    nextforest = []
    for i, row in enumerate(forest):
        nextrow = []
        for j, cell in enumerate(row):
            neighbours = Counter()
            for ii in range(max(i-1, 0), min(i+2, len(forest))):
                for jj in range(max(j-1, 0), min(j+2, len(row))):
                    if i == ii and j == jj:
                        continue
                    neighbours.update(forest[ii][jj])
            
            nextcell = cell
            if cell == '.' and neighbours['|'] >= 3:
                nextcell = '|'
            elif cell == '|' and neighbours['#'] >= 3:
                nextcell = '#'
            elif cell == '#' and (neighbours['#'] == 0 or neighbours['|'] == 0):
                nextcell = '.'

            nextrow.append(nextcell)
        nextforest.append(nextrow)
    return nextforest

def part1():
    forest = [list(line.strip()) for line in fileinput.input()]

    print('Initial state')
    print(*(''.join(f) for f in forest), sep='\n')
    for iteration in range(10):
        forest = tick(forest)
        print('iteration', iteration + 1)
        print(*(''.join(f) for f in forest), sep='\n')
    
    final = Counter()
    for row in forest:
        final.update(row)
    
    print(final['#'] * final['|'])
    
def part2():
    limit = 1000000000
    forest = [list(line.strip()) for line in fileinput.input()]

    states = [forest]
    loop_length = limit
    for iteration in range(limit):
        forest = tick(forest)
        try:
            prev = states.index(forest)
        except ValueError:
            states.append(forest)
        else:
            loop_length = iteration - prev + 1
            break

    remaining_iterations = limit - prev

    index = prev + remaining_iterations % loop_length
    
    final = Counter()
    for row in states[index]:
        final.update(row)
    print(final['#'] * final['|'])

part2()