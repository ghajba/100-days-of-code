# -*- coding: utf-8 -*-

from collections import Counter

__author__ = "GHajba"
__copyright__ = "Copyright 2016, JaPy Szoftver Kft"
__license__ = 'MIT'

if __name__ == '__main__':
    result = 0
    with open('input4.txt','r') as infile:
        for line in infile.readlines():
            line = line.strip()
            last_dash = line.rfind('-')
            checksum_start = line.find('[')
            checksum = line[checksum_start+1:-1]
            number = int(line[last_dash+1:checksum_start])
            c = sorted(Counter(line[:last_dash].replace('-','')).most_common(), key=lambda t: (-t[1], t[0]))
            valid = True
            for i in range(len(checksum)):
                if c[i][0] != checksum[i]:
                    valid = False
                    break
            if valid:
                result += number
    print(result)