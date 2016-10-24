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

# Recursive version
def largestPrimeFactorRecursive(n):
	firstPrimeFactor = smallestFactor(n)
	return n if n == firstPrimeFactor else largestPrimeFactorRecursive(n/firstPrimeFactor)

# Main
number = int(sys.argv[1])
print "Largest prime factor of %d: %d" % (number, largestPrimeFactorRecursive(number))

