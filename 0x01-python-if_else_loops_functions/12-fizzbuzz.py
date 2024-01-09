#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101, 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=' ')
        elif num % 5 == 0:
            if num == 100:
                print("Buzz".format(num), end=' ')
            else:
                print("Buzz", end=' ')
        elif num % 3 == 0:
            print("Fizz", end=' ')
        else:
            print("{}".format(num), end=' ')
