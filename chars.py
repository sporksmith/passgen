#!/usr/bin/env python

import random
import string
import sys
import math

def chars(numchars, r=random.SystemRandom()):
    candidates = set()
    candidates.update(string.ascii_lowercase)
    candidates.update(string.ascii_uppercase)
    candidates.update(string.punctuation)
    candidates.update(string.digits)

    # r.choice requires an indexable data structure
    candidates = list(candidates)

    pw = [r.choice(candidates) for i in xrange(numchars)]
    pw = ''.join(pw)
    entropy = math.log(len(candidates)**numchars)/math.log(2)
    return (pw, entropy)

if __name__ == '__main__':
    (pw, entropy) = chars(int(sys.argv[1]))
    print pw
    print 'entropy: %f bits' % entropy

