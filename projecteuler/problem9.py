#! /usr/bin/python

import sys

def findPythagoreanTripletProduct(tripletSum):
	for a in xrange(tripletSum-1, 0, -1):
		for b in xrange(a-1, 0, -1):
			c = tripletSum - a - b
			if a*a + b*b == c*c:
				return a*b*c


tripletSum = int(sys.argv[1])
print "The product of the pythagorean triplet for which a + b + c = %d is: %d" % (tripletSum, findPythagoreanTripletProduct(tripletSum))
