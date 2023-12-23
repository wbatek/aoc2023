SLOPE_DIRECTIONS = {
    '>': 'R',
    '<': 'L',
    '^': 'U',
    'v': 'D'
}

MOVE_TO_DIRECTION = {
    (-1, 0): 'U',
    (1, 0): 'D',
    (0, 1): 'R',
    (0, -1): 'L'
}


def part_one(filename):
    grid = get_data(filename)
    start = find_start(grid)
    finish = find_finish(grid)
    return str(bfs(grid, start, finish))


def part_two(filename):
    grid = replace_slopes(get_data(filename))
    start, finish = find_start(grid), find_finish(grid)
    points_3 = get_points_with_3(grid, start, finish)
    print(points_3)
    graph = {point: {} for point in points_3}

    for point in points_3:
        queue = [(point, 0)]
        visited = {point}

        while queue:
            pos, steps = queue.pop(0)
            r, c = pos

            if steps != 0 and (r, c) in points_3:
                graph[point][(r, c)] = steps
                continue

            for rd, cd in MOVE_TO_DIRECTION.keys():
                new_r = r + rd
                new_c = c + cd
                if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[new_r]) or (new_r, new_c) in \
                        visited or grid[new_r][new_c] == '#':
                    continue
                queue.append(((new_r, new_c), steps + 1))
                visited.add((new_r, new_c))

    seen = set()

    return str(dfs(start, finish, seen, graph))


def dfs(point: tuple, finish: tuple, seen: set, graph: dict):
    if point == finish:
        return 0

    m = -float('inf')
    seen.add(point)
    for nx in graph[point]:
        if nx not in seen:
            m = max(m, dfs(nx, finish, seen, graph) + graph[point][nx])
    seen.remove(point)

    return m


def get_points_with_3(grid: list, start: tuple, finish: tuple) -> list:
    points = [start, finish]
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == '#':
                continue
            neighbors = 0
            for rd, cd in MOVE_TO_DIRECTION.keys():
                new_r = y + rd
                new_c = x + cd
                if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[new_r]) or grid[new_r][
                    new_c] == '#':
                    continue
                neighbors += 1
            if neighbors >= 3:
                points.append((y, x))
    return points


def replace_slopes(grid: list) -> list:
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char in SLOPE_DIRECTIONS.keys():
                grid[y][x] = '.'
    return grid


def bfs(grid: list, start: tuple, finish: tuple) -> int:
    result = 0
    visited = set()
    visited.add(set)
    queue = [(start, 'D', 0, visited)]

    while queue:
        pos, direction, steps, v = queue.pop(0)
        v = set(v)
        r, c = pos

        if pos == finish:
            result = max(result, steps)
            continue

        for rd, cd in MOVE_TO_DIRECTION.keys():
            new_r = r + rd
            new_c = c + cd
            if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[new_r]) or (new_r, new_c) in v or \
                    grid[new_r][new_c] == '#':
                continue
            elif grid[new_r][new_c] == '.':
                queue.append(((new_r, new_c), MOVE_TO_DIRECTION[rd, cd], steps + 1, v))
                v.add((new_r, new_c))
            else:
                if MOVE_TO_DIRECTION[(rd, cd)] == SLOPE_DIRECTIONS[grid[new_r][new_c]]:
                    queue.append(((new_r, new_c), MOVE_TO_DIRECTION[rd, cd], steps + 1, v))
                    v.add((new_r, new_c))
    return result


def find_start(grid: list) -> tuple:
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == '.':
                return y, x


def find_finish(grid: list) -> tuple:
    row = grid[-1]
    for x, char in enumerate(row):
        if char == '.':
            return len(grid) - 1, x


def get_data(filename):
    with open(filename, "r") as file:
        data = file.read().splitlines()
    return [list(line) for line in data]


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
