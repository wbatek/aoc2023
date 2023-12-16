class Beam:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction


def part_one(filename: str) -> str:
    data = get_data(filename)
    return str(calculate_coverage(data, Beam(0, 0, 'E')))


def part_two(filename: str) -> str:
    data = get_data(filename)
    result = 0
    for i in range(len(data[0])):
        result = max(result, calculate_coverage(data, Beam(i, 0, 'S')),
                     calculate_coverage(data, Beam(i, len(data) - 1, 'N')))
    for i in range(len(data)):
        result = max(result, calculate_coverage(data, Beam(0, i, 'E')),
                     calculate_coverage(data, Beam(len(data[0]) - 1, i, 'W')))
    return str(result)


def calculate_coverage(data: list, start_beam: Beam) -> int:
    count = 0
    already_seen = set()
    beams = [start_beam]
    coverage = [['.' for _ in range(len(data[0]))] for _ in range(len(data))]
    while beams:
        beam_size = len(beams)
        for i in range(beam_size):
            current_beam = beams.pop(0)
            if ((current_beam.x, current_beam.y,
                current_beam.direction) in already_seen or current_beam.x < 0 or current_beam.x >= len(data[0])
                    or current_beam.y < 0 or current_beam.y >= len(data)):
                continue
            already_seen.add((current_beam.x, current_beam.y, current_beam.direction))
            if coverage[current_beam.y][current_beam.x] != '#':
                coverage[current_beam.y][current_beam.x] = '#'
                count += 1
            move(current_beam, data, beams)
    return count


def move(beam: Beam, data: list, beams: list):
    if beam.direction == 'E':
        if data[beam.y][beam.x] in '.-':
            beams.append(Beam(beam.x + 1, beam.y, 'E'))
        elif data[beam.y][beam.x] == '/':
            beams.append(Beam(beam.x, beam.y - 1, 'N'))
        elif data[beam.y][beam.x] == '\\':
            beams.append(Beam(beam.x, beam.y + 1, 'S'))
        elif data[beam.y][beam.x] == '|':
            beams.append(Beam(beam.x, beam.y - 1, 'N'))
            beams.append(Beam(beam.x, beam.y + 1, 'S'))

    elif beam.direction == 'W':
        if data[beam.y][beam.x] in '.-':
            beams.append(Beam(beam.x - 1, beam.y, 'W'))
        elif data[beam.y][beam.x] == '/':
            beams.append(Beam(beam.x, beam.y + 1, 'S'))
        elif data[beam.y][beam.x] == '\\':
            beams.append(Beam(beam.x, beam.y - 1, 'N'))
        elif data[beam.y][beam.x] == '|':
            beams.append(Beam(beam.x, beam.y - 1, 'N'))
            beams.append(Beam(beam.x, beam.y + 1, 'S'))

    elif beam.direction == 'N':
        if data[beam.y][beam.x] == '.' or data[beam.y][beam.x] == '|':
            beams.append(Beam(beam.x, beam.y - 1, 'N'))
        elif data[beam.y][beam.x] == '/':
            beams.append(Beam(beam.x + 1, beam.y, 'E'))
        elif data[beam.y][beam.x] == '\\':
            beams.append(Beam(beam.x - 1, beam.y, 'W'))
        elif data[beam.y][beam.x] == '-':
            beams.append(Beam(beam.x + 1, beam.y, 'E'))
            beams.append(Beam(beam.x - 1, beam.y, 'W'))

    elif beam.direction == 'S':
        if data[beam.y][beam.x] == '.' or data[beam.y][beam.x] == '|':
            beams.append(Beam(beam.x, beam.y + 1, 'S'))
        elif data[beam.y][beam.x] == '/':
            beams.append(Beam(beam.x - 1, beam.y, 'W'))
        elif data[beam.y][beam.x] == '\\':
            beams.append(Beam(beam.x + 1, beam.y, 'E'))
        elif data[beam.y][beam.x] == '-':
            beams.append(Beam(beam.x + 1, beam.y, 'E'))
            beams.append(Beam(beam.x - 1, beam.y, 'W'))


def get_data(filename: str):
    with open(filename) as file:
        data = file.readlines()
    return [list(x.strip()) for x in data]


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
