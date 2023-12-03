import re

GEAR = '*'
DOT = '.'


def part_one(filename: str) -> str:
    result = 0
    pattern = re.compile(r'\d+')
    with open(filename) as file:
        lines = file.readlines()
        for i in range(len(lines)):
            matches = pattern.finditer(lines[i])
            for match in matches:
                int_val = int(match.group())
                start_index, end_index = match.start(), match.end()
                if check_surrounding(lines, i, start_index, end_index):
                    result += int_val
    return str(result)


def part_two(filename: str) -> str:
    result = 0
    pattern = re.compile(r'\*')
    with open(filename) as file:
        lines = file.readlines()
        for i in range(len(lines)):
            matches = pattern.finditer(lines[i])
            for match in matches:
                start_index, end_index = match.start(), match.end()
                result += find_numbers_surrounding(lines, i, start_index)
    return str(result)


def find_numbers_surrounding(lines: list, i: int, gear_index: int):
    pattern = re.compile(r'\d+')
    numbers = []
    surrounding_numbers = []
    for x in range(-1, 2):
        if i + x < 0 or i + x >= len(lines):
            continue
        matches = pattern.finditer(lines[i + x])
        for match in matches:
            int_val = int(match.group())
            start_index, end_index = match.start(), match.end()
            numbers.append((int_val, start_index, end_index - 1))

    for number in numbers:
        if number[2] == gear_index - 1 or number[1] == gear_index + 1 or number[1] <= gear_index <= number[2]:
            surrounding_numbers.append(number)
            if len(surrounding_numbers) == 2:
                break

    if len(surrounding_numbers) == 2:
        print(surrounding_numbers[0][0], surrounding_numbers[1][0])
        return surrounding_numbers[0][0] * surrounding_numbers[1][0]
    return 0


def check_surrounding(lines: list, i: int, start: int, end: int):
    for j in range(start - 1, end + 1):
        for x in range(-1, 2):
            if check_cell(lines, i + x, j):
                return True
    return False


def check_cell(lines: list, i: int, j: int) -> bool:
    # True indicates that there is a symbol in the cell
    if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[i]) - 1:
        return False
    if lines[i][j] != DOT and not lines[i][j].isdigit():
        return True
    return False


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
