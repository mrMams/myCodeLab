#! /usr/bin/python

import sys

def getSmallestMultiple(maxNb):
	if maxNb <= 2:
		return maxNb
	candidateNb = getSmallestMultiple(maxNb - 1)
	if candidateNb % maxNb == 0:
		return candidateNb
	else:
		i = 2
		while (candidateNb * i) % maxNb != 0:
			i += 1
		return candidateNb *i

maxNb = int(sys.argv[1])
print "Smallest positive nb divisible by all numbers from 1 to %d is: %d" % (maxNb,getSmallestMultiple(maxNb))

