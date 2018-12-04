import fileinput
import re
import datetime
from collections import defaultdict

r = re.compile(r'^\[(\d+-\d+-\d+ \d+:\d+)](?: Guard #(\d+))? (falls asleep|wakes up|begins shift)$')

def parse(line):
    d, id, event = r.match(line).groups()
    return datetime.datetime.strptime(d, '%Y-%m-%d %H:%M'), event, id and int(id)

def part1():
    guards_total = defaultdict(int)
    guards = defaultdict(lambda: defaultdict(int))
    parsed = sorted(parse(line) for line in fileinput.input())

    id = None
    sleepy_time = None
    for date, event, newid in parsed:
        if event == 'begins shift':
            id = newid
        if event == 'falls asleep':
            sleepy_time = date

        if event == 'wakes up':
            for m in range(sleepy_time.minute, date.minute):
                guards[id][m] += 1
                guards_total[id] += 1

    most_sleepy_guard_id, _ = sorted(guards_total.items(), key=lambda g:g[1], reverse=True)[0]
    most_sleepy_minute_of_most_sleepy_guard, _ = sorted(guards[most_sleepy_guard_id].items(), key=lambda m:m[1], reverse=True)[0]
    print(most_sleepy_guard_id * most_sleepy_minute_of_most_sleepy_guard)

def part2():
    guards = defaultdict(int)
    parsed = sorted(parse(line) for line in fileinput.input())

    id = None
    sleepy_time = None
    for date, event, newid in parsed:
        if event == 'begins shift':
            id = newid
        if event == 'falls asleep':
            sleepy_time = date

        if event == 'wakes up':
            for m in range(sleepy_time.minute, date.minute):
                guards[(id, m)] += 1

    (most_sleepy_guard_id, most_sleepy_minute), _= sorted(guards.items(), key=lambda g: g[1], reverse=True)[0]
    print(most_sleepy_guard_id * most_sleepy_minute)

part2()
