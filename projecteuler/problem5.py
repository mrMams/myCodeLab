#! /usr/bin/python

import sys

# TODO: check only prime numbers instead of all integers
def isDivisibleByAllIntegersBelow(nb, maxNb):
	for i in xrange(2, maxNb+1):
		if nb % i != 0:
			return False
	return True

# Testing isDivisibleByAllIntegersBelow
print "Is %d divisible by all numbers from 1 to %d? %s" % (2520, 10, isDivisibleByAllIntegersBelow(2520, 10))
print "Is %d divisible by all numbers from 1 to %d? %s" % (2520, 11, isDivisibleByAllIntegersBelow(2520, 11))


def getSmallestMultiple(maxNb):
	if maxNb <= 2:
		return maxNb
	candidateNb = getSmallestMultiple(maxNb - 1)
	while not isDivisibleByAllIntegersBelow(candidateNb, maxNb):
		candidateNb += 1
	return candidateNb

maxNb = int(sys.argv[1])
print "Smallest positive nb divisible by all numbers from 1 to %d is: %d" % (maxNb,getSmallestMultiple(maxNb))

