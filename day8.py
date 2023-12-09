import unittest
import re
from utils import read_input

sample1 = [
    "RL",
    "",
    "AAA = (BBB, CCC)",
    "BBB = (DDD, EEE)",
    "CCC = (ZZZ, GGG)",
    "DDD = (DDD, DDD)",
    "EEE = (EEE, EEE)",
    "GGG = (GGG, GGG)",
    "ZZZ = (ZZZ, ZZZ)",
]

sample2 = [
    "LLR",
    "",
    "AAA = (BBB, BBB)",
    "BBB = (AAA, ZZZ)",
    "ZZZ = (ZZZ, ZZZ)",
]


def get_data(lines):
    steps = lines[0].strip()

    nodes = {}
    for n in [x.split(" = ") for x in lines[2:]]:
        k = n[0]
        v = re.findall("[A-Z]+", n[1])
        nodes[k] = v
    return (steps, nodes)


def get_hops(lines):
    (steps, nodes) = get_data(lines=lines)
    hops = 0
    key = "AAA"
    step_idx = 0

    while True:
        idx = 0 if steps[step_idx] == "L" else 1
        key = nodes[key][idx]
        hops += 1
        step_idx += 1

        if key == "ZZZ":
            break

        if step_idx == len(steps):
            step_idx = 0

    return hops


class Test(unittest.TestCase):
    def test_case(self):
        (k, v) = get_data(sample1)
        self.assertEqual(k, "RL")
        self.assertEqual(
            v,
            {
                "AAA": ["BBB", "CCC"],
                "BBB": ["DDD", "EEE"],
                "CCC": ["ZZZ", "GGG"],
                "DDD": ["DDD", "DDD"],
                "EEE": ["EEE", "EEE"],
                "GGG": ["GGG", "GGG"],
                "ZZZ": ["ZZZ", "ZZZ"],
            },
        )

    def test_get_hops_part1_sample1(self):
        h = get_hops(sample1)
        self.assertEqual(h, 2)

    def test_get_hops_part1_sample2(self):
        h = get_hops(sample2)
        self.assertEqual(h, 6)

    def test_get_hops_part1_solution(self):
        lines = read_input("day8.txt")
        h = get_hops(lines)
        self.assertEqual(h, 16409)


if __name__ == "__main__":
    unittest.main()
