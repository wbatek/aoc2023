import heapq


def part_one(filename: str) -> str:
    grid = get_data(filename)
    return str(dijkstra_part1(grid))


def part_two(filename: str) -> str:
    grid = get_data(filename)
    return str(dijkstra_part2(grid))


def dijkstra_part1(grid: list) -> dict:
    seen = set()
    # heat loss, row, column, direction row, direction column, number of steps in current direction
    priority_queue = [(0, 0, 0, 0, 0, 0)]
    while priority_queue:
        heat_loss, row, column, dr, dc, steps = heapq.heappop(priority_queue)

        if row == len(grid) - 1 and column == len(grid[row]) - 1:
            return heat_loss

        if (row, column, dr, dc, steps) in seen:
            continue

        seen.add((row, column, dr, dc, steps))

        if steps < 3 and (dr, dc) != (0, 0):
            if 0 <= row + dr < len(grid) and 0 <= column + dc < len(grid[0]):
                heapq.heappush(priority_queue, (heat_loss + grid[row + dr][column + dc],
                                                row + dr, column + dc, dr, dc, steps + 1))

        for row_dir, column_dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (row_dir, column_dir) != (-dr, -dc) and (row_dir, column_dir) != (dr, dc):
                if 0 <= row + row_dir < len(grid) and 0 <= column + column_dir < len(grid[0]):
                    heapq.heappush(priority_queue, (heat_loss + grid[row + row_dir][column + column_dir],
                                                    row + row_dir, column + column_dir, row_dir, column_dir, 1))


def dijkstra_part2(grid: list) -> dict:
    seen = set()
    # heat loss, row, column, direction row, direction column, number of steps in current direction
    priority_queue = [(0, 0, 0, 0, 0, 0)]
    while priority_queue:
        heat_loss, row, column, dr, dc, steps = heapq.heappop(priority_queue)

        if row == len(grid) - 1 and column == len(grid[row]) - 1 and steps >= 4:
            return heat_loss

        if (row, column, dr, dc, steps) in seen:
            continue

        seen.add((row, column, dr, dc, steps))

        if steps < 10 and (dr, dc) != (0, 0):
            if 0 <= row + dr < len(grid) and 0 <= column + dc < len(grid[0]):
                heapq.heappush(priority_queue, (heat_loss + grid[row + dr][column + dc],
                                                row + dr, column + dc, dr, dc, steps + 1))

        # (dr, dc) == (0, 0) to enable it on initial step of loop
        if steps >= 4 or (dr, dc) == (0, 0):
            for row_dir, column_dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (row_dir, column_dir) != (-dr, -dc) and (row_dir, column_dir) != (dr, dc):
                    if 0 <= row + row_dir < len(grid) and 0 <= column + column_dir < len(grid[0]):
                        heapq.heappush(priority_queue, (heat_loss + grid[row + row_dir][column + column_dir],
                                                        row + row_dir, column + column_dir, row_dir, column_dir, 1))


def get_data(filename: str) -> list:
    with open(filename, "r") as file:
        return [[int(cell) for cell in line.strip()] for line in file.readlines()]


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
