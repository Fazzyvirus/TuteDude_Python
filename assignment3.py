#Task 1: Calculate Factorial Using a Function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(2)
print(result)

#Task 2: Using the Math Module for Calculations
num = int(input('Enter a number: '))

import math
print(math.sqrt(num))
print(math.log(num))
print(math.sin(num))