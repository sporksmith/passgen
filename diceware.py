#!/usr/bin/env python

import random
import string
import sys
import math

# return (passString, bitsentropy)
def diceware(numwords, r=random.SystemRandom(), wordsfile='diceware.wordlist.asc.txt'):
    f = open(wordsfile)
    lines = f.readlines()
    words = map(lambda x: x.split()[1], lines)

    rv = [r.choice(words).capitalize() for i in xrange(numwords)]

    pw = ''.join(rv)
    entropy = math.log(len(words)**numwords)/math.log(2)
    return (pw, entropy)

if __name__ == '__main__':
    (pw, entropy) = diceware(int(sys.argv[1]))
    print pw
    print 'entropy: %f bits' % entropy
