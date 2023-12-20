import math
from collections import defaultdict


def part_one(filename: str) -> str:
    N = 1000
    start, flip_flops, conjunctions, rules = get_data(filename)
    print(rules)
    values_count = {0: 0, 1: 0}
    for i in range(N):
        queue = [s for s in start]
        values_count[0] += 1
        while queue:
            current, signal_value = queue.pop(0)
            values_count[signal_value] += 1

            if current not in flip_flops.keys() and current not in conjunctions.keys():
                continue

            if current in conjunctions:
                next_signal = 0 if all(val == 1 for val in conjunctions[current].values()) else 1
                for rule in rules[current]:
                    if rule in conjunctions:
                        conjunctions[rule][current] = next_signal
                    queue.append((rule, next_signal))

            else:
                if signal_value == 0:
                    next_signal = 1 if flip_flops[current] == 0 else 0
                    flip_flops[current] = next_signal
                    for rule in rules[current]:
                        if rule in conjunctions:
                            conjunctions[rule][current] = next_signal
                        queue.append((rule, next_signal))

    return str(values_count[0] * values_count[1])


def part_two(filename: str) -> str:
    start, flip_flops, conjunctions, rules = get_data(filename)
    presses = 0
    last = ""
    for key, val in rules.items():
        if 'rx' in val:
            last = key
            break

    next_to_last = []
    for key, val in rules.items():
        if last in val:
            next_to_last.append(key)

    seen = {key: 0 for key in next_to_last}
    cycle_lengths = {}

    while True:
        queue = [s for s in start]
        presses += 1
        while queue:
            current, signal_value = queue.pop(0)

            if current in conjunctions:
                next_signal = 0 if all(val == 1 for val in conjunctions[current].values()) else 1
                for rule in rules[current]:
                    if rule == last and next_signal == 1:
                        seen[current] += 1
                        if current not in cycle_lengths:
                            cycle_lengths[current] = presses

                        if all(seen.values()):
                            x = 1
                            for cycle_length in cycle_lengths.values():
                                x = x * cycle_length // math.gcd(x, cycle_length)
                            return str(x)

                    if rule in conjunctions:
                        conjunctions[rule][current] = next_signal
                    queue.append((rule, next_signal))

            else:
                if signal_value == 0:
                    next_signal = 1 if flip_flops[current] == 0 else 0
                    flip_flops[current] = next_signal
                    for rule in rules[current]:
                        if rule in conjunctions:
                            conjunctions[rule][current] = next_signal
                        queue.append((rule, next_signal))


def get_data(filename: str) -> tuple:
    with open(filename, "r") as file:
        data = file.read().split('\n')
    flip_flops = {}
    conjunction = defaultdict(dict)
    rules = {}
    start = []
    for val in data:
        name = val.split('->')[0][:-1]
        rules[name[1:]] = []
        for dest in val.split('->')[1][1:].split(', '):
            rules[name[1:]].append(dest)
        if name[0] == '%':
            # handle flip flops
            flip_flops[name[1:]] = 0
        elif name[0] == '&':
            # handle conjunctions
            for line in data:
                key, elems = line.split('->')[0][1:-1], line.split('->')[1][1:]
                for elem in elems.split(', '):
                    if elem == name[1:]:
                        conjunction[name[1:]][key] = 0
        else:
            # handle broadcasting
            destinations = val.split('->')[1][1:]
            for dest in destinations.split(', '):
                start.append((dest, 0))
    return start, flip_flops, conjunction, rules


if __name__ == "__main__":
    input_path = "input.txt"
    # with open("output1.txt", "w") as f:
    #     f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
