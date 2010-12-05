#!/usr/bin/env python

import random
import string
import sys
import math

wordsfile = 'diceware.wordlist.asc.txt'
f = open(wordsfile)
lines = f.readlines()
words = map(lambda x: x.split()[1], lines)

r = random.SystemRandom()

numwords = int(sys.argv[1])

rv = [r.choice(words).capitalize() for i in xrange(numwords)]
print ''.join(rv)
print 'entropy: ',
print math.log(len(words)**numwords)/math.log(2)
