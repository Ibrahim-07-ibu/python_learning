# # 1

# def removing_el(nums,k):
#     result = []
#     x = len(nums) - k
#     if k > len(nums):
#         print("Invalid input")
#     else:
#         for i in range(0,x,+1):
#             result.append(nums[i])
#         print(result)
# removing_el( [10, 20, 30, 40, 50],2)


# # 2

# def finding_max_odd(x,y):
#     count_x = 0
#     count_y = 0
#     for i in x:
#         if i % 2 != 0:
#             count_x += 1
#     for i in y :
#         if i % 2 != 0:
#             count_y += 1
#     if count_x > count_y:
#         print(x)
#     elif count_x < count_y:
#         print(y)
#     else:
#         print("Odd counts are equal")

# finding_max_odd([1, 2, 3, 4, 5, 6, 7], [11, 22, 33, 44, 55])

# #3

# def finding_the_prev_div_numb(numb):
#     result=[]
#     for i in range(len(numb)):
#         prev_numb = i - 1 
#         if prev_numb>0:
#             if numb[i] % prev_numb == 0:
#                 result.append(numb[i])
#     print(result)

# finding_the_prev_div_numb( [1, 2, 3, 6, 7])
--------------------------------------------------------------
#1


# Write a Python program to find all the pairs of numbers whose sum is equal to a given target value,
# but you cannot use nested loops.
# Example:
# numbers = [2, 4, 3, 5, 7, 8, -1]
# target = 7
# Expected Output:
# Pairs with sum 7 are: [(2, 5), (4, 3), (8, -1)]

#2


# Write a function that compresses a string using counts of repeated characters.
#  If the compressed string is not shorter, return the original string.
# Example Input:

# text = "aaabbccccd"
# Output:

# a3b2c4d1