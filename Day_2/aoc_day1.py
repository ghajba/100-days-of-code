# -*- coding: utf-8 -*-

__author__ = "GHajba"
__copyright__ = "Copyright 2016, JaPy Szoftver Kft"
__license__ = 'MIT'

x_direction = [0, 1, 0, -1]
y_direction = [1, 0, -1, 0]

direction = 0

locations = set()

if __name__ == '__main__':
    with open('input1.txt') as infile:
        data = infile.readline().split(', ')

    x = 0
    y = 0
    twice = []

    for info in data:
        if info[0] == 'L':
            direction = (direction + 3) % 4
        else:
            direction = (direction + 1) % 4
        x_d = x_direction[direction]
        y_d = y_direction[direction]

        for i in range(1, int(info[1:]) + 1):
            x += x_d
            y += y_d
            if (x, y) in locations:
                twice.append(abs(x) + abs(y))
                break
            else:
                locations.add((x, y))
    print(twice[0])
