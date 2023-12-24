def part_one(filename: str) -> str:
    hailstones = get_data(filename)
    result = 0

    for i, h1 in enumerate(hailstones):
        for j, h2 in enumerate(hailstones[:i]):
            x1, y1, z1, vx1, vy1, vz1 = h1
            x2, y2, z2, vx2, vy2, vz2 = h2

            a1, a2 = vy1, vy2
            b1, b2 = -vx1, -vx2
            c1, c2 = vy1 * x1 - vx1 * y1, vy2 * x2 - vx2 * y2

            if a1 * b2 - a2 * b1 == 0:
                continue

            xr = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
            yr = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)
            if 200000000000000 <= xr <= 400000000000000 and 200000000000000 <= yr <= 400000000000000:
                if (xr - x1) * vx1 >= 0 and (yr - y1) * vy1 >= 0 and (xr - x2) * vx2 >= 0 and (yr - y2) * vy2 >= 0:
                    result += 1
    return str(result)


def get_data(filename: str) -> list:
    with open(filename, "r") as file:
        data = file.read().splitlines()
    r = []
    for line in data:
        pos, vel = line.split(" @ ")
        x, y, z = pos.split(", ")
        vx, vy, vz = vel.split(", ")
        r.append((int(x), int(y), int(z), int(vx), int(vy), int(vz)))
    return r


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
