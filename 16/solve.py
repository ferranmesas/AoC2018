import json
from funcs import funcs

def part1():
    with open('input_part1.txt') as f:
        f = iter(f)
        total_matches = 0
        while True:
            try:
                before = json.loads(next(f).split(' ', 1)[1])
                instruction = [int(x) for x in next(f).split()]
                after = json.loads(next(f).split(' ', 1)[1])
                next(f)
                matches = 0
                for func in funcs:
                    result = before[:]
                    func(result, *instruction[1:])
                    if result == after:
                        matches += 1
                if matches >= 3:
                    total_matches += 1
            except StopIteration:
                break
        print(total_matches)

def part2():
    with open('input_part1.txt') as f:
        f = iter(f)
        possible_funcs = {}
        ops = []
        while True:
            try:
                before = json.loads(next(f).split(' ', 1)[1])
                instruction = [int(x) for x in next(f).split()]
                after = json.loads(next(f).split(' ', 1)[1])
                next(f)
                ops.append((before, instruction, after))
            except StopIteration:
                break
    
    for func in funcs:
        invalid_opcodes = set()
        for before, instruction, after in ops:
            registers = before[:]
            func(registers, *instruction[1:])
            if registers != after:
                invalid_opcodes.add(instruction[0])
        possible_funcs[func] = set(range(16)) - invalid_opcodes

    remaining_opcodes = set(range(16))
    opcode_mapping = {}
    while remaining_opcodes:
        for func, opcodes in possible_funcs.items():
            if f in opcode_mapping.values():
                continue
            remaining_opcodes_for_func = opcodes & remaining_opcodes
            if len(remaining_opcodes_for_func) == 1:
                opcode, = remaining_opcodes_for_func
                opcode_mapping[opcode] = func
                remaining_opcodes.remove(opcode)
    
    with open('input_part2.txt') as f:
        registers = [0] * 4
        for line in f:
            opcode, *args = map(int, line.split())
            opcode_mapping[opcode](registers, *args)

        print(registers[0])


part2()