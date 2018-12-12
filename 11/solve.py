import fileinput

grid_size = 300

def make_grid(serial):
    grid = []
    for x in range(1, grid_size+1):
        rack = []
        for y in range(1, grid_size+1):
            power_level = (((x + 10) * y) + serial) * (x + 10)
            power_level = (power_level % 1000) // 100
            rack.append(power_level - 5)
        grid.append(rack)
    return grid

def solve1(serial):
    grid = make_grid(serial)
    
    best_sum = float('-infinity')
    best_coords = None
    for x in range(grid_size - 1):
        for y in range(grid_size - 1):
            current_sum = 0
            for xx in (-1, 0, 1):
                for yy in (-1, 0, 1):
                    current_sum += grid[x+xx][y+yy]
            if current_sum  > best_sum:
                best_sum = current_sum
                best_coords = (x, y)
    return ','.join(str(x) for x in best_coords)

def solve2(serial):
    grid = make_grid(serial)
    summed_areas = [[0] * grid_size for _ in range(grid_size)]
    for x in range(grid_size):
        for y in range(grid_size):
            if x > 0 and y > 0:
                summed_areas[x][y] = grid[x][y] + summed_areas[x-1][y] + summed_areas[x][y-1] - summed_areas[x-1][y-1]
            elif x > 0:
                summed_areas[x][y] = grid[x][y] + summed_areas[x-1][y]
            elif y > 0:
                summed_areas[x][y] = grid[x][y] + summed_areas[x][y-1]
            else:
                summed_areas[x][y] = grid[x][y]

    best_sum = float('-infinity')
    best_coords = None
    for z in range(1, grid_size+1): 
        for x in range(grid_size - 1):
            for y in range(grid_size - 1):
                if x + z >= grid_size or y + z >= grid_size:
                    break
                current_sum = summed_areas[x][y] + summed_areas[x+z][y+z] - summed_areas[x+z][y] - summed_areas[x][y+z]
                if current_sum  > best_sum:
                    best_sum = current_sum
                    best_coords = (x+2, y+2, z)

    return ','.join(str(x) for x in best_coords)
    
print(solve2(5093))