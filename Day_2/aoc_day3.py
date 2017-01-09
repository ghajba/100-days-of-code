# -*- coding: utf-8 -*-

__author__ = "GHajba"
__copyright__ = "Copyright 2016, JaPy Szoftver Kft"
__license__ = 'MIT'

if __name__ == '__main__':
    count = 0
    with open('input3.txt','r') as infile:
        for line in infile.readlines():
            data = sorted([int(d) for d in line.split()])
            if data[0] + data[1] > data[2]:
                count += 1
    print(count)