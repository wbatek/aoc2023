START_IDX = [3, 30, 41, 76, 124, 161, 183]
# START_IDX = [3, 7, 12, 18, 22, 27, 31]
NUMBER_OF_MAPS = 7


def part_one(filename: str) -> str:
    with open(filename) as file:
        data = [line.strip() for line in file.readlines()]
    seeds = [int(x) for x in data[0].split(" ") if x.isdigit()]
    seed_to_location = {seed: seed for seed in seeds}
    for i in range(NUMBER_OF_MAPS):
        update_values(seeds, seed_to_location, data, START_IDX[i])
        print(seed_to_location)

    return str(min(seed_to_location.values()))


def part_two(filename: str) -> str:
    with open(filename) as file:
        data = [line.strip() for line in file.readlines()]
    seed_ranges = data[0].split(": ")[1].split(" ")
    seeds = set()
    for i in range(0, len(seed_ranges), 2):
        pair = seed_ranges[i:i + 2]
        for j in range(int(pair[1])):
            print(int(pair[0])+j)
            seeds.add(int(pair[0]) + j)
    seeds = list(seeds)

    seed_to_location = {seed: seed for seed in seeds}
    for i in range(NUMBER_OF_MAPS):
        update_values(seeds, seed_to_location, data, START_IDX[i])
        print(seed_to_location)

    return str(min(seed_to_location.values()))


def update_values(seeds, seed_to_location, data, first_line_idx):
    for seed in seeds:
        print(seed)
        for line in data[first_line_idx:]:
            if line == "":
                break
            val, key, r = [int(x) for x in line.split(" ")]
            map_value = seed_to_location[seed]
            if map_value in range(key, key + r):
                i_val = val + (map_value - key)
                seed_to_location[seed] = i_val
                break


if __name__ == "__main__":
    input_path = "input.txt"
    # with open("output1.txt", "w") as f:
    #     f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
