#!/usr/bin/python
import sys

'''
Principe: crible d'erathosthene applique sur les facteurs de n
candidats = liste des nombres de 2 a n
prime = 2
primes = [2]
tant que candidats non vide
	eliminer tous les nombres divisibles par prime de candidats
	prime = le plus petit element de candidats
	primes.add(prime)
	candidats.remove(prime)
retourner le plus grand element de primes
'''

# Returns the smallest factor of a number (is always prime !)
def smallestFactor(n):
	i = 2
	while n % i != 0 :
		i += 1
	return i

# The main function
def largestPrimeFactor(n):
	# Considering factors only
	# TODO: find a better way to generate candidates
	smallestFact = smallestFactor(n)
	print "Smallest factor of %d: %d" % (n,smallestFact)
	print "Therefore, the largest factor is %d" % (n/smallestFact)
	candidats = [x for x in xrange(smallestFact, (n/smallestFact) + 1) if n % x == 0]
	print "Factors: ", candidats
	if not candidats:
		return n
	prime = candidats[0]
	while len(candidats) > 1 :
		candidats = [ x for x in candidats if x % prime != 0 ]
		print candidats
		if candidats:
			prime = candidats[0]

	return prime

# Main
number = int(sys.argv[1])
print "Largest prime factor of %d: " % (number)
print largestPrimeFactor(number)

