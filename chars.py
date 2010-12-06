#!/usr/bin/env python

import random
import string
import sys
import math

class charsPass:
    def __init__(self, r=random.SystemRandom(), useLower=True, useUpper=True, usePunct=True, useDigits=True):
        self.r = r

        self.candidates = set()
        if useLower: self.candidates.update(string.ascii_lowercase)
        if useUpper: self.candidates.update(string.ascii_uppercase)
        if usePunct: self.candidates.update(string.punctuation)
        if useDigits: self.candidates.update(string.digits)
        self.candidates = list(self.candidates)

    def entropy_of_length(self, length):
        return math.log(len(self.candidates)**length)/math.log(2)

    def length_of_entropy(self, entropy):
        length = 1
        while (entropy_of_length(length) < entropy):
            length += 1
        return length

    def generate_length(self, length):
        pw = [self.r.choice(self.candidates) for i in xrange(length)]
        pw = ''.join(pw)
        return (pw, self.entropy_of_length(length))

    def generate_entropy(self, entropy):
        return self.generate_length(self.length_of_entropy(entropy))


if __name__ == '__main__':
    g = charsPass(useLower=True, useUpper=True, usePunct=True, useDigits=True)
    (pw, entropy) = g.generate_length(int(sys.argv[1]))
    print pw
    print 'entropy: %f bits' % entropy
