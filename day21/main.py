def part_one(filename: str) -> str:
    N = 64
    grid, start = get_data(filename)
    queue = [start]
    for i in range(N):
        print(queue)
        q_size = len(queue)
        for _ in range(q_size):
            c = queue.pop(0)
            if c[0] < 0 or c[0] >= len(grid) or c[1] < 0 or c[1] >= len(grid[0]) or grid[c[0]][c[1]] == '#':
                continue
            else:
                if (c[0] + 1, c[1]) not in queue:
                    queue.append((c[0] + 1, c[1]))
                if (c[0] - 1, c[1]) not in queue:
                    queue.append((c[0] - 1, c[1]))
                if (c[0], c[1] + 1) not in queue:
                    queue.append((c[0], c[1] + 1))
                if (c[0], c[1] - 1) not in queue:
                    queue.append((c[0], c[1] - 1))
    cnt = 0
    for i in range(len(queue)):
        c = queue.pop(0)
        if c[0] < 0 or c[0] >= len(grid) or c[1] < 0 or c[1] >= len(grid[0]) or grid[c[0]][c[1]] == '#':
            continue
        else:
            cnt += 1
    return str(cnt)


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

    # with open("output2.txt", "w") as f:
    #     f.write(part_two(input_path))
