import unittest
import re
from functools import cmp_to_key
from utils import read_input

cards = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")
cards2 = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")
lines = read_input("day7.txt")
values = [l.split(" ") for l in lines]
sample = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]
sample = [l.split(" ") for l in sample]


def sort_hands(a, b):
    ha = a[0]
    hb = b[0]
    ta = get_type(ha)
    tb = get_type(hb)

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
    parts = list(
        dict(sorted(parts.items(), key=lambda item: item[1], reverse=True)).values()
    )

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


def sort_hands2(a, b):
    ha = a[0]
    hb = b[0]
    ta = get_type2(ha)
    tb = get_type2(hb)

    if ta > tb:
        return -1
    elif ta == tb:
        for i in range(0, 5):
            if cards2.index(ha[i]) == cards2.index(hb[i]):
                continue
            elif cards2.index(ha[i]) < cards2.index(hb[i]):
                return -1
            else:
                return 1
    else:
        return 1


sort_hands_cmp_key2 = cmp_to_key(sort_hands2)


def get_type2(hand):
    chars = [x for x in hand]
    s = list(set(chars))
    parts = {}
    j_count = 0
    for ch in chars:
        if ch == "J":
            j_count += 1

        if ch in parts:
            parts[ch] = parts[ch] + 1
        else:
            parts[ch] = 1

    srted = sorted(parts.items(), key=lambda item: item[1], reverse=True)
    filtered = [x for x in srted if x[0] != "J"]
    dtc = dict(srted)

    if j_count == 5:
        return 7  # five of kind

    if j_count > 0:
        item = filtered[0]
        k = item[0]
        v = item[1]

        dtc[k] = j_count + v
        del dtc["J"]

    parts = list(dtc.values())

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
    return total


def get_total_winning2(lines):
    lines.sort(key=sort_hands_cmp_key2)
    lines.reverse()
    total = 0
    for idx in range(len(lines)):
        w = lines[idx]
        hand = w[0]
        type = get_type2(hand)
        amount = int(w[1])
        v = (idx + 1) * amount
        total += v
    return total


class Test(unittest.TestCase):
    def test_case(self):
        self.assertEqual(get_type("AAAAA"), 7)
        self.assertEqual(get_type("AA8AA"), 6)
        self.assertEqual(get_type("23332"), 5)
        self.assertEqual(get_type("TTT98"), 4)
        self.assertEqual(get_type("23432"), 3)
        self.assertEqual(get_type("A23A4"), 2)
        self.assertEqual(get_type("23456"), 1)

    def test_part1_get_total_winning_sample(self):
        self.assertEqual(get_total_winning(sample[:]), 6440)

    def test_part1_get_total_winning_solution(self):
        self.assertEqual(get_total_winning(values[:]), 250232501)

    def test_part2_get_total_winning_sample(self):
        self.assertEqual(get_total_winning2(sample[:]), 5905)

    def test_get_sort(self):
        lines = [["T3J3J", "75"], ["T3333", "937"]]
        self.assertEqual(get_total_winning2(lines), 1949)

    def test_part2_get_total_winning_solution(self):
        self.assertEqual(get_total_winning2(values[:]), 249138943)


if __name__ == "__main__":
    unittest.main()
