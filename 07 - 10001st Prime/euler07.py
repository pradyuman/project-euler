#Problem 7 - 10001st prime
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?

#Solution
#104743

def isprime(prime):
    prime *= 1.0
    if prime % 2 == 0 and prime != 2:
        return False
    for divisor in range(3,int(prime ** 0.5) + 1 , 2):
        if prime % divisor == 0:
            return False
    return True

number = 1
count = 0
while count != 10001:
	number += 1
	if isprime(number):
		count += 1

print(number)