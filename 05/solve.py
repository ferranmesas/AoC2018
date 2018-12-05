import fileinput

def react(polymer: str):
    stack = []
    for letter in polymer:
        if not stack:
            stack.append(letter)
            continue
        top = stack[-1]
        if top.lower() == letter.lower() and top != letter:
            stack.pop()
        else:
            stack.append(letter)

    return ''.join(stack)

def part1():
    line = fileinput.input().readline().strip()
    print(len(react(line)))

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

    # or print(reduce(lambda m, r: min(len(react(line.replace(r, '').replace(r.upper(), ''))), m), reactants, len(line)))

part2()
