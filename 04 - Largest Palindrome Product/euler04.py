A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


#Solution
#4613732

MAX_NUMBER = 600851475143

def isprime(prime):
    prime *= 1.0
    if prime % 2 == 0 and prime != 2:
        return False
    for divisor in range(3,int(prime ** 0.5) + 1 , 2):
        if prime % divisor == 0:
            return False
    return True

prime = 1
#Dividing by lowest prime number and then going up
while MAX_NUMBER != 1:
	prime += 1
	while(not(isprime(prime))):
		prime += 1
	while not(MAX_NUMBER % prime):
		MAX_NUMBER = MAX_NUMBER / prime

print(prime)