#Problem 6 - Sum Sqaure Difference
#The sum of the squares of the first ten natural numbers is: 1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is: (1 + 2 + ... + 10)^2 = 552 = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#Solution
#25164150

total = 0
sumsquare = 0

for i in range(1,101):
    total += i #Calculating square of sums (will be completed below)
    sumsquare += i ** 2 #Calculating sum of sqaures

squaresum = total ** 2

print(abs(sumsquare - squaresum))
