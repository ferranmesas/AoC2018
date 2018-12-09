import fileinput
import re

class Node():
    def __init__(self, stream):
        nchildren = next(stream)
        nmeta = next(stream)
        self.children = [Node(stream) for _ in range(nchildren)]
        self.meta = [next(stream) for _ in range(nmeta)]

    def print_node(self, indent=0):
        print(' ' * indent + 'Node with meta', self.meta)
        for c in self.children:
            c.print_node(indent+2)

    def sum_metas(self):
        return sum(c.sum_metas() for c in self.children) + sum(self.meta)

    def second_check(self):
        if not self.children:
            return sum(self.meta)
        
        result = 0
        for m in self.meta:
            try:
                result += self.children[m - 1].second_check()
            except IndexError:
                pass
        return result

def part1():
    numbers = iter(map(int, fileinput.input().readline().strip().split()))
    root = Node(numbers)
    print(root.sum_metas())

def part2():
    numbers = iter(map(int, fileinput.input().readline().strip().split()))
    root = Node(numbers)
    print(root.second_check())

part2()