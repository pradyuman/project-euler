#Problem 10 - Summation of Primes

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

#Solution
#142913828922

def isprime(prime):
    prime *= 1.0
    if prime % 2 == 0 and prime != 2:
        return False
    for divisor in range(3,int(prime ** 0.5) + 1 , 2):
        if prime % divisor == 0:
            return False
    return True

number = 1
primesum = 0
while number < 2000001:
	number += 1
	if isprime(number):
		primesum += number

print(primesum)


