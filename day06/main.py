def part_one(filename: str) -> str:
    times, distances = get_times_distances(filename)
    result = 1
    for i in range(len(times)):
        result *= get_race(i, times, distances)
    return str(result)


def part_two(filename: str) -> str:
    times, distances = get_times_distances(filename)
    time = [int(''.join([str(time) for time in times]))]
    distance = [int(''.join([str(distance) for distance in distances]))]
    return str(get_race(0, time, distance))


def get_race(idx: int, times: list, distances: list) -> int:
    time = times[idx]
    distance = distances[idx]
    result = 0
    for i in range(time):
        move = (time - i) * i
        if move > distance:
            result += 1
    return result


def get_times_distances(filename: str) -> tuple:
    with open(filename) as file:
        data = [line.strip() for line in file.readlines()]
    times = data[0].split(":")[1].strip().split(" ")
    times = [int(time) for time in times if time != ""]
    distances = data[1].split(":")[1].strip().split(" ")
    distances = [int(distance) for distance in distances if distance != ""]
    return times, distances


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
