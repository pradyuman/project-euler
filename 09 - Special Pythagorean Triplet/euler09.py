#Problem 9 - Special Pythagorean Triplet
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2.
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#Solution
#31875000

def isTriplet():
    for i in range(100,750):
        for j in range(200,750):
            for k in range(300,750):
                if i ** 2 + j **2 == k**2:
                    if (i + j + k == 1000) & (i < j) & (j < k):
                        print(i*j*k)
                        return

isTriplet()
