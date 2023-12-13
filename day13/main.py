def part_one(filename: str) -> str:
    grids = get_data(filename)
    result = 0
    for grid in grids:
        result += find_vertical_p1(grid)
        result += 100 * find_horizontal_p1(grid)
    return str(result)


def part_two(filename: str) -> str:
    grids = get_data(filename)
    result = 0
    for grid in grids:
        result += 100 * find_horizontal_p2(grid)
        result += find_vertical_p2(grid)
    return str(result)


def find_vertical_p2(grid: list):
    result = 0
    for i in range(1, len(grid[0])):
        is_matching = True
        bad = 0
        for j in range(len(grid)):
            if grid[j][i - 1] != grid[j][i]:
                bad += 1
        if is_matching and bad < 2:
            c1 = i - 1
            c2 = i
            one_side_length = min(c1 + 1, len(grid[0]) - c2)
            j = 0
            bad = 0
            for j in range(len(grid)):
                if grid[j][c1 + 1 - one_side_length:c1 + 1] != grid[j][c2:c2 + one_side_length][::-1]:
                    if check_only_one_differ(grid[j][c1 + 1 - one_side_length:c1 + 1],
                                             grid[j][c2:c2 + one_side_length][::-1]):
                        bad += 1
                    else:
                        bad += 2
            if bad == 1 and j == len(grid) - 1:
                return c1 + 1
    return result


def find_horizontal_p2(grid: list):
    result = 0
    for i in range(1, len(grid)):
        is_matching = True
        bad = 0
        for j in range(len(grid[0])):
            if grid[i - 1][j] != grid[i][j]:
                bad += 1
        if bad < 2 and is_matching:
            r1 = i - 1
            r2 = i
            one_side_length = min(r1 + 1, len(grid) - r2)
            j = 0
            for j in range(1, one_side_length):
                if grid[r1 - j] != grid[r2 + j]:
                    if check_only_one_differ(grid[r1 - j], grid[r2 + j]):
                        bad += 1
                    else:
                        bad += 2
            if bad == 1 and j == one_side_length - 1:
                return r1 + 1
    return result


def find_vertical_p1(grid: list):
    result = 0
    for i in range(1, len(grid[0])):
        is_matching = True
        correct = True
        for j in range(len(grid)):
            if grid[j][i - 1] != grid[j][i]:
                is_matching = False
                break
        if is_matching:
            c1 = i - 1
            c2 = i
            one_side_length = min(c1 + 1, len(grid[0]) - c2)
            j = 0
            for j in range(len(grid)):
                if grid[j][c1 + 1 - one_side_length:c1 + 1] != grid[j][c2:c2 + one_side_length][::-1]:
                    correct = False
                    break
            if correct and j == len(grid) - 1:
                return c1 + 1
    return result


def find_horizontal_p1(grid: list):
    result = 0
    for i in range(1, len(grid)):
        is_matching = True
        correct = True
        for j in range(len(grid[0])):
            if grid[i - 1][j] != grid[i][j]:
                is_matching = False
                break
        if is_matching:
            r1 = i - 1
            r2 = i
            one_side_length = min(r1 + 1, len(grid) - r2)
            j = 0
            for j in range(one_side_length):
                if grid[r1 - j] != grid[r2 + j]:
                    correct = False
                    break
            if correct and j == one_side_length - 1:
                return r1 + 1
    return result


def check_only_one_differ(first, second) -> bool:
    count = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            count += 1
    return count == 1


def get_data(filename: str):
    grids = []
    with open(filename, "r") as file:
        line = file.readline()
        grid = []
        while line:
            if line == "\n":
                grids.append(grid)
                grid = []
            else:
                grid.append(list(line.strip()))
            line = file.readline()
        grids.append(grid)
    return grids


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
