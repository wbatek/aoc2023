def part_one(filename: str) -> str:
    result = 0
    bricks = get_data(filename)
    bricks.sort(key=lambda x: x[2])

    push_bricks(bricks)

    up, down = construct_up_and_down(bricks)

    for i, brick in enumerate(bricks):
        if all(len(down[j]) > 1 for j in up[i]):
            result += 1
    return str(result)


def push_bricks(bricks: list) -> None:
    for i, brick in enumerate(bricks):
        bottom = 1
        for s_brick in bricks[:i]:
            if is_overlapping(brick, s_brick):
                bottom = max(bottom, s_brick[5] + 1)
        brick[5] -= brick[2] - bottom
        brick[2] = bottom
    bricks.sort(key=lambda x: x[2])


def construct_up_and_down(bricks: list) -> tuple:
    up = {i: set() for i in range(len(bricks))}
    down = {i: set() for i in range(len(bricks))}

    for i, brick in enumerate(bricks):
        for j, s_brick in enumerate(bricks[:i]):
            if is_overlapping(brick, s_brick) and brick[2] == s_brick[5] + 1:
                up[j].add(i)
                down[i].add(j)
    return up, down


def is_overlapping(brick1: list, brick2: list) -> bool:
    return max(brick1[0], brick2[0]) <= min(brick1[3], brick2[3]) and max(brick1[1], brick2[1]) <= min(brick1[4], brick2[4])


def part_two(filename: str) -> str:
    result = 0
    bricks = get_data(filename)
    bricks.sort(key=lambda x: x[2])

    push_bricks(bricks)

    up, down = construct_up_and_down(bricks)

    for i in range(len(bricks)):
        queue = [j for j in up[i] if len(down[j]) == 1]
        res = set(queue)
        res.add(i)
        while queue:
            brick = queue.pop()
            for j in up[brick]:
                if j not in res:
                    if down[j].issubset(res):
                        res.add(j)
                        queue.append(j)
        result += len(res) - 1
    return str(result)


def get_data(filename: str) -> list:
    with open(filename, "r") as file:
        data = file.read().splitlines()
    r = []
    for line in data:
        line = line.replace("~", ",")
        r.append(list(map(int, line.split(","))))
    return r


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
