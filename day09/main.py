def part_one(filename: str) -> str:
    series = get_data(filename)
    result = 0
    for single_series in series:
        result += predict_part_one(single_series)
    return str(result)


def part_two(filename: str) -> str:
    series = get_data(filename)
    result = 0
    for single_series in series:
        result += predict_part_two(single_series)
    return str(result)


def predict_part_one(series: list) -> int:
    result = series[-1]
    layers = generate_layers(series)
    for i in range(len(layers) - 1):
        result += layers[i][-1] - layers[i][-2]
    return result


def predict_part_two(series: list) -> int:
    result = 0
    layers = generate_layers(series)
    for i in range(len(layers) - 2, -1, -1):
        result = layers[i][0] - result
    return result


def generate_layers(series: list) -> list:
    length = len(series)

    layers = [series]
    all_zeros = False
    while not all_zeros:
        layer = []
        for i in range(length - len(layers)):
            layer.append(layers[-1][i + 1] - layers[-1][i])
        layers.append(layer)
        all_zeros = all([x == 0 for x in layer])
    return layers


def get_data(filename: str) -> list:
    with open(filename) as file:
        lines = [line for line in file.readlines()]
    series = []
    for i in range(len(lines)):
        series.append([int(x) for x in lines[i].split(" ")])
    return series


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
