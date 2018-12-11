import fileinput
import re

class Node():
    def __init__(self, value):
        self.value = value
        self.clockwise = self
        self.counterclockwise = self

    def insert_clockwise_after(self, other):
        old_cw = other.clockwise
        old_cw.counterclockwise = self
        self.clockwise = old_cw
        other.clockwise = self
        self.counterclockwise = other
    
    def remove_ccw(self):
    
        ccw = self.counterclockwise.counterclockwise
        self.counterclockwise = ccw
        ccw.clockwise = self
    
    def __str__(self):
        result = []   
        current = self
        while True:
            result.append(current.value)
            current = current.clockwise
            if self == current:
                break
        return " ".join(str(x) for x in result)
    

parser = re.compile(r'([0-9]+) players; last marble is worth ([0-9]+) points')

def part1(multiplier=1):
    players, last = map(int, parser.match(fileinput.input().readline()).groups())
    current = Node(0)
    scores = [0] * players
    last *= multiplier
    for i in range(1, last+1):
        current_player = (i) % players
        if i % 23 == 0:
            for _ in range(6):
                current = current.counterclockwise
            scores[current_player] += i + current.counterclockwise.value
            current.remove_ccw()
        else:
            n = Node(i)
            n.insert_clockwise_after(current.clockwise)
            current = n
    print(max(scores))


def part2():
    part1(100)

part2()