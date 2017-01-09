# -*- coding: utf-8 -*-

import hashlib

__author__ = "GHajba"
__copyright__ = "Copyright 2016, JaPy Szoftver Kft"
__license__ = 'MIT'

if __name__ == '__main__':
    i = 0
    r = [0] * 8
    t = set()
    while True:
        md5 = hashlib.md5(('uqwqemis' + str(i)).encode()).hexdigest()
        i += 1
        if md5.startswith('00000'):
            if md5[5] not in '12345670' or md5[5] in t:
                continue
            r[int(md5[5])] = md5[6]
            t.add(md5[5])
        if len(t) == 8:
            break
    print(''.join(r))
