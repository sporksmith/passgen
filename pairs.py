#!/usr/bin/env python

import random
import string
import sys
import math

def rand_pair(r):
    c = r.choice(cons)
    v = r.choice(vowels)
    return c + v

def pairs(numpairs, r=random.SystemRandom()):
    vowels = set('aeiou')
    cons = set(string.lowercase) - vowels

    # r.choice requires an indexable data structure
    vowels = list(vowels)
    cons = list(cons)

    rand_pair = lambda: (r.choice(cons) + r.choice(vowels))

    pw = [rand_pair() for i in xrange(numpairs)]
    pw = ''.join(pw)
    entropy = math.log((len(cons)*len(vowels))**numpairs)/math.log(2)
    return (pw, entropy)

if __name__ == '__main__':
    (pw, entropy) = pairs(int(sys.argv[1]))
    print pw
    print 'entropy: %f bits' % entropy

