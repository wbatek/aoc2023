def part_one(filename: str) -> str:
    sum = 0
    with open(filename) as file:
        line = file.readline()
        while line:
            sum += parse_line(line[5:])[0]
            line = file.readline()
    return str(sum)


def part_two(filename: str) -> str:
    sum = 0
    with open(filename) as file:
        line = file.readline()
        while line:
            sum += parse_line(line[5:])[1] * parse_line(line[5:])[2] * parse_line(line[5:])[3]
            line = file.readline()
    return str(sum)


def parse_line(line: str) -> list:
    game_number = line.split(":")[0]
    green, blue, red = get_colors(line.split(":")[1])
    if red > 12 or green > 13 or blue > 14:
        return [0, int(green), int(blue), int(red)]
    return [int(game_number), int(green), int(blue), int(red)]


def get_colors(line: str) -> tuple:
    line = line.replace(',', '').replace('\n', '')
    (max_green, max_blue, max_red) = 0, 0, 0
    for subgame in line.split(";"):
        data = subgame.split(" ")
        for color in data:
            if color == "green":
                max_green = max(int(max_green), int(data[data.index(color) - 1]))
            elif color == "blue":
                max_blue = max(int(max_blue), int(data[data.index(color) - 1]))
            elif color == "red":
                max_red = max(int(max_red), int(data[data.index(color) - 1]))
    return int(max_green), int(max_blue), int(max_red)


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
