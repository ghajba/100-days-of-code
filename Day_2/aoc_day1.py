# -*- coding: utf-8 -*-

__author__ = "GHajba"
__copyright__ = "Copyright 2016, JaPy Szoftver Kft"
__license__ = 'MIT'

x_direction = [0, 1, 0, -1]
y_direction = [1, 0, -1, 0]

direction = 0

if __name__ == '__main__':
    with open('input1.txt') as infile:
        data = infile.readline().split(', ')

    x = 0
    y = 0

    for info in data:
        if info[0] == 'L':
            direction = (direction + 3) % 4
        else:
            direction = (direction + 1) % 4
        x += x_direction[direction] * int(info[1:])
        y += y_direction[direction] * int(info[1:])
    print(abs(x) + abs(y))
