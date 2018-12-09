import fileinput
import re
from collections import defaultdict
from string import ascii_uppercase

r = re.compile(r'^Step (?P<requisite>[A-Z]) must be finished before step (?P<step>[A-Z]) can begin.$')

def parse(line):
    m = r.match(line)
    return m.group('step'), m.group('requisite')

def part1():
    requisite_map = defaultdict(list)
    for l in fileinput.input():
        step, req = parse(l)
        requisite_map[step].append(req)
    
    pending_steps = set()
    pending_steps.update(requisite_map.keys())
    for v in requisite_map.values():
        pending_steps.update(v)

    completed_steps = []

    pending_steps = sorted(pending_steps)
    while pending_steps:
        for step in pending_steps:
            requisites = requisite_map[step]
            if all(req in completed_steps for req in requisites):
                completed_steps.append(step)
                pending_steps.remove(step)
                break
    print(''.join(completed_steps))


def part2():

    workers = 5
    extra_work = 60
    requisite_map = defaultdict(list)
    for l in fileinput.input():
        step, req = parse(l)
        requisite_map[step].append(req)
    
    pending_steps = set()
    pending_steps.update(requisite_map.keys())
    for v in requisite_map.values():
        pending_steps.update(v)

    completed_steps = []
    current_work = {}

    pending_steps = pending_steps
    time = 0
    while pending_steps or current_work:
        # step time
        time += 1
        current_work = {k: v-1 for k, v in current_work.items()}
        
        # complete work
        just_finished_steps = [id for id, v in current_work.items() if v == 0]
        if len(just_finished_steps) > 1:
            print("more than one step finished now!", just_finished_steps, pending_steps)
        for j in just_finished_steps:
            del current_work[j]
            completed_steps.append(j)


        # find steps that can be started
        available_steps = []
        for step in pending_steps:
            requisites = requisite_map[step]
            if all(req in completed_steps for req in requisites):
                available_steps.append(step)

        available_steps = sorted(available_steps)

        # if any workers are free, they take new work
        for step in available_steps:
            if len(current_work) < workers:
                print('worker available at time', time, 'can work on', available_steps)
                current_work[step] = ascii_uppercase.index(step) + 1 + extra_work
                pending_steps.remove(step)

    print(time - 1)
part2()