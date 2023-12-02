import re

word_to_digit = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def part_one(filename: str):
    elem_sum = 0
    with open(filename, "r") as x:
        line = x.readline()
        while line:
            first, last = get_digits(line)
            elem_sum += (10 * int(first) + int(last))
            line = x.readline()
    return str(elem_sum)


def part_two(filename: str):
    elem_sum = 0
    with open(filename, "r") as x:
        line = x.readline()
        while line:
            first, last = check(line)
            print(first, last)
            elem_sum += (10 * int(first) + int(last))
            line = x.readline()
    return str(elem_sum)


def get_digits(line: str) -> (str, str):
    match = re.findall(r'\d', line)
    if len(match) == 0:
        return -1, -1
    return match[0], match[-1]


def check(line: str) -> (int, int):
    number_pattern = re.compile('|'.join(map(re.escape, word_to_digit.keys())), re.IGNORECASE)
    matches = []
    start = 0
    while True:
        match = number_pattern.search(line, start)
        if match is None:
            break
        matches.append((match.group(0), match.start()))
        start = match.start() + 1
    first, last = get_digits(line)

    if len(matches) == 0:
        return int(first), int(last)
    if first == -1 and last == -1:
        return int(word_to_digit[matches[0][0]]), int(word_to_digit[matches[-1][0]])

    r_first = word_to_digit[matches[0][0]] if matches[0][1] < line.find(first) else first
    r_last = word_to_digit[matches[-1][0]] if matches[-1][1] > line.rfind(last) else last
    return int(r_first), int(r_last)


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
