def part_one(filename: str) -> str:
    data = get_data(filename)
    roll(data)
    return str(calc_result(data))


def part_two(filename: str) -> str:
    data = get_data(filename)
    count = 0
    amount_of_cycles = 10 ** 9
    cached_values = {}
    while count < amount_of_cycles:
        count += 1
        for j in range(4):
            roll(data)
            data = rotate(data)
        after_cycle = tuple(tuple(row) for row in data)
        if after_cycle in cached_values:
            length = count - cached_values[after_cycle]
            amount = (amount_of_cycles - count) // length
            count += amount * length
        cached_values[after_cycle] = count
    return str(calc_result(data))

def calc_result(data: list) -> int:
    result = 0
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == 'O':
                result += len(data) - i
    return result


def roll(data: list):
    for i in range(1, len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'O':
                temp = i - 1
                while temp >= 0 and data[temp][j] != '#' and data[temp][j] != 'O':
                    temp -= 1
                if temp == i - 1 and data[temp][j] == 'O':
                    continue
                elif temp + 1 != i:
                    data[temp + 1][j] = 'O'
                    data[i][j] = '.'


def rotate(data: list):
    result = [['?' for _ in range(len(data))] for _ in range(len(data[0]))]
    for row in range(len(data)):
        for col in range(len(data[row])):
            result[col][len(data) - row - 1] = data[row][col]
    return result


def get_data(filename: str):
    with open(filename) as file:
        data = file.readlines()
    data = [list(line.strip()) for line in data]
    return data


def print_grid(grid: list):
    for row in grid:
        print(row)


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
