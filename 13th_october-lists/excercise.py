# 1. Find the sum of all digits in a number.

def sum(n):
    count = 0
    while n > 0 :
        a = n % 10
        count += a
        n //= 10
    print(count)
sum(473473464)

# 2.  Write a function that takes a number N and adds all numbers from 1 to N into an empty list.
Finally, print the output list.
def num(n):
    numbers = []
    for i in range(1,n+1):
        numbers.append(i)
    print(numbers)
num(9)

# 3. Write a function that takes a number N and returns the sum of all odd numbers that are also multiples of 7 between 1 and N.

def num(n):
    total = 0
    for i in range(1,n+1):
        if i % 7 == 0 and i % 2 != 0:
            total += i
    print(total)
num(30)
num(50)





