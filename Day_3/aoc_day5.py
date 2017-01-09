# -*- coding: utf-8 -*-

import hashlib

__author__ = "GHajba"
__copyright__ = "Copyright 2016, JaPy Szoftver Kft"
__license__ = 'MIT'

if __name__ == '__main__':
    i = 0
    r = []
    while True:
        md5 = hashlib.md5(('uqwqemis' + str(i)).encode()).hexdigest()
        if md5.startswith('00000'):
            r.append(md5[5])
        if len(r) == 8:
            break
        i += 1
    print(''.join(r))
