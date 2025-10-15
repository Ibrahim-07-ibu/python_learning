 Given a list of integers, check if a number is present in the list or not. Print “found” else, print “not found”

def check_number_in_list():
    numbers = [10, 20, 30, 40, 50]
    num = int(input("Enter a number: "))
    if num in numbers:
        print("found")
    else:
        print("not found")

Check if the sum of all numbers in a list is even or not

def check_even_or_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

Given two numbers a and b and a list of numbers num_list. Print all the elements in num_list between a and b.

def print_numbers_in_range():
    num_list = [8, 1, 0, 19, 11, 28, 3, 5]
    a = int(input("Enter lower limit: "))
    b = int(input("Enter upper limit: "))
    print("Numbers between", a, "and", b, ":")
    for num in num_list:
        if a <= num <= b:
            print(num)