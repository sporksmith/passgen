#!/usr/bin/env python3

import random
import string
import sys
import math

def pairs(numpairs, r=random.SystemRandom(), useCaps=True):
    vowels = set('aeiou')
    cons = set(string.ascii_lowercase) - vowels

    # r.choice requires an indexable data structure
    vowels = list(vowels)
    cons = list(cons)

    rand_pair = lambda: (r.choice(cons) + r.choice(vowels))

    pw = [rand_pair() for i in range(numpairs)]
    if useCaps:
        pw = map(lambda x: r.choice([x, x.upper()]), pw)
    pw = ''.join(pw)
    entropy = math.log((len(cons)*len(vowels)*(useCaps and 4 or 1))**numpairs)/math.log(2)
    return (pw, entropy)

if __name__ == '__main__':
    (pw, entropy) = pairs(int(sys.argv[1]), useCaps=(sys.argv[2]=='t'))
    print(pw)
    print('entropy: %f bits' % entropy)

