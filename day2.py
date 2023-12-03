import re
import unittest


def read_input():
    file = open('day2.txt', 'r')
    lines = file.readlines()
    file.close()
    values = []
    for line in lines:
        values.append(line.strip())
    return values


def parse_game_from_string(val):
    split1 = val.split(':')
    id = int(split1[0].replace("Game ", ""))
    game_strings = split1[1].split(";")
    rolls = []
    for g in game_strings:
        colors = g.split(",")
        red = 0
        green = 0
        blue = 0
        for color in colors:
            r_index = color.find("red")
            g_index = color.find("green")
            b_index = color.find("blue")
            red = int(color[:r_index]) if r_index > -1 else red
            green = int(color[:g_index]) if g_index > -1 else green
            blue = int(color[:b_index]) if b_index > -1 else blue
        rolls.append([red, green, blue])
    return (id, rolls, val)


def sum_possible_game_ids(strings, max_r, max_g, max_b):
    games = map(parse_game_from_string, strings)
    possible_games = []
    for game in games:
        # print("--------------------------------------")
        # print(game[2])
        possible = True
        for roll in game[1]:
            # print(
            # f"id: {game[0]} red: {roll[0]} green: {roll[1]} blue: {roll[2]}")
            if roll[0] > max_r or roll[1] > max_g or roll[2] > max_b:
                possible = False
                # print("^Possible")

        if possible:
            possible_games.append(game[0])
        else:
            pass
            # print("Impossible")

    return sum(possible_games)


class TestDay2(unittest.TestCase):
    def test_read_input(self):
        self.assertEqual(len(read_input()), 100)

    def test_parse_value(self):
        self.assertEqual(parse_game_from_string(
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'), (1, [[4, 0, 3], [1, 2, 6], [0, 2, 0]], 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'))
        self.assertEqual(parse_game_from_string(
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue'), (2, [
                [0, 2, 1],
                [1, 3, 4],
                [0, 1, 1]
            ], 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue'))
        self.assertEqual(parse_game_from_string(
            'Game 31: 9 blue, 6 red, 7 green; 20 red, 1 green, 15 blue; 6 blue, 7 green, 17 red; 2 blue, 3 green, 6 red; 1 red, 3 blue, 2 green; 5 green, 18 red, 6 blue'), (31, [
                [6, 7, 9],
                [20, 1, 15],
                [17, 7, 6],
                [6, 3, 2],
                [1, 2, 3],
                [18, 5, 6],
            ], 'Game 31: 9 blue, 6 red, 7 green; 20 red, 1 green, 15 blue; 6 blue, 7 green, 17 red; 2 blue, 3 green, 6 red; 1 red, 3 blue, 2 green; 5 green, 18 red, 6 blue'))

    def test_sum_possible_game_ids(self):
        lines = [
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
        ]
        self.assertEqual(sum_possible_game_ids(lines, 12, 13, 14), 8)

    def test_test_day1_part1(self):
        lines = read_input()
        total = sum_possible_game_ids(lines, 12, 13, 14)
        self.assertEqual(total, 2006)


if __name__ == '__main__':
    unittest.main()
