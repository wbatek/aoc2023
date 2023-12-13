START_IDX = [3, 30, 41, 76, 124, 161, 183]
NUMBER_OF_MAPS = 7


def part_one(filename: str) -> str:
    with open(filename) as file:
        data = [line.strip() for line in file.readlines()]
    seeds = [int(x) for x in data[0].split(" ") if x.isdigit()]
    seed_to_location = {seed: seed for seed in seeds}
    for i in range(NUMBER_OF_MAPS):
        update_values(seeds, seed_to_location, data, START_IDX[i])

    return str(min(seed_to_location.values()))


def part_two(filename: str) -> str:
    with open(filename) as file:
        data = [line.strip() for line in file.readlines()]
    seeds = data[0].split(": ")[1].split(" ")
    return str(find_first_location(seeds, data))


def update_values(seeds, seed_to_location, data, first_line_idx):
    for seed in seeds:
        for line in data[first_line_idx:]:
            if line == "":
                break
            val, key, r = [int(x) for x in line.split(" ")]
            map_value = seed_to_location[seed]
            if map_value in range(key, key + r):
                i_val = val + (map_value - key)
                seed_to_location[seed] = i_val
                break


def find_first_location(seeds, data):
    location = 0
    while True:
        if get_seed_for_location(seeds, location, data):
            return location
        location += 1


def check_location_in_range(seeds, current_seed) -> bool:
    for i in range(0, len(seeds), 2):
        if int(current_seed) in range(int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])):
            return True
    return False


def get_seed_for_location(seeds, location, data) -> int:
    l = location
    for i in range(NUMBER_OF_MAPS - 1, -1, -1):
        for line in data[START_IDX[i]:]:
            if line == "":
                break
            val, key, r = [int(x) for x in line.split(" ")]
            dif = location - val
            if 0 <= dif < r:
                l = key + dif
                break
        location = l
    if check_location_in_range(seeds, l):
        return True
    return False


if __name__ == "__main__":
    input_path = "input.txt"
    # with open("output1.txt", "w") as f:
    #     f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
