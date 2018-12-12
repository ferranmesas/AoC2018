import fileinput
from collections import defaultdict

def part1(steps=20):
    i = iter(fileinput.input())
    make_state = lambda: defaultdict(lambda: '.')

    string_state = next(i).strip().split()[2]
    

    next(i)
    transitions = defaultdict(lambda: '.')
    for line in i:
        frm, _, to = line.strip().split()
        transitions[tuple(frm)] = to

    state = make_state()
    for idx, char in enumerate(string_state):
        if char == '#':
            state[idx] = '#'
    
    for z in range(steps):
        minx = min(state.keys())
        maxx = max(state.keys())
        next_state = make_state()
        for x in range(minx-2, maxx+3):
            neigbourhood = (state[x-2], state[x-1], state[x], state[x+1], state[x+2])
            if transitions[neigbourhood] == '#':
                next_state[x] = '#'
        state = next_state

    return sum(state.keys())

def part2():
    generations = 50000000000
    # "experimentally" determined. I can't prove these are right though.
    steady_state_score_generation = 92
    score_increase_by_generation = 186
    initial_score = part1(steady_state_score_generation)
    
    return initial_score + (generations - steady_state_score_generation) * score_increase_by_generation
print(part2())