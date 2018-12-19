import json
import fileinput
from funcs import funcs_by_name

def run_program(ip, program, registers):
    registers[ip] = -1
    while True:
        funcs_by_name["addi"](registers, ip, 1, ip) 
        try:
            opcode, args = program[registers[ip]]
            funcs_by_name[opcode](registers, *args)
        except:
            return

def parse():
    input = fileinput.input()
    ip = int(next(input).split()[1])
    program = []
    for line in input:
        opcode, *args = line.split()
        program.append((opcode, [int(x) for x in args]))
    return ip, program

def part1():
    ip, program = parse()
    registers = [0] * 6
    run_program(ip, program, registers)
    print(registers[0])

def part2():
    ip, program = parse()
    registers = [0] * 6
    registers[0] = 1
    run_program(ip, program, registers)
    print(registers[0])

part2()