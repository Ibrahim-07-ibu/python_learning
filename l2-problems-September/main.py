# L2 problems 

# problem 1
def is_between(n,l,r):
     if n== n>l and n== n <r:
          print("yes")
     else:
          print("no")
# problem 2
def calculator(operator, number1, number2):
    #Write your code here
    if operator == "+" :
        print(number1 + number2)
    elif operator == "-" :
        print(number1 - number2)
    elif operator == "/" :
        print(number1 / number2)
    elif operator == "*" :
        print(number1 * number2)
    else:
        print("invalid operator")
# problem 3
def max_of_three(a, b, c):
    #Enter code here
    if c > a and c > b :
        print(c)  
    elif b > a and b > c :
        print(b)
    elif a > b and a > c :
        print(a) 
    else:
        print("invalid input")