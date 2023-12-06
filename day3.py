from utils import read_input
import unittest
import re

sample_values = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..',
    '......*001'
]

sample_gears = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..',
]


def get_symbols(ri, s, e, rows):
    row = rows[ri]
    rs = 0 if ri == 0 else ri - 1
    re = ri if ri == len(rows)-1 else ri + 1
    cs = 0 if s == 0 else s - 1
    ce = e if e == len(row) else e + 1

    symbols = []
    for r in range(rs, re+1):
        for si in range(cs, ce):
            s = rows[r][si]
            if not s.isdigit() and s != '.':
                symbols.append([s, r, si])

    return symbols


def find_part_numbers(lines):
    parts = []

    for li in range(len(lines)):
        line = lines[li]
        matches = re.finditer(f"\d+", line)
        for m in matches:
            s = m.start()
            e = m.end()
            n = int(m.group(0))

            symbols = get_symbols(li, s, e, lines)
            if (len(symbols) > 0):
                parts.append(n)

    return parts


def find_gears(lines):
    parts = []

    for li in range(len(lines)):
        line = lines[li]
        matches = re.finditer(f"\d+", line)
        for m in matches:
            s = m.start()
            e = m.end()
            n = int(m.group(0))

            symbols = get_symbols(li, s, e, lines)
            if (len(symbols) > 0):
                parts.append([n, symbols])

    gears = []
    for e in parts:
        n = e[0]
        sa = e[1]
        for s in sa:
            if s[0] == '*':
                gear = None
                for x in gears:
                    if x[0] == s[1] and x[1] == s[2]:
                        gear = x
                        break

                if gear:
                    gear[2].append(n)
                else:
                    gears.append([s[1], s[2], [n]])

    doubles = []
    total = 0
    for g in gears:
        if len(g[2]) == 2:
            doubles.append(g)
            x = g[2][0]
            y = g[2][1]
            total += (x*y)

    return total


class TestDay3(unittest.TestCase):
    def test_read_input(self):
        self.assertEqual(len(read_input("day3.txt")), 140)

    def test_find_partial_numbers(self):
        self.assertEqual(sum(find_part_numbers(sample_values)), 4362)

    def test_find_partial_numbers_part1(self):
        values = read_input("day3.txt")
        self.assertEqual(sum(find_part_numbers(values)), 536202)

    def test_find_gears(self):
        self.assertEqual(find_gears(sample_gears), 467835)

    def test_find_gears_part2(self):
        values = read_input("day3.txt")
        self.assertEqual(find_gears(values), 78272573)


if __name__ == "__main__":
    unittest.main()
