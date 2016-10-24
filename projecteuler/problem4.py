#!/usr/bin/python

import sys

def isPalindrome(nstr):
	if len(nstr) == 1: 
		return True
	elif len(nstr) == 2:
		return nstr[0]==nstr[1]
	else:
		return nstr[0]==nstr[-1] and isPalindrome(nstr[1:-1])

# Main method - can be improved, by skipping all remaining values of a, when a result is found
def largestPalindromeProduct(nbDigits):
	result = -1
	minValue = 10 ** (nbDigits -1)
	maxValue = (10 ** nbDigits) - 1
	for a in xrange(maxValue, minValue, -1):
		for b in xrange(a, minValue, -1):
			c=a*b
			if c > result and isPalindrome(str(c)):
				print "%d * %d = %d" % (a,b,c)
				result =  int(c)
				break #No need to carry on, decrementing a
	return result


def listPalidromeProducts(nbDigits):
	minValue = 10 ** (nbDigits -1)
	maxValue = (10 ** nbDigits) - 1
	print "Range: %d - %d" % (minValue, maxValue)
	for a in xrange(maxValue, minValue, -1):
		for b in xrange(a, minValue, -1):
			c=str(a*b)
			if isPalindrome(c):
				print "%d * %d = %s" % (a,b,c)

nbDigits = int(sys.argv[1])
#print "List of palidrome product of two %d-digit numbers:"
#listPalidromeProducts(nbDigits)
print "Largest palidrome product of two %d-digit numbers: %d" % (nbDigits, largestPalindromeProduct(nbDigits))

