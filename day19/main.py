import re
from collections import deque

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
    queue = deque([('in', {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000)}
                    )])
    result = 0

    while queue:
        i = 0
        current_rule, d = queue.pop()

        rule = rules[current_rule][i]
        while rule != 'A' and rule != 'R':
            if '<' not in rule and '>' not in rule:
                queue.append((rule, d))
                break
            sign = '>' if '>' in rule else '<'
            to_compare = int(rule[rule.index(sign) + 1:rule.index(':')])
            type_of_column = rule[0]
            if sign == '<':
                if d[type_of_column][0] < to_compare:
                    new_d = create_dict(d, type_of_column,
                                        (d[type_of_column][0], min(to_compare - 1, d[type_of_column][1])))
                    if rule[rule.index(':') + 1:] == 'A':
                        result += ((new_d['x'][1] - new_d['x'][0] + 1) *
                                   (new_d['m'][1] - new_d['m'][0] + 1) *
                                   (new_d['a'][1] - new_d['a'][0] + 1) *
                                   (new_d['s'][1] - new_d['s'][0] + 1))

                    elif rule[rule.index(':') + 1:] == 'R':
                        pass

                    else:
                        queue.append((rule[rule.index(':') + 1:], new_d))

                    if d[type_of_column][1] > to_compare:
                        d = create_dict(d, type_of_column, (to_compare, d[type_of_column][1]))
                        i += 1
                        rule = rules[current_rule][i]
                    else:
                        i = 0
                else:
                    i += 1
                    d = create_dict(d, type_of_column, (to_compare, d[type_of_column][1]))
                    rule = rules[current_rule][i]
            else:
                if d[type_of_column][1] > to_compare:
                    new_d = create_dict(d, type_of_column,
                                        (max(to_compare + 1, d[type_of_column][0]), d[type_of_column][1]))
                    if rule[rule.index(':') + 1:] == 'A':
                        result += ((new_d['x'][1] - new_d['x'][0] + 1) *
                                   (new_d['m'][1] - new_d['m'][0] + 1) *
                                   (new_d['a'][1] - new_d['a'][0] + 1) *
                                   (new_d['s'][1] - new_d['s'][0] + 1))
                    elif rule[rule.index(':') + 1:] == 'R':
                        pass
                    else:
                        queue.append((rule[rule.index(':') + 1:], new_d))

                    if d[type_of_column][0] < to_compare:
                        d = create_dict(d, type_of_column, (d[type_of_column][0], to_compare))
                        i += 1
                        rule = rules[current_rule][i]
                    else:
                        i = 0
                else:
                    i += 1
                    d = create_dict(d, type_of_column, (d[type_of_column][0], to_compare))
                    rule = rules[current_rule][i]

        if rule == 'A':
            result += ((d['x'][1] - d['x'][0] + 1) *
                       (d['m'][1] - d['m'][0] + 1) *
                       (d['a'][1] - d['a'][0] + 1) *
                       (d['s'][1] - d['s'][0] + 1))
    return str(result)


def create_dict(d, key, value):
    x = dict(d)
    x[key] = value
    return x


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

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
