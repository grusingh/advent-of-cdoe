import unittest
import re

sample = [
    'Time:      7  15   30',
    'Distance:  9  40  200',
]

values = [
    'Time:        54     94     65     92',
    'Distance:   302   1476   1029   1404'
]


def part1(lines):
    times = [int(x) for x in re.findall("\d+", lines[0])]
    dists = [int(x) for x in re.findall("\d+", lines[1])]

    ranges = []
    product = 1

    r = len(times)
    for idx in range(r):
        t = times[idx]
        d = dists[idx]

        s = None
        e = None
        for i in range(1, t + 1):
            p = (i)
            covered = p * (t - i)

            if covered > d and s is None:
                s = i

            if covered <= d and s is not None and e is None:
                e = i - 1

            print(" p:", p, " c:", covered, "s: ", s, "e: ", e)

        rng = e - s + 1
        print("range: t: ", t, "d: ", d, " r: ", rng)
        ranges.append(rng)
        product *= rng

    print("product", product)
    return product


class TestDay6(unittest.TestCase):
    def xtest_part1_sample(self):
        p = part1(sample)
        self.assertEqual(p, 288)

    def test_part1_solution(self):
        p = part1(values)
        self.assertEqual(p, 288)


if __name__ == "__main__":
    unittest.main()
