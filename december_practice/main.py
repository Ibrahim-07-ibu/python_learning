# # 1. Write a function that takes an integer n and prints the first n terms of the following sequence:
# # 10, 20, 30, 40, 50, …
# # Sample Inputs & Outputs
# # Sample Input 1
# # n = 1
# # Output
# # 10
# # Sample Input 2
# # n = 3
# # Output
# # 10 20 30

# def print_terms(n):
#     result=0
#     for i in range(0,n):
#         result+=10
#         print(result)
# print_terms(3)
        

# # 2. Write a function that takes an integer n and prints the first n terms of the following sequence:
# # 5, 10, 15, 20, 25, …
# # Sample Inputs & Outputs
# # Sample Input 1
# # n = 1
# # Output
# # 5
# # Sample Input 2
# # n = 4
# # Output
# # 5 10 15 20
# def print_terms(n):
#     result=0
#     for i in range(0,n):
#         result+=5
#         print(result)
# print_terms(3)

# def print_terms(n):
#     result=0
#     for i in range(0,n):
#         result+=2
#         print(result)
# print_terms(3)

# def three_terms(nums,n):
#     count = 0
#     new_1=new_2=[]
#     for i in range(len(nums)):
#         new_1=nums[0:n]
#         new_2=nums[n:n+3]
#     for el in new_1:

#     print(new_1,new_2)
# three_terms([12,132,332,1241,424,1231,2313,113,24,23],3)

# x = 1200 / 4 
# y= x/10
# print(x+y)

'''1️. A cab service charges ₹50 as a base fare and ₹10 per km for the first 10 km. For every km beyond 10, it charges ₹15 per km.  
Write a program to calculate the total fare for a given distance.  
Test  
calculate_fare(8)  
calculate_fare(12)
2.
A student gets grades based on marks — A if ≥90, B if ≥75, C if ≥60, D if ≥40, else F.  
Write a program that prints the grade for the given marks.  
Test  
find_grade(82)  
find_grade(37)
3. A power company gives discounts based on electricity usage.  
If usage <100 units → no discount,  
100–200 units → 10% discount,  
>200 units → 20% discount.  
Calculate the total bill after discount if the cost per unit is ₹5.  
Test  
electricity_bill(80)  
electricity_bill(220)
'''

# def fare(distance):
#     base_fare = 50
#     result =0 
#     if distance <= 10:
#         result = base_fare + distance*10
#     elif distance > 10 :
#         result = 
#     print(result)
# fare(8)

# def electricity(unit):
#     if unit <= 100:
#         result = unit * 5
#     elif unit <= 200:
#         result = 100*5 + (unit - 100)*7
#     elif unit <= 300:
#         result = 100*5 + 100*7 + (unit - 200)*10
#     else:
#         result = 100*5 + 100*7 + 100*10 + (unit - 300)*15
#     return result
# print(electricity(453))



# def rev_words(arr):
#     words=""
#     for i in range(len(arr)):
#         if arr[i] != " ":
#             words = words +  arr[i]
#     print(words)
# rev_words("iron man is flying")

# def sep_digit(n):
#     quo = n
#     rem = 0 
#     result = []
#     while quo > 0 :
#         rem = quo % 10
#         result.append
#         quo = quo // 10
#     print(result)
# sep_digit(132)

# x = 1 % 10 
# print(x)
# def func(n):
#     result = []
#     inc = 10
#     while n > 0:
#         digit = n % 10          
#         temp = digit % inc
#         result.append(temp)
#         inc = inc * 10
#         n = n // 10             
#     print(result)

# func(132)

# n = 5738429
# # Even =8,4,2
# # Odd = 5,7,3,9
# # Output:
# #  [8, 4, 2, 5, 7, 3, 9]
# def odd_even(n):
#     evens = []
#     odds = []
#     for i in str(n):
#         if ord(i) % 2 == 0:
#             evens.append(i)
#         else:
#             odds.append(i)
#     return evens + odds
# print(odd_even(5738429))