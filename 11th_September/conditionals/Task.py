# task 1
a = int(input("enter a number"))
b = int(input("enter a number"))

if (a + b) % 5 == 0:
    print(1)
else:
    print(0)

# task 2
N = int(input("enter a number9"))

if N % 7 == 0:
    print("yes")
else:
    print("no")

A= int(input("Enter order amount: "))

if A > 500:
    print("free delivery")
    total = A
else:
    print("Delivery charge ₹50 added")
    total = A + 50

print("Total amount:", total)

a = int(input("enter value"))
b = int(input("enter value"))
c = int(input("enter value"))

if a + b > c :
    print("yes")
else:
    print("no")


x = int(input("enter your age"))

if x < 13:
    print("child")
else:
    if  x < 19:
        print("Teen")
    else:
        if x < 59:
            print("Adult")
        else:
            if  x < 100:
                print("Senior")
