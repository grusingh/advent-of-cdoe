import re
import unittest


def read_input():
    file = open('day1.txt', 'r')
    lines = file.readlines()
    file.close()
    values = []
    for line in lines:
        values.append(line.strip())
    return values


def parse_numbers_from_string(val):
    num_string = ['one', 'two', 'three', 'four',
                  'five', 'six', 'seven', 'eight', 'nine']
    nums = []
    for i in range(len(val)+1):
        for j in range(len(val)+1):
            v = val[i:j]
            if len(v) == 1 and re.match(f"\d", v):
                nums.append(int(v))
                continue

            if v in num_string:
                nums.append(num_string.index(v)+1)

    if len(nums) == 1:
        return int(f"{nums[0]}{nums[0]}")
    elif len(nums) > 1:
        return int(f"{nums[0]}{nums[-1]}")
    else:
        return 0


def parse_numbers_from_strings(strings):
    result = []
    for val in strings:
        result.append(parse_numbers_from_string(val))
    return result


class TestParseNumbers(unittest.TestCase):
    def test_parse_numbers_from_strings(self):
        lines = [
            '1eightwo',
            'abc2x3oneight',
            '1abc2',
            'pqr3stu8vwx',
            'a1b2c3d4e5f',
            'treb7uchet',
            'l9',
            'two1nine',
            'eightwothree',
            'abcone2threexyz',
            'xtwone3four',
            '4nineeightseven2',
            'zoneight234',
            '7pqrstsixteen',
        ]
        result = parse_numbers_from_strings(lines)
        expected = [12, 28, 12, 38, 15, 77, 99, 29, 83, 13, 24, 42, 14, 76]
        self.assertEqual(result, expected)

    def test_solution(self):
        values = read_input()
        numbers = parse_numbers_from_strings(values)
        self.assertEqual(sum(numbers), 55260)


if __name__ == '__main__':
    unittest.main()
