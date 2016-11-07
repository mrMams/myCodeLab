#! /usr/bin/python

import sys

def getLargestProduct(bigNumberFile, nbAdjacentDigits):
	factors = readFirstDigits(bigNumberFile, nbAdjacentDigits)
	largestProduct = computeProduct(factors)

	while True:
		factors.pop()
		nextDigit = bigNumberFile.read(1)
		if not nextDigit:
			break
		else:
			if isDigit(nextDigit):
				factors.insert(0, int(nextDigit))
				product = computeProduct(factors)
				if product > largestProduct:
					largestProduct = product
	
	return largestProduct

def readFirstDigits(f,n):
	result = []
	for i in xrange(n):
		result.insert(0, int(f.read(1)))
	return result

def computeProduct(factors):
	product = 1
	for factor in factors:
		product *= factor
	return product

def isDigit(char):
	try:
		int(char)
		return True
	except ValueError:
		return False

bigNumberFileName = sys.argv[1]
nbAdjacentDigits = int(sys.argv[2])

with open(bigNumberFileName, "r") as bigNumberFile:
	print "The largest product is: %d" % getLargestProduct(bigNumberFile , nbAdjacentDigits)




