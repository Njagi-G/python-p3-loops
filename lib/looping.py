#!/usr/bin/env python3

# Question 1
def happy_new_year():
    # code goes here!
    pass
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

happy_new_year()


# Question 2
def square_integers(int_list):
    # code goes here!
    pass
    int_list_squared = [int ** 2 for int in int_list]
    return int_list_squared

square_integers([1, 2, 3, 4, 5])
print(square_integers([1, 2, 3, 4, 5]))


# Question 3
def fizzbuzz():
    # code goes here!
    pass
    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

fizzbuzz()



