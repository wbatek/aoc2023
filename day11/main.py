def part_one(filename: str, expand=2) -> str:
    result = 0
    grid, hash_indices, rows_dict, columns_dict = get_data(filename, expand)

    for i in range(len(hash_indices)):
        for j in range(i + 1, len(hash_indices)):
            first_idx = hash_indices[i]
            second_idx = hash_indices[j]
            count = 0
            for k in range(min(first_idx[0], second_idx[0]), max(first_idx[0], second_idx[0])):
                count += rows_dict[k]

            for k in range(min(first_idx[1], second_idx[1]), max(first_idx[1], second_idx[1])):
                count += columns_dict[k]

            result += count
    return str(result)


def part_two(filename: str) -> str:
    return part_one(filename, 1000000)


def get_data(filename: str, expand: int) -> tuple:
    with open(filename, "r") as file:
        grid = file.readlines()
    grid = [line.strip() for line in grid]
    hash_indices = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                hash_indices.append((i, j))

    empty_rows = []
    for i in range(len(grid)):
        if grid[i] == "." * len(grid[i]):
            empty_rows.append(i)
    rows_dict = {x: expand if x in empty_rows else 1 for x in range(len(grid))}
    empty_columns = []
    for i in range(len(grid[0])):
        if all(grid[j][i] == "." for j in range(len(grid))):
            empty_columns.append(i)
    columns_dict = {x: expand if x in empty_columns else 1 for x in range(len(grid[0]))}
    return grid, hash_indices, rows_dict, columns_dict


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
