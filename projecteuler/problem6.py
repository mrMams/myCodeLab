#! /usr/bin/python

import sys

# Returns the sum square difference for the first n natural numbers
def sumSquareDiff(n):
	return squareOfSum(n) - sumOfSquare(n)

def squareOfSum(n):
	return (n*(n+1))**2/4

def sumOfSquare(n):
	result = (n*((n+1)**2))/2

	# Computing second term
	secondTerm = 0
	for i in xrange(1, n/2 + 1):
		secondTerm += i * (n-i+1) 
	secondTerm *= 2
	result -= secondTerm

	# if n is odd, ceiling of (n/2)**2 must be added 
	if n % 2 == 1:
		result += (n/2 + 1)**2
	
	return result

n=int(sys.argv[1])
print "squareOfSum(%d) = %d" % (n, squareOfSum(n))
print "sumOfSquare(%d) = %d" % (n, sumOfSquare(n))
print "sumSquareDiff(%d) = %d" % (n, sumSquareDiff(n))

