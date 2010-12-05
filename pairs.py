#!/usr/bin/env python

import random
import string
import sys
import math

numpairs = int(sys.argv[1])

r = random.SystemRandom()

vowels = set('aeiou')
cons = set(string.lowercase) - vowels
vowels = list(vowels)
cons = list(cons)

def rand_pair():
    c = r.choice(cons)
    v = r.choice(vowels)
    return c + v

rv = [rand_pair() for i in xrange(numpairs)]
print ''.join(rv)

print 'entropy: ',
print math.log((len(cons)*len(vowels))**numpairs)/math.log(2)
