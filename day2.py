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
    red = 0
    green = 0
    blue = 0
    for g in game_strings:
        colors = g.split(",")
        for color in colors:
            r_index = color.find("red")
            g_index = color.find("green")
            b_index = color.find("blue")
            red += int(color[:r_index]) if r_index > -1 else 0
            green += int(color[:g_index]) if g_index > -1 else 0
            blue += int(color[:b_index]) if b_index > -1 else 0
    return (id, red, green, blue, val)


def sum_possible_game_ids(strings, max_r, max_g, max_b):
    games = map(parse_game_from_string, strings)
    possible_games = []
    for game in games:
        print("--------------------------------------")
        print(game[4])
        print(f"id: {game[0]} red: {game[1]} green: {game[2]} blue: {game[3]}")
        if game[1] <= max_r and game[2] <= max_g and game[3] <= max_b:
            print("Possible")
            possible_games.append(game[0])
        else:
            print("Impossible")
    return sum(possible_games)


class TestDay2(unittest.TestCase):
    def read_input(self):
        self.assertEqual(len(read_input()), 100)

    def parse_value(self):
        self.assertEqual(parse_game_from_string(
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'), (1, 5, 4, 9))
        self.assertEqual(parse_game_from_string(
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue'), (2, 1, 6, 6))
        self.assertEqual(parse_game_from_string(
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'), (3, 25, 26, 11))
        self.assertEqual(parse_game_from_string(
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red'), (4, 23, 7, 21))
        self.assertEqual(parse_game_from_string(
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'), (5, 7, 5, 3))
        self.assertEqual(parse_game_from_string(
            'Game 1: 10 green, 5 blue; 1 red, 9 green, 10 blue; 5 blue, 6 green, 2 red; 7 green, 9 blue, 1 red; 2 red, 10 blue, 10 green; 7 blue, 1 red'), (1, 7, 42, 46))
        self.assertEqual(parse_game_from_string(
            'Game 14: 9 green, 4 red; 6 blue, 1 red, 7 green; 3 blue, 5 green'), (14, 5, 21, 9))
        self.assertEqual(parse_game_from_string(
            'Game 31: 9 blue, 6 red, 7 green; 20 red, 1 green, 15 blue; 6 blue, 7 green, 17 red; 2 blue, 3 green, 6 red; 1 red, 3 blue, 2 green; 5 green, 18 red, 6 blue'), (31, 68, 25, 41))
        # self.assertEqual(parse_game_from_string(''), (0, 0, 0, 0))

    def sum_possible_game_ids(self):
        lines = [
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
        ]
        self.assertEqual(sum_possible_game_ids(lines, 12, 13, 14), 8)

    def test_day1_part1(self):
        lines = read_input()
        total = sum_possible_game_ids(lines, 12, 13, 14)
        self.assertEqual(total, 0)


if __name__ == '__main__':
    unittest.main()
