# -*- coding: utf-8 -*-

__author__ = "GHajba"
__copyright__ = "Copyright 2016, JaPy Szoftver Kft"
__license__ = 'MIT'

if __name__ == '__main__':
    with open('input2.txt', 'r') as infile:
        lines = infile.readlines()
        button = 5
        for l in lines:
            for c in l:
                if c == 'R':
                    if button in [3, 6, 9]: continue
                    button += 1
                if c == 'L':
                    if button in [1, 4, 7]: continue
                    button -= 1
                if c == 'U':
                    if button in [1, 2, 3]: continue
                    button -= 3
                if c == 'D':
                    if button in [7, 8, 9]: continue
                    button += 3
            print(button)
