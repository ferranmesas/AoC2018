def solve1(skip):
    recipes = [3, 7]
    elves = [0, 1]
    def calc(recipe1, recipe2):
        a, b = divmod(recipe1 + recipe2, 10)
        if a:
            return a, b
        else:
            return b, 

    while len(recipes) < skip + 12:
        new_recipes = calc(recipes[elves[0]], recipes[elves[1]])
        recipes.extend(new_recipes)
        elves = [(elf + 1 + recipes[elf]) % len(recipes) for elf in elves]

    return ''.join(str(x) for x in recipes[skip:skip+10])

def solve2(match):
    digits = [int(x) for x in str(match)]
    recipes = [3, 7]
    elves = [0, 1]
    def calc(recipe1, recipe2):
        a, b = divmod(recipe1 + recipe2, 10)
        if a:
            return a, b
        else:
            return b, 

    test_index = 0
    while True:
        new_recipes = calc(recipes[elves[0]], recipes[elves[1]])
        recipes.extend(new_recipes)
        elves = [(elf + 1 + recipes[elf]) % len(recipes) for elf in elves]
        while test_index < len(recipes) - len(digits):
            if digits == recipes[test_index:test_index+len(digits)]:
                return test_index
            test_index += 1

print(solve1(430971))
print(solve2(430971))

