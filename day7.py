import unittest
import re
from functools import cmp_to_key
from utils import read_input

cards = 'A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2'.split(', ')
lines = read_input("day7.txt")
values = [l.split(' ') for l in lines]
sample = [
    '32T3K 765',
    'T55J5 684',
    'KK677 28',
    'KTJJT 220',
    'QQQJA 483',
]
sample = [l.split(' ') for l in sample]


def sort_hands(a, b):
    ha = a[0]
    hb = b[0]
    ta = get_type(ha)
    tb = get_type(hb)

    # print("sort ", a, ta, b, tb)

    if ta > tb:
        return -1
    elif ta == tb:
        for i in range(0, 5):
            if cards.index(ha[i]) == cards.index(hb[i]):
                continue
            elif cards.index(ha[i]) < cards.index(hb[i]):
                return -1
            else:
                return 1
    else:
        return 1


sort_hands_cmp_key = cmp_to_key(sort_hands)


def get_type(hand):
    chars = [x for x in hand]
    s = list(set(chars))
    l = len(s)
    parts = {}
    for ch in chars:
        if ch in parts:
            parts[ch] = parts[ch] + 1
        else:
            parts[ch] = 1
    parts = list(dict(
        sorted(parts.items(), key=lambda item: item[1], reverse=True)).values())

    # print("hand: ", hand, " parts: ", parts)

    if parts[0] == 5:
        return 7  # five of kind
    if parts[0] == 4:
        return 6  # four of kind
    if parts[0] == 3 and parts[1] == 2:
        return 5  # full house
    if parts[0] == 3:
        return 4  # three of kind
    if parts[0] == 2 and parts[1] == 2:
        return 3  # two pair
    if parts[0] == 2:
        return 2  # one pair
    return 1


def get_total_winning(lines):
    lines.sort(key=sort_hands_cmp_key)
    lines.reverse()
    total = 0
    for idx in range(len(lines)):
        w = lines[idx]
        amount = int(w[1])
        total += (idx + 1) * amount
        # print("win: ", w, " idx:", idx, " amt: ", amount)
    return total


class Test(unittest.TestCase):
    def xtest_case(self):
        self.assertEqual(get_type('AAAAA'), 7)
        self.assertEqual(get_type('AA8AA'), 6)
        self.assertEqual(get_type('23332'), 5)
        self.assertEqual(get_type('TTT98'), 4)
        self.assertEqual(get_type('23432'), 3)
        self.assertEqual(get_type('A23A4'), 2)
        self.assertEqual(get_type('23456'), 1)

    def xtest_part1_get_total_winning_sample(self):
        self.assertEqual(get_total_winning(sample[:]), 6440)

    def test_part1_get_total_winning_solution(self):
        self.assertEqual(get_total_winning(values[:]), 250232501)


if __name__ == "__main__":
    unittest.main()
