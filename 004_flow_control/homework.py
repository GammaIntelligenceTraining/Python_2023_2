# FizzBuzz
# For range of numbers from 1 to 100
# Write a program that prints Fizz if number divides by 3 without remainder
# prints Buzz if number divides by 5 without remainder
# prints FizzBuzz if number divides by 3 and 5 without remainder

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('FIZZBUZZ')
    elif num % 3 == 0:
        print('FIZZ')
    elif num % 5 == 0:
        print('BUZZ')
    else:
        print(num)