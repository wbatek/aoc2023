def part_one(filename: str) -> str:
    N = 64
    grid, start = get_data(filename)
    return str(fill(grid, start, N))


def part_two(filename: str) -> str:
    grid, start = get_data(filename)
    size = len(grid)
    N = 26501365

    grid_width = N // size - 1
    odd_grids = (grid_width // 2 * 2 + 1) ** 2
    even_grids = ((grid_width + 1) // 2 * 2) ** 2

    odd_points = fill(grid, start, size * 2 + 1)
    even_points = fill(grid, start, size * 2)

    corner_top = fill(grid, (size - 1, start[1]), size - 1)
    corner_right = fill(grid, (start[0], 0), size - 1)
    corner_bottom = fill(grid, (0, start[1]), size - 1)
    corner_left = fill(grid, (start[0], size - 1), size - 1)

    small_topright = fill(grid, (size - 1, 0), size // 2 - 1)
    small_topleft = fill(grid, (size - 1, size - 1), size // 2 - 1)
    small_bottomright = fill(grid, (0, 0), size // 2 - 1)
    small_bottomleft = fill(grid, (0, size - 1), size // 2 - 1)

    large_topright = fill(grid, (size - 1, 0), size * 3 // 2 - 1)
    large_topleft = fill(grid, (size - 1, size - 1), size * 3 // 2 - 1)
    large_bottomright = fill(grid, (0, 0), size * 3 // 2 - 1)
    large_bottomleft = fill(grid, (0, size - 1), size * 3 // 2 - 1)

    result = (odd_grids * odd_points + even_grids * even_points +
              corner_bottom + corner_left + corner_right + corner_top +
              (grid_width + 1) * (small_bottomleft + small_bottomright + small_topleft + small_topright) +
              grid_width * (large_bottomleft + large_bottomright + large_topleft + large_topright))
    return str(result)


def fill(grid: list, start: tuple, N: int) -> int:
    result = set()
    seen = {start}
    queue = [(start, N)]

    while queue:
        current, n = queue.pop(0)
        r, c = current
        if n % 2 == 0:
            result.add(current)
        if n == 0:
            continue

        for next_row, next_column in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if next_row < 0 or next_row >= len(grid) or next_column < 0 or next_column >= len(grid[0]) or \
                    grid[next_row][next_column] == "#" or (next_row, next_column) in seen:
                continue
            seen.add((next_row, next_column))
            queue.append(((next_row, next_column), n - 1))
    return len(result)


def get_data(filename: str) -> tuple:
    with open(filename, "r") as file:
        grid = [list(line.strip()) for line in file.readlines()]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                return grid, (i, j)
    return grid, None


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
