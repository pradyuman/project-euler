#Problem 3 - Largest Prime Factor
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

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