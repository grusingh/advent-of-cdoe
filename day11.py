import unittest
import re
from utils import read_input, write_matrix_to_file

# values = read_input("day.txt")
sample = [
    "...#......",
    ".......#..",
    "#.........",
    "..........",
    "......#...",
    ".#........",
    ".........#",
    "..........",
    ".......#..",
    "#...#.....",
]

expanded_sample = [
    "....#........",
    ".........#...",
    "#............",
    ".............",
    ".............",
    "........#....",
    ".#...........",
    "............#",
    ".............",
    ".............",
    ".........#...",
    "#....#.......",
]
expanded_num_matrix = [
    "....1........",
    ".........2...",
    "3............",
    ".............",
    ".............",
    "........4....",
    ".5...........",
    "............6",
    ".............",
    ".............",
    ".........7...",
    "8....9.......",
]


def get_matrix(lines, filler_times=1):
    rows = []
    for r in lines:
        chars = [c for c in r]
        rows.append(chars)

    empty_cols_idx = []
    for ci in range(len(rows[0])):
        col = []
        for ri in range(len(rows)):
            col.append(rows[ri][ci])
        if len(set(col)) == 1 and col[0] == ".":
            # print("found empty column", ci)
            empty_cols_idx.append(ci)

    # print("empty cols: ", empty_cols_idx)
    rows2 = []
    for ri in range(len(rows)):
        col = []
        # print("before", rows[ri])
        for idx in range(len(rows[ri])):
            if len([x for x in empty_cols_idx if x == idx]) == 1:
                # print("found filler", idx, "row ", ri)
                for t in range(filler_times):
                    col.append(".")
            else:
                col.append(rows[ri][idx])
        # print("col len", len(col), col)
        rows2.append(col)

    new_rows = []
    for ri in range(len(rows2)):
        r = rows2[ri]
        new_rows.append(r)
        s = set(r)
        if len(s) == 1 and "." in s:
            # print("found empty row", ri)
            for f in range(filler_times - 1):
                new_rows.append(r)

    return new_rows


def replace_galaxies_with_numbers(matrix):
    count = 1
    for ri in range(len(matrix)):
        row = matrix[ri]
        for ci in range(len(row)):
            if matrix[ri][ci] == "#":
                matrix[ri][ci] = f"{count}"
                count += 1
    return matrix


def find_pairs(matrix):
    gal = []
    for r in matrix:
        for c in r:
            if c != ".":
                gal.append(c)
    pairs = []
    for c1 in gal:
        for c2 in gal:
            add = True
            for p in pairs:
                if (p[0] == c1 or p[0] == c2) and (p[1] == c1 or p[1] == c2):
                    add = False

            if c1 != c2 and add:
                pairs.append([c1, c2])
    return pairs


def get_index(matrix, v):
    for ri in range(len(matrix)):
        r = matrix[ri]
        for ci in range(len(r)):
            c = r[ci]
            if c == v:
                return (ri, ci)


def get_path_length(matrix, a, b):
    idxa = get_index(matrix, a)
    idxb = get_index(matrix, b)
    return abs(idxa[0] - idxb[0]) + abs(idxa[1] - idxb[1])


def compute_sum(matrix):
    pairs = find_pairs(matrix)
    # print("pairs", len(pairs), pairs)
    total = 0
    for p in pairs:
        total += get_path_length(matrix, p[0], p[1])
    return total


class Test(unittest.TestCase):
    def test_get_matrix(self):
        matrix = get_matrix(sample, 2)
        expected = ["@".join(["".join(r) for r in expanded_sample])]
        result = ["@".join(["".join(r) for r in matrix])]
        self.assertEqual(result, expected)

    def test_replace_galaxies_with_numbers(self):
        matrix = get_matrix(sample, 2)
        num_matrix = replace_galaxies_with_numbers(matrix)
        expected = ["@".join(["".join(r) for r in expanded_num_matrix])]
        result = ["@".join(["".join(r) for r in num_matrix])]

        self.assertEqual(result, expected)

    def test_pairs(self):
        matrix = get_matrix(sample, 2)
        pairs = find_pairs(replace_galaxies_with_numbers(matrix))
        self.assertEqual(len(pairs), 36)

    def test_path_length(self):
        matrix = get_matrix(sample, 2)
        num_matrix = replace_galaxies_with_numbers(matrix)
        self.assertEqual(get_path_length(num_matrix, "9", "5"), 9)
        self.assertEqual(get_path_length(num_matrix, "1", "7"), 15)
        self.assertEqual(get_path_length(num_matrix, "3", "6"), 17)
        self.assertEqual(get_path_length(num_matrix, "8", "9"), 5)

    def test_sample_sum(self):
        matrix = get_matrix(sample, 2)
        num_matrix = replace_galaxies_with_numbers(matrix)
        total = compute_sum(num_matrix)
        self.assertEqual(total, 374)

    def test_sample_sum_filler_10(self):
        matrix = get_matrix(sample, 10)
        num_matrix = replace_galaxies_with_numbers(matrix)
        total = compute_sum(num_matrix)
        self.assertEqual(total, 1030)

    def test_sample_sum_filler_100(self):
        matrix = get_matrix(sample, 100)
        num_matrix = replace_galaxies_with_numbers(matrix)
        total = compute_sum(num_matrix)
        self.assertEqual(total, 8410)

    def xtest_part1_sum(self):
        matrix = get_matrix(read_input("day11.txt"))
        num_matrix = replace_galaxies_with_numbers(matrix)
        total = compute_sum(num_matrix)
        self.assertEqual(total, 374)

    def test_part2_sum(self):
        matrix = get_matrix(read_input("day11.txt"), 1000000)
        num_matrix = replace_galaxies_with_numbers(matrix)
        total = compute_sum(num_matrix)
        self.assertEqual(total, 374)


if __name__ == "__main__":
    unittest.main()
