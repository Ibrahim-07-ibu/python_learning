# problem 1

a = int(input("enter a number"))
b = int(input("enter a number"))
if (a + b) % 5 == 0:
    print(1)
else: 
    print(0)# problem 2
N = int(input("enter a number"))

if N % 7 == 0:
    print("yes")
else:
    print("no")# problem 3
A= int(input("enter order amount: "))

if A > 500:
    print("free delivery")
    total = A
else:
    print("delivery charges ₹50 added")
    total = A + 50

print("Total amount:" total)# problem 5

a = int(input("enter value"))
b = int(input("enter value"))
c = int(input("enter value"))

if a + b > c :
    print("yes")
else:
    print("no")
    
# problem 6

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

# problem 7
A = int(input("enter a year"))
print(A)

if A >= 2001 and A<= 2100:
  print("21st Century")
else :
  print("Not in 21st Century")

# problem 8
n = int(input("enter a number"))
print(n)

if n%3 == 0 or n%5 == 0:
  print("divisible")
else :
  print("not divisible")


# problem 8
n = int(input("enter your year"))
print(n)

if n== 2020:
  print("Y")
else:
  print("N")

# problem 9
n = int(input("enter your year"))
print(n)

if n== 1900 :
  print("leap year")
else:
  print("not a leap year")

