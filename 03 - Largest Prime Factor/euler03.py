#Problem 3 - Largest Prime Factor
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#Solution
#4613732

MAX_NUMBER = 600851475143

#Finding next lowest prime number
def nextprime(num,prime):
	#Making num a float if num isn't already
	num *= 1.0
	#Taking out all even numbers
	if num == 2 and num > prime:
		return 2
	if  num % 2 == 0:
		return 0
	for i in range(2,int(num**0.5)+1):
		if num % i == 0:
			return 0
		elif i > prime:
			return i

prime = 1
#Dividing by lowest prime number and then going up
while MAX_NUMBER != 1:
	for i in range(2,int(MAX_NUMBER ** 0.5)):
		prime = nextprime(i, prime)
		break
	while not(MAX_NUMBER % 5):
		MAX_NUMBER = MAX_NUMBER / prime

print(prime)