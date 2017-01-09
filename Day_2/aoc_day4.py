# -*- coding: utf-8 -*-

from collections import Counter

__author__ = "GHajba"
__copyright__ = "Copyright 2016, JaPy Szoftver Kft"
__license__ = 'MIT'

alphabet = 'abcdefghijklmnopqrstuvwxyz'

if __name__ == '__main__':
    with open('input4.txt', 'r') as infile:
        for line in infile.readlines():
            line = line.strip()
            last_dash = line.rfind('-')
            checksum_start = line.find('[')
            room_name = line[:last_dash]
            number = int(line[last_dash + 1:checksum_start])
            decrypted = ''
            for c in room_name:
                if c == '-':
                    decrypted += ' '
                else:
                    decrypted += alphabet[(alphabet.index(c) + number) % 26]
            if 'north' in decrypted:
                print(number)
                break
