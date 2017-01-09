# -*- coding: utf-8 -*-

__author__ = "GHajba"
__copyright__ = "Copyright 2016, JaPy Szoftver Kft"
__license__ = 'MIT'

if __name__ == '__main__':
    count = 0
    with open('input3.txt', 'r') as infile:
        t = [[], [], []]
        l = 0
        for line in infile.readlines():
            if l > 0 and l % 3 == 0:
                for i in range(3):
                    data = sorted(t[i])
                    if data[0] + data[1] > data[2]:
                        count += 1
                t = [[], [], []]
            l += 1
            x, y, z = [int(d) for d in line.split()]
            t[0].append(x)
            t[1].append(y)
            t[2].append(z)
        else:
            for i in range(3):
                data = sorted(t[i])
                if data[0] + data[1] > data[2]:
                    count += 1

    print(count)
