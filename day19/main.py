import re

COLUMNS = {
    'x': 0,
    'm': 1,
    'a': 2,
    's': 3
}


def part_one(filename: str) -> str:
    rules, parts = get_data(filename)
    return str(calculate(rules, parts))


def calculate(rules, parts):
    result = 0
    for part in parts:
        i = 0
        next_step = 'in'
        while next_step != 'A' and next_step != 'R':
            rule = rules[next_step][i]
            if '<' not in rule and '>' not in rule:
                next_step = rule
                i = 0
                continue
            sign = '>' if '>' in rule else '<'
            comparable = int(part[COLUMNS[rule[0]]])
            to_compare = int(rule[rule.index(sign) + 1:rule.index(':')])

            if sign == '<':
                if comparable < to_compare:
                    next_step = rule[rule.index(':') + 1:]
                    i = 0
                else:
                    i += 1
            else:
                if comparable > to_compare:
                    next_step = rule[rule.index(':') + 1:]
                    i = 0
                else:
                    i += 1

        if next_step == 'A':
            result += sum([int(p) for p in part])
    return str(result)

def part_two(filename: str) -> str:
    rules, _ = get_data(filename)
    ranges = {key: (1, 4000) for key in COLUMNS.keys()}

def count(ranges, next_step='in'):
    if next_step == 'R':
        return 0
    if next_step == 'A':
        product = 1
        for left, right in ranges.values():
            product *= right - left + 1
        return product


def get_data(filename: str) -> tuple:
    with open(filename, "r") as file:
        data = file.read().splitlines()
    rules = {}
    for line in data:
        if line == "":
            break
        rule_name, rule = line.split('{')
        rule = rule.replace('}', '')
        rules[rule_name] = rule.split(",")
    x = data.index("")
    parts = []
    for line in data[x + 1:]:
        parts.append([int(match.group(2)) for match in re.finditer(r'(\w+)=(\d+)', line)])
    return rules, parts


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    # with open("output2.txt", "w") as f:
    #     f.write(part_two(input_path))
