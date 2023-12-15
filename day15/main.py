def part_one(filename: str) -> str:
    data = get_data(filename)
    return str(sum([calc_hash(x) for x in data]))


def part_two(filename: str) -> str:
    data = get_data(filename)
    boxes = {i: [] for i in range(256)}
    for line in data:
        label = line[:max(line.find('-'), line.find('='))]
        operation = line[min(line.find('-'), line.find('='))]
        box_num = calc_hash(label)
        if operation == '-':
            if label in [x[0] for x in boxes[box_num]]:
                for i, x in enumerate(boxes[box_num]):
                    if x[0] == label:
                        boxes[box_num].remove(x)
                        break
        else:
            value = line[line.find('=') + 1:]
            if label in [x[0] for x in boxes[box_num]]:
                for i, x in enumerate(boxes[box_num]):
                    if x[0] == label:
                        boxes[box_num][i] = (label, value)
                        break
            else:
                boxes[box_num].append((label, value))
    return str(calculate_power(boxes))


def calculate_power(boxes: dict) -> int:
    result = 0
    for key, content in boxes.items():
        if len(content) == 0:
            continue
        current = 0
        for i, x in enumerate(content):
            current += (key + 1) * (i + 1) * int(x[1])
        result += current
    return result


def calc_hash(x: str) -> int:
    result = 0
    for char in x:
        result = ((result + ord(char)) * 17) % 256
    return result


def get_data(filename: str):
    with open(filename) as file:
        return file.readline().strip().split(',')


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
