import sys

fibMemo = {1: 1, 2: 2}
def fib(n):
        if n in fibMemo:
                return fibMemo[n]
        else:
                for i in range(3, n+1):
                        fibMemo[i] = fibMemo[i-1] + fibMemo[i-2]
                return fibMemo[n]

number = int(sys.argv[1])
for i in range(1, number+1):
        fibi = fib(i)
        print "fib(%d) = %d %s" % (i, fibi, ("pair" if fibi%2 == 0 else ""))

# TODO:
# - Algo: integrer cette fonction avec la fonction fib ci-dessus pour memoriser les calculs intermediaires de fib
# - Python: utiliser un generateur
def sumPairFib():
        k, currentFib = 2, fib(2)
        result = currentFib
        while currentFib < 4000000:
                k, currentFib = (k+3), fib(k)
                result += currentFib
                print "k=%d, currentFib=%d, result=%d" % (k, currentFib, result)
        return result

print "La somme des termes voulus est: %d" % sumPairFib()
