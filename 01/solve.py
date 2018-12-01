with open('input.txt') as f:
  print(sum(map(int, f.readlines())))

import itertools
with open('input.txt') as f:
  nums = map(int, f.readlines())
  seen = set()
  count = 0
  for n in itertools.cycle(nums):
    if count in seen:
      print(count)
      break
    seen.add(count)
    count += n
    
