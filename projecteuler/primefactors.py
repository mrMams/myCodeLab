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

def largestPrimeFactor(n):
	# Considering factors only
	# TODO: find a better way to generate candidates
	candidats = [x for x in xrange(2, n/2) if n % x == 0]
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

