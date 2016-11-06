#! /usr/bin/python

import sys

primes = [2, 3]

def primeGenerator():
	for x in primes:
		yield x 
	candidatePrime = primes[-1] 
	while True:
		candidatePrime += 2
		if isNotDivisibleByAllPrimes(candidatePrime):
			primes.append(candidatePrime)
			yield candidatePrime

def isNotDivisibleByAllPrimes(n):
	for p in primes:
		if n % p == 0:
			return False
		if p*p > n:
			return True
	return True


def getNthPrime(n):
	i=0
	primeGen = primeGenerator()
	for prime in primeGen:
		i+=1
		if i==n:
			return prime 


n=int(sys.argv[1])
print primes
print "the %dth prime is: %d" % (n, getNthPrime(n))
