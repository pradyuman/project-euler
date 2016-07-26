/*
Problem 3 - Largest Prime Factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Solution - 6857
*/
package main

import "fmt"

func main() {
	largest := 0
	num := 600851475143
	for i := 2; i * i <= num; i = increment(i) {
		if num % i == 0 {
			num /= i;
			largest = i
		}
	}

	if num > largest {
		largest = num
	}

	fmt.Printf("%d\n", largest)
}

func increment(num int) int {
	if num == 2 {
		return 3
	} else {
		return num + 2
	}
}
