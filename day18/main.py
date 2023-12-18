def part_one(filename: str) -> str:
    data = get_data(filename)
    return str(calculate_area(data))


def calculate_area(data: list) -> int:
    directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    boundary_points = [(0, 0)]
    size_of_boundary = 0
    for line in data:
        direction, steps, _ = line
        dr, dc = directions[direction]
        size_of_boundary += int(steps)
        boundary_points.append((boundary_points[-1][0] + dr * int(steps), boundary_points[-1][1] + dc * int(steps)))
    shoelace_sum = 0
    for i in range(len(boundary_points) - 1):
        shoelace_sum += boundary_points[i][0] * (boundary_points[i + 1][1] - boundary_points[i - 1][1])
    shoelace = abs(shoelace_sum) / 2
    inner_points = shoelace - size_of_boundary // 2 + 1
    result = int(inner_points + size_of_boundary)
    return result


def part_two(filename: str) -> str:
    data = get_data_part2(filename)
    return str(calculate_area(data))


def get_data(filename: str) -> list:
    with open(filename, "r") as file:
        return [line.strip().split(" ") for line in file.readlines()]


def get_data_part2(filename: str) -> list:
    directions = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
    data = get_data(filename)
    for i in range(len(data)):
        color = data[i][2]
        data[i][1] = int(color[2:7], 16)
        data[i][0] = directions[color[-2]]
    return data


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
