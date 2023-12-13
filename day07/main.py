AVAILABLE_CARDS = [-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


class Hand:
    # 'H', '1P', '2P', '3', 'FH', '4', '5'
    #  0,   1,    2,    3,   4,    5,   6

    def __init__(self, cards: list, cost: int, part2: bool = False):
        self.cards = self.convert_cards(cards, part2)
        self.poker_hand_val = self.get_poker_hand()
        self.cost = cost

    def get_poker_hand(self) -> int:
        card_to_count = {card: 0 for card in AVAILABLE_CARDS}
        for card in self.cards:
            card_to_count[card] += 1
        return self.determine_poker_hand_val(card_to_count)

    @staticmethod
    def convert_cards(cards: list, part2: bool) -> list:
        return [int(card) if card.isdigit() else Hand.convert_letter(card, part2) for card in cards]

    @staticmethod
    def convert_letter(card: str, part2: bool) -> int:
        if card == 'T':
            return 10
        elif card == 'J':
            if part2:
                return -1
            return 11
        elif card == 'Q':
            return 12
        elif card == 'K':
            return 13
        elif card == 'A':
            return 14
        else:
            raise ValueError("Unknown card: " + card)

    @staticmethod
    def determine_poker_hand_val(card_to_count: dict) -> int:
        joker_val = card_to_count[-1]
        card_to_count.pop(-1, None)
        if 5 - joker_val in card_to_count.values():
            return 6
        elif 4 - joker_val in card_to_count.values():
            return 5
        elif 3 - joker_val in card_to_count.values():
            associated_key = [key for key, value in card_to_count.items() if value == 3 - joker_val][0]
            card_to_count.pop(associated_key, None)
            if 2 in card_to_count.values():
                return 4
            else:
                return 3
        elif 2 - joker_val in card_to_count.values():
            if list(card_to_count.values()).count(2) == 2:
                return 2
            else:
                return 1
        else:
            return 0


def part_one(filename: str) -> str:
    result = 0
    lines = parse_input(filename)
    hands = [Hand(list(line.split(" ")[0]), line.split(" ")[1]) for line in lines]
    hands_sorted = sorted(hands, key=lambda x: (x.poker_hand_val, x.cards), reverse=True)
    for i in range(len(lines)):
        result += (i + 1) * int(hands_sorted[len(lines) - i - 1].cost)
    return str(result)


def parse_input(filename: str) -> list:
    with open(filename, "r") as file:
        x = file.readlines()
    return [y.strip() for y in x]


def part_two(filename: str) -> str:
    result = 0
    lines = parse_input(filename)
    hands = [Hand(list(line.split(" ")[0]), line.split(" ")[1], True) for line in lines]
    hands_sorted = sorted(hands, key=lambda x: (x.poker_hand_val, x.cards), reverse=True)
    for i in range(len(lines)):
        result += (i + 1) * int(hands_sorted[len(lines) - i - 1].cost)
    return str(result)


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

    with open("output2.txt", "w") as f:
        f.write(part_two(input_path))
