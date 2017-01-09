# -*- coding: utf-8 -*-

__author__ = "GHajba"
__copyright__ = "Copyright 2016, JaPy Szoftver Kft"
__license__ = 'MIT'

keypad = [
    [None, None, '1', None, None],
    [None, '2', '3', '4', None],
    ['5', '6', '7', '8', '9'],
    [None, 'A', 'B', 'C', None],
    [None, None, 'D', None, None],
]

if __name__ == '__main__':
    with open('input2.txt', 'r') as infile:
        lines = infile.readlines()
        row = 3
        button = 0
        for l in lines:
            for c in l:
                if c == 'R':
                    if button == 4 or keypad[row][button + 1] is None: continue
                    button += 1
                if c == 'L':
                    if button == 0 or keypad[row][button - 1] is None: continue
                    button -= 1
                if c == 'U':
                    if row == 0 or keypad[row - 1][button] is None: continue
                    row -= 1
                if c == 'D':
                    if row == 4 or keypad[row + 1][button] is None: continue
                    row += 1
            print(keypad[row][button])
