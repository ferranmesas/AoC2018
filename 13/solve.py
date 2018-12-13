import fileinput

directions = 'v<^>'

turns = {
    ('>', '/'): '^',
    ('>', '\\'): 'v',
    ('<', '/'): 'v',
    ('<', '\\'): '^',
    ('^', '/'): '>',
    ('^', '\\'): '<',
    ('v', '/'): '<',
    ('v', '\\'): '>',
}

class SomethingHappenedAtLocation(Exception):
    def __init__(self, y, x):
        self.x = x
        self.y = y

class Minecart():
    def __init__(self, char):
        self.next_turn = -1
        self.direction = char
        self.track_below = '|' if self.direction in 'v^' else '-'
        self.updated_this_tick = False

    def __str__(self):
        return self.direction

def parse(stream):
    grid = []
    minecarts = []
    for line in stream:
        row = []
        for char in line.strip('\n'):
            if char in directions:
                m = Minecart(char)
                row.append(m)
                minecarts.append(m)
            else:
                row.append(char)
        grid.append(row)
    return grid, minecarts

def print_tracks(tracks):
    for row in tracks:
        for c in row:
            print(c, end='')
        print()

def tick(grid, part=1):
    remaining_carts = 0
    last_cart_location = None
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if isinstance(cell, Minecart):
                minecart = cell
                if minecart.updated_this_tick:
                    continue
                # first, look where we're going to move
                next_cell_coords = None

                if minecart.direction == '<':
                    next_cell_coords = (i, j - 1)
                if minecart.direction == '>':
                    next_cell_coords = (i, j + 1)
                if minecart.direction == '^':
                    next_cell_coords = (i - 1, j)
                if minecart.direction == 'v':
                    next_cell_coords = (i + 1, j)
                
                # check what's there
                next_cell = grid[next_cell_coords[0]][next_cell_coords[1]]
                if isinstance(next_cell, Minecart):
                    if part == 1:
                        raise SomethingHappenedAtLocation(*next_cell_coords)
                    else:
                        # remove both carts
                        grid[next_cell_coords[0]][next_cell_coords[1]] = next_cell.track_below
                        grid[i][j] = cell.track_below
                        continue

                # copy current_state
                current_track = minecart.track_below
                current_direction = minecart.direction
                current_turn = minecart.next_turn

                next_direction = next_turn = None
                if next_cell in '-|':
                    next_direction = current_direction
                    next_turn = current_turn

                elif next_cell in '/\\':
                    next_direction = turns[(current_direction, next_cell)]
                    next_turn = current_turn
                
                elif next_cell == '+':
                    next_direction = directions[(directions.index(current_direction) + current_turn) % 4]
                    next_turn = ((minecart.next_turn + 2) % 3) - 1

                # update minecart
                minecart.updated_this_tick = True
                minecart.direction = next_direction
                minecart.track_below = next_cell
                minecart.next_turn = next_turn

                # update grid
                grid[i][j] = current_track
                grid[next_cell_coords[0]][next_cell_coords[1]] = minecart
                remaining_carts += 1
                last_cart_location = (i, j)
    
    if part == 2 and remaining_carts == 1:
        raise SomethingHappenedAtLocation(*last_cart_location)

                    

def solve(part):
    tracks, minecarts = parse(fileinput.input())
    while True:
        try:
            tick(tracks, part)
        except SomethingHappenedAtLocation as e:
            print(e.x, e.y)
            break

        for minecart in minecarts:
            minecart.updated_this_tick = False
    
solve(2)