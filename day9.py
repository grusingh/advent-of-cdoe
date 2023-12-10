import unittest
import re
from utils import read_input

values = read_input("day9.txt")
sample = [
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45",
]


def get_data(lines):
    result = []
    for line in lines:
        result.append([int(x) for x in line.split(" ")])
    return result


def get_interations_to_zero(input):
    line = input
    lines = [input]

    while True:
        r = []
        all_zero = True
        for i in range(1, len(line)):
            v = line[i] - line[i - 1]
            r.append(v)

            if v != 0:
                all_zero = False

        # print("r:", r)
        lines.append(r)
        line = r

        if all_zero:
            break

    # print(lines)
    return lines


def get_next(line):
    lst = get_interations_to_zero(line)
    lst.reverse()

    # print("before: ", lst)

    v = 0
    for l in lst:
        # print("l", l)
        # print("s", len(set(l)))

        if len(set(l)) == 1:
            v = l[-1:][0]
            # print("v1", v)
            l.append(v)
        else:
            v = l[-1:][0] + v
            # print("v2", v)
            l.append(v)

        # print("new line", l)

    lst.reverse()
    # print("after:", lst)
    return lst[0][-1:][0]


def get_sum_part1(lines):
    data = get_data(lines)
    total = 0
    for d in data:
        n = get_next(d)
        # print("n", n)
        total += n
    return total


class Test(unittest.TestCase):
    def xtest_case(self):
        v = get_data(sample)
        self.assertEqual(
            v, [[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]]
        )

    def xtest_get_interations_to_zero(self):
        data = get_data(sample)
        v = get_interations_to_zero(data[0])
        self.assertEqual(v, [[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0, 0, 0, 0]])

    def test_get_sum_sample(self):
        total = get_sum_part1(sample)
        self.assertEqual(total, 114)

    def test_get_sum_part1(self):
        total = get_sum_part1(values)
        self.assertEqual(total, 1789635132)


if __name__ == "__main__":
    unittest.main()
