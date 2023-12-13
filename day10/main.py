DIRECTIONS = ['U', 'D', 'L', 'R']
AVAILABLE_MOVES = {
    '-': [('L', ['L', 'F', '-']), ('R', ['J', '7', '-'])],
    '|': [('U', ['7', 'F', '|']), ('D', ['L', 'J', '|'])],
    'L': [('U', ['|', '7', 'F']), ('R', ['-', '7', 'J'])],
    'J': [('U', ['|', '7', 'F']), ('L', ['-', 'F', 'L'])],
    '7': [('D', ['|', 'L', 'J']), ('L', ['-', 'F', 'L'])],
    'F': [('D', ['|', 'J', 'L']), ('R', ['-', '7', 'J'])],
    '.': []
}
SYMBOLS = ['-', '|', 'L', 'J', '7', 'F']


def part_one(filename: str) -> str:
    grid = get_data(filename)
    s_index = [(i, j) for i, row in enumerate(grid) for j, value in enumerate(row) if value == 'S'][0]
    loop_indices = get_loop_indices(grid, s_index)
    return str(len(loop_indices) // 2)


def part_two(filename: str) -> str:
    grid = get_data(filename)
    s_index = [(i, j) for i, row in enumerate(grid) for j, value in enumerate(row) if value == 'S'][0]
    loop_indices = get_loop_indices(grid, s_index)
    result = 0
    for i in range(len(grid)):
        left = 0
        for j in range(len(grid[0])):
            if (i, j) not in loop_indices and left % 2 == 1:
                result += 1
            if grid[i][j] in ['|', 'L', 'J'] and (i, j) in loop_indices:
                left += 1

    return str(result)


def print_loop(grid: list, loop_indices: list):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in loop_indices:
                print(grid[i][j], end='')
            else:
                print(' ', end='')
        print()


def get_loop_indices(grid: list, s_index: tuple) -> list:
    loop_indices = [s_index]
    current_index = s_index
    while current_index != s_index or len(loop_indices) == 1:
        if len(loop_indices) == 1:
            # we are in Start position
            for symbol in SYMBOLS:
                grid[s_index[0]][s_index[1]] = symbol
                neighbour_indices = get_next_index(grid, s_index)
                if neighbour_indices is None:
                    continue
                else:
                    current_index = neighbour_indices[0] if neighbour_indices[0] not in loop_indices else \
                        neighbour_indices[1]
                    loop_indices.append(current_index)
                    break
        else:
            neighbour_indices = get_next_index(grid, current_index)
            if neighbour_indices[0] in loop_indices and neighbour_indices[1] in loop_indices:
                break
            current_index = neighbour_indices[0] if neighbour_indices[0] not in loop_indices else neighbour_indices[1]
            loop_indices.append(current_index)
    return loop_indices


def get_next_index(grid: list, current_index: tuple) -> list | None:
    current_value = grid[current_index[0]][current_index[1]]
    current_moves = AVAILABLE_MOVES[current_value]
    indices = []
    for direction in DIRECTIONS:
        if direction in [x[0] for x in current_moves]:
            found_tuple = next((item for item in current_moves if item[0] == direction), None)
            indices.append(get_next_index_for_direction(grid, current_index, direction, found_tuple[1]))

    if indices[0] is None or indices[1] is None:
        return None
    if len(indices) == 2:
        return indices
    return None


def get_next_index_for_direction(grid: list, current_index: tuple, direction: str, current_moves) -> tuple | None:
    if direction == 'U':
        if current_index[0] - 1 < 0:
            return None

        if grid[current_index[0] - 1][current_index[1]] in current_moves:
            return current_index[0] - 1, current_index[1]
    elif direction == 'D':
        if current_index[0] + 1 > len(grid) - 1:
            return None
        if grid[current_index[0] + 1][current_index[1]] in current_moves:
            return current_index[0] + 1, current_index[1]
    elif direction == 'L':
        if current_index[1] - 1 < 0:
            return None

        if grid[current_index[0]][current_index[1] - 1] in current_moves:
            return current_index[0], current_index[1] - 1
    elif direction == 'R':
        if current_index[1] + 1 > len(grid[0]) - 1:
            return None

        if grid[current_index[0]][current_index[1] + 1] in current_moves:
            return current_index[0], current_index[1] + 1
    return None


def get_data(filename: str) -> list:
    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()]
    grid = []
    for i in range(len(lines)):
        grid.append([x for x in lines[i]])
    return grid


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
