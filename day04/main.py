COLON_IDX = 9


def part_one(filename: str) -> str:
    result = 0
    lines = open_file_and_extract_data(filename)
    for i in range(len(lines)):
        winning_numbers = {int(num) for num in lines[i][0].split()}
        counter = get_number_of_matches(lines[i][1].split(), winning_numbers)
        result += 2 ** (counter - 1) if counter >= 1 else 0
    return str(result)


def part_two(filename: str) -> str:
    lines = open_file_and_extract_data(filename)
    counts = {i + 1: 1 for i in range(len(lines))}
    for i in range(len(lines)):
        winning_numbers = {int(num) for num in lines[i][0].split()}
        counter = get_number_of_matches(lines[i][1].split(), winning_numbers)
        for j in range(counter):
            counts[i + 1 + j + 1] += counts[i + 1]
    return str(sum(counts.values()))


def get_number_of_matches(numbers: list, winning_numbers: set) -> int:
    counter = 0
    for num in numbers:
        if int(num) in winning_numbers:
            counter += 1
    return counter


def open_file_and_extract_data(filename: str) -> list:
    with open(filename, "r") as file:
        lines = file.readlines()
    lines = [line[COLON_IDX + 1:] for line in lines]
    lines = [line.strip() for line in lines]
    lines = [line.split("|") for line in lines]
    return lines


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
