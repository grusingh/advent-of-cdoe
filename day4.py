import unittest
from utils import read_input

cards = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
]


def calculate_points(cards):
    total_points = 0
    for card in cards:
        parts = card.split("|")
        one_parts = parts[0].split(":")
        card_number = one_parts[0]
        winners = list((int(w) for w in one_parts[1].split(" ") if len(w) > 0))
        candidates = list((int(c) for c in parts[1].split(" ") if len(c) > 0))
        wins = list(set(winners).intersection(candidates))

        point = 0
        for i in range(len(wins)):
            if i == 0:
                point = 1
            else:
                point = point + point
        total_points += point

        print(card_number, "winners: ", winners,
              " candidares: ", candidates, " wins: ", wins, " point: ", point)

    return total_points


class TestDay4(unittest.TestCase):
    def test_sample_points(self):
        s = calculate_points(cards)
        self.assertEqual(s, 13)

    def test_points_part1(self):
        cards = read_input("day4.txt")
        p = calculate_points(cards)
        self.assertEqual(p, 21138)


if __name__ == "__main__":
    unittest.main()
