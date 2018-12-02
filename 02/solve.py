from collections import Counter

with open('input.txt') as f:
  twos = 0
  threes = 0
  for line in f.readlines():
    c = Counter(line)
    twos += 2 in c.values()
    threes += 3 in c.values()
  print(twos * threes)


from itertools import combinations

def distance(w1, w2):
  return sum(l1 != l2 for l1, l2 in zip(w1, w2))

def common_letters(w1, w2):
  return ''.join(l1 for l1, l2 in zip(w1, w2) if l1 == l2)

with open('input.txt') as f:
  lines = [l.strip() for l in f.readlines()]
  for w1, w2 in combinations(lines, 2):
    if distance(w1, w2) == 1:
      print(common_letters(w1, w2))
      break
