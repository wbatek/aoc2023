cached_values = {}


def part_one(filename: str) -> str:
    lines, counts = get_data(filename)
    result = 0
    for i, line in enumerate(lines):
        result += count(list(line) + ['.'], [int(x) for x in counts[i]])

    return str(result)


def part_two(filename: str) -> str:
    lines, counts = get_data(filename)
    new_lines = []
    for line in lines:
        new_lines.append('?'.join([line] * 5))
    new_counts = []
    for i, c in enumerate(counts):
        new_counts.append(c * 5)
        new_counts[i] = [int(x) for x in new_counts[i]]
    result = 0
    for i, line in enumerate(new_lines):
        result += count(list(line) + ['.'], [int(x) for x in new_counts[i]])

    return str(result)

def count(inputs, numbers):
    if not numbers and all([i in '?.' for i in inputs]):
        return 1
    if (not inputs and numbers) or (inputs and not numbers):
        return 0

    current = (tuple(inputs),tuple(numbers))
    if current in cached_values.keys():
        return cached_values[current]

    result = 0
    if inputs[0] in '.?':
        result += count(inputs[1:], numbers)
    if inputs[0] in '#?':
        if all([i in '#?' for i in inputs[:numbers[0]]]):
            try:
                if inputs[numbers[0]] == '#':
                    return result
                else:
                    result += count(inputs[numbers[0] + 1:], numbers[1:])
            except IndexError: pass
    cached_values[current] = result
    return result


def get_data(filename: str) -> tuple:
    with open(filename) as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    lines = [line.split(' ') for line in data]
    counts = [line[1].split(',') for line in lines]
    lines = [line[0] for line in lines]
    return lines, counts


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
