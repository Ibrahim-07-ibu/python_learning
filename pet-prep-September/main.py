# 1
x = int(input("enter a year"))

if (x % 400 == 0) or (x % 4 == 0 and x % 100 != 0) :
    print("Y")
else:
    print("N")
    
# 2 
num = int(input("Enter a positive integer: "))

digit_sum = 0

while num > 0:
    digit = num % 10         
    digit_sum =digit_sum + digit       
    num = num // 10 

print(digit_sum)
# 3 
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

 even_sum = 0

 for i in range(a, b + 1):
    if i % 2 == 0:         
        even_sum = even_sum + i

print(even_sum)

# 4
x = int(input("enter the weight of the product"))

if x <= 5 :
    cost = 10
elif  x > 5 and x <= 20 :
    cost = 20
elif x > 20 :
    cost = 50 

tax = cost * 0.05
print(cost + tax)







