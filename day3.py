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


def get_symbols(ri, s, e, rows):
    row = rows[ri]
    rs = 0 if ri == 0 else ri - 1
    re = ri if ri == len(rows)-1 else ri + 1
    cs = 0 if s == 0 else s - 1
    ce = e if e == len(row) else e + 1

    # print("ri: ", ri, s, e)
    # print("rc: ", rs, re, cs, ce)

    symbols = []
    for r in range(rs, re+1):
        # print(" for: ", r, " row:", rows[r], " str:", rows[r][cs:ce])
        for s in rows[r][cs:ce]:
            if not s.isdigit() and s != '.':
                symbols.append(s)

    return symbols


def find_part_numbers(lines):
    parts = []

    for li in range(len(lines)):
        line = lines[li]
        # print(li, " => ", line)
        matches = re.finditer(f"\d+", line)
        for m in matches:
            # print('      %d-%d: %s' % (m.start(), m.end(), m.group(0)))
            s = m.start()
            e = m.end()
            n = int(m.group(0))

            symbols = get_symbols(li, s, e, lines)
            if (len(symbols) > 0):
                parts.append(n)

    return parts


class TestDay3(unittest.TestCase):
    def test_read_input(self):
        self.assertEqual(len(read_input("day3.txt")), 140)

    def test_find_partial_numbers(self):
        self.assertEqual(sum(find_part_numbers(sample_values)), 4362)

    def test_find_partial_numbers_part1(self):
        values = read_input("day3.txt")
        self.assertEqual(sum(find_part_numbers(values)), 0)


if __name__ == "__main__":
    unittest.main()
