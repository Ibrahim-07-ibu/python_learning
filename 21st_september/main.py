 #1
N = int(input("enter a number"))
M = int(input("enter a number"))

if (N + M) % 2 == 0:
    print("even")
else:
    print("odd")

#2
n = int(input("enter a number"))

x = n // 10
y = n % 10

m = x + y 
j = x * y 

if m + j == n:
    print("great")
else:
    print("no")

#4
x = int(input("enter the distance in km: "))

if x <= 5:
    fare = x * 10
elif x <= 15:
    fare = (5 * 10) + (x - 5) * 8
else:
    fare = (5 * 10) + (10 * 8) + (x - 15) * 6

if fare < 50:
    fare = 50

print("Final Fare = ₹", fare)

#5
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Not a valid triangle")
else:
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

#6
n = int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)

#7
stream = input("Enter your stream (Science/Commerce/Arts): ")

match stream:
    case "Science":
        sub = input("Enter your sub-choice (Medical/Engineering): ")
        match sub:
            case "Medical":
                print("You chose Science → Medical")
            case "Engineering":
                print("You chose Science → Engineering")
            case _:
                print("Invalid sub-choice for Science")

    case "Commerce":
        sub = input("Enter your sub-choice (CA/B Com): ")
        match sub:
            case "CA":
                print("You chose Commerce → CA")
            case "B Com":
                print("You chose Commerce → B Com")
            case _:
                print("Invalid sub-choice for Commerce")

    case "Arts":
        sub = input("Enter your sub-choice (History/Literature): ")
        match sub:
            case "History":
                print("You chose Arts → History")
            case "Literature":
                print("You chose Arts → Literature")
            case _:
                print("Invalid sub-choice for Arts")

    case _:
        print("Invalid stream entered")

#8
time = int(input("Enter the show time (in 24-hour format): "))

if 9 <= time < 12:
    print("Morning Show")
elif 12 <= time < 16:
    print("Matinee Show")
elif 16 <= time < 20:
    print("Evening Show")
else:
    print("Night Show")

#9
km = float(input("Enter value in kilometers: "))
choice = input("Convert to (meters/centimeters/millimeters/miles): ")

match choice:
    case "meters":
        print(km * 1000, "meters")
    case "centimeters":
        print(km * 100000, "centimeters")
    case "millimeters":
        print(km * 1000000, "millimeters")
    case "miles":
        print(km * 0.621371, "miles")
    case _:
        print("Invalid choice")



#10
mode = input("Enter payment mode (UPI/Card/NetBanking/COD): ")

if mode == "UPI":
    print("You selected UPI payment")
elif mode == "Card":
    print("You selected Debit/Credit Card payment")
elif mode == "NetBanking":
    pr int("You selected Net Banking")
elif mode == "COD":
    print("You selected Cash on Delivery")
else:
    print("Invalid Payment Mode")

# 3
consumer_type = input("Enter consumer type (residential/commercial): ")
units = int(input("Enter units consumed: "))

bill = 0

if consumer_type == "residential":
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = units * 5
    else:
        bill = units * 7

elif consumer_type == "commercial":
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = units * 7
    else:
        bill = units * 10

else:
    print("Invalid consumer type")

if bill > 0:
    print("Bill = ₹", bill)