import fileinput
import networkx as nx
import datetime
from collections import defaultdict

moves = {
    'N': 1j,
    'S': -1j,
    'W': -1,
    'E': 1
}

def parse(line):
    d, id, event = r.match(line).groups()
    return datetime.datetime.strptime(d, '%Y-%m-%d %H:%M'), event, id and int(id)

def get_graph(string):
    string = string[1:-1]
    graph = nx.Graph()

    position = 0 + 0j
    pos_stack = []
    index = 0
    while index < len(string):
        char = string[index]
        index += 1
        if char in moves:
            newpos = position + moves[char]
            graph.add_edge(position, newpos)
            position = newpos
        elif char == '(':
            pos_stack.append((index, position))
        elif char == '|':
            position = pos_stack[-1][1]
        elif char == ')':
            pos_stack.pop()
    return graph

def part1(string):
    g = get_graph(string)
    lens = map(
        lambda x: len(x) - 1,
        nx.single_source_shortest_path(g, 0+0j).values()
    )
    print(max(lens))

def part2(string):
    g = get_graph(string)
    lens = map(
        lambda x: len(x) - 1,
        nx.single_source_shortest_path(g, 0+0j).values()
    )
    print(sum(1 for l in lens if l >= 1000))

for line in fileinput.input():
    string = line.strip()
    part1(string)
    part2(string)
