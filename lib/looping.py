#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(f"{i}")
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    for i in int_list:
        print(i*i)

def fizzbuzz():
    # code goes here!
    for i in range(1,100):
        if (i%3 == 0 and i%5 == 0):
            print("fizzbuzz")
        elif i%3 == 0:
            print("fizz")
        elif i%5 == 0:
            print("buzz")
        else:
            print(i)

happy_new_year()
square_integers([1, 2, 3, 4, 5, 6])
fizzbuzz()