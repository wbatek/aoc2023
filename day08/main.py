def part_one(filename: str) -> str:
    directions, mapping = get_data(filename)

    current = 'AAA'
    counter = 0
    while True:
        for direction in directions:
            current = mapping[current][int(direction)]
            counter += 1
            if current == 'ZZZ':
                return str(counter)


def part_two(filename: str) -> str:
    directions, mapping = get_data(filename)
    current = [start for start in mapping.keys() if start.endswith('A')]
    end = [end for end in mapping.keys() if end.endswith('Z')]
    steps = []
    for c in current:
        current_steps = 0
        temp = c
        while True:
            for direction in directions:
                temp = mapping[temp][int(direction)]
                current_steps += 1
                if temp in end:
                    steps.append(current_steps)
                    break
            if len(steps) == current.index(c) + 1:
                break

    result = lcm(steps)
    return str(result)


def get_data(filename: str) -> tuple:
    with open(filename, "r") as file:
        lines = file.readlines()
    directions = lines[0].replace('L', '0').replace('R', '1').strip()
    mapping = {}
    for line in lines[2:]:
        line = line.split(" ")
        mapping[line[0]] = (''.join(char for char in line[-2] if char.isalpha() or char.isdigit()),
                            ''.join(char for char in line[-1] if char.isalpha() or char.isdigit()))
    return directions, mapping


def lcm(found: list):
    res = found[0]
    for i in found:
        res = (res * i) // gcd(res, i)
    return res


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
