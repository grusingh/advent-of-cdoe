from utils import read_input
import unittest
import sys

sample = [
    'seeds: 79 14 55 13',
    '',
    'seed-to-soil map:',
    '50 98 2',
    '52 50 48',
    '',
    'soil-to-fertilizer map:',
    '0 15 37',
    '37 52 2',
    '39 0 15',
    '',
    'fertilizer-to-water map:',
    '49 53 8',
    '0 11 42',
    '42 0 7',
    '57 7 4',
    '',
    'water-to-light map:',
    '88 18 7',
    '18 25 70',
    '',
    'light-to-temperature map:',
    '45 77 23',
    '81 45 19',
    '68 64 13',
    '',
    'temperature-to-humidity map:',
    '0 69 1',
    '1 0 69',
    '',
    'humidity-to-location map:',
    '60 56 37',
    '56 93 4'
]


def get_seeds(lines):
    seeds = []
    s = lines[0][7:].split(' ')
    for i in s:
        seeds.append(int(i))
    return seeds


def get_mapping(m, lines):
    start = None
    ranges = []
    for li in range(len(lines)):
        l = lines[li]
        if m in l:
            start = li
        elif start is not None and (len(l.strip()) == 0 or li == len(lines)):
            break
        elif start is not None and len(l.strip()) > 0:
            ranges.append(l)
    mappings = []
    for r in ranges:
        parts = r.split(' ')
        d = int(parts[0])
        s = int(parts[1])
        l = int(parts[2])

        mappings.append([d, s, l])
    return mappings


def get_value(v, lst):
    for li in range(len(lst)):
        parts = lst[li]
        d = parts[0]
        s = parts[1]
        l = parts[2]

        if v >= s and v < s+l:
            i = v - s
            r = d + i
            return r
    return v


def get_seed_to_location(seed, lines):
    seed_to_soil_map = get_mapping("seed-to-soil map:", lines)
    soil_to_fertilizer_map = get_mapping("soil-to-fertilizer map:", lines)
    fertilizer_to_water_map = get_mapping("fertilizer-to-water map:", lines)
    water_to_light_map = get_mapping("water-to-light map:", lines)
    light_to_temperature_map = get_mapping("light-to-temperature map:", lines)
    temperature_to_humidity_map = get_mapping(
        "temperature-to-humidity map:", lines)
    humidity_to_location_map = get_mapping("humidity-to-location map:", lines)

    soil = get_value(seed, seed_to_soil_map)
    # print("seed_to_soil_map", seed, soil)
    fert = get_value(soil, soil_to_fertilizer_map)
    # print("soil_to_fertilizer_map", soil, fert)
    water = get_value(fert, fertilizer_to_water_map)
    # print("fertilizer_to_water_map", fert, water)
    light = get_value(water, water_to_light_map)
    # print("water_to_light_map", water, light)
    temp = get_value(light, light_to_temperature_map)
    # print("light_to_temperature_map", light, temp)
    hum = get_value(temp, temperature_to_humidity_map)
    # print("temperature_to_humidity_map", temp, hum)
    loc = get_value(hum, humidity_to_location_map)
    # print("humidity_to_location_map", hum, loc)
    # print("seed: ", seed, " loc: ", loc)

    return loc


def get_lowest_location_number(lines):
    min_loc = sys.maxsize
    seeds = get_seeds(lines=lines)

    for seed in seeds:
        loc = get_seed_to_location(seed=seed, lines=lines)

        if loc < min_loc:
            min_loc = loc

    return min_loc


class TestDay5(unittest.TestCase):
    def test_get_seeds(self):
        seeds = get_seeds(sample)
        self.assertEqual(seeds, [79, 14, 55, 13])

    def test_sample(self):
        m = get_mapping("seed-to-soil map:", sample)
        self.assertEqual(len(m), 2)
        m = get_mapping("humidity-to-location map:", sample)
        self.assertEqual(len(m), 2)

    def test_lowest_number_sample(self):
        v = get_lowest_location_number(lines=sample)
        self.assertEqual(v, 35)

    def test_lowest_number_part1(self):
        lines = read_input("day5.txt")
        v = get_lowest_location_number(lines=lines)
        self.assertEqual(v, 35)

    def test_get_seed_to_location(self):
        """
Seed number 79 corresponds to soil number 81.
Seed number 14 corresponds to soil number 14.
Seed number 55 corresponds to soil number 57.
Seed number 13 corresponds to soil number 13.

        """
        self.assertEqual(get_seed_to_location(79, sample), 82)
        self.assertEqual(get_seed_to_location(14, sample), 43)
        self.assertEqual(get_seed_to_location(55, sample), 86)
        self.assertEqual(get_seed_to_location(13, sample), 35)


if __name__ == "__main__":
    unittest.main()
