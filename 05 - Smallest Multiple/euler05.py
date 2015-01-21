#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Solution
#232792560 - Took 42s

def evenlyDivisible():
    i = 20
    while i:
        test = 0
        for j in range(2,21):
            if i % j:
                test += 1
        if not(test):
            print(i)
            return
        i += 20

evenlyDivisible()