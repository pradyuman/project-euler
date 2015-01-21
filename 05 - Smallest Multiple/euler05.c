/*2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 *What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

 *Solution
 *232792560 - Took 0.88s
 */

#include <stdio.h>

int evenlyDivisible(void);

int main(void) {
    int result;

    result = evenlyDivisible();
    printf("%d\n", result);

    return 0;
}

int evenlyDivisible(void){
    int i = 20;
    int j;
    while(i) {
        int test = 0;
        for(j=1; j<=20; j++){
            if(i % j) {
                test += 1;
            }
        }
        if(!test)
            return i;
        i += 20;
    }
    return 0;
}
