# def remove_dup(numb):
#     result = []
#     for i in range(0,len(numb),+1):
#         if numb[i] not in result::
#             result.appened(numb[i])
#     print(result)

# def sec_highest(numb):
#     first = -99999
#     second = -99999
#     for i in numb:
#         if i > first:
#             second = first
#             first = i
#         elif i > second and i != first:
#             second = i 
#     print(second)
# sec_highest([4,9,1,3,7])

# def rev_list(numb):
#     result=[]
#     for i in range(len(numb)-1,-1,-1):
#         result.append(numb[i])
#     print(result)
# rev_list([4,1,6,9])

# def letter(a):
#     # count = 0
#     b = ""
#     for i in a:
#         count = 0
#         if i not in b:
#             for j in a:
#                 if i == j:
#                     count +=1
#                     b +=i
#             print(i,count)
# letter("success")

# def chars(a):
#     count = 0
#     b = []
#     for i in a:
#         if i == 0:
#             count +=1
#         elif count == 1:
#             b.append(i)
#     print(b)
# chars([1,2,0,9,8,7,0])

# You are given a list of integers and a target number.
#   Your task is to identify two different elements in the list whose sum equals the target.
#   Return the indices of those two elements.

# ```python
# Input:
# # nums = [2, 7, 11, 15]
# # target = 9
# Output:
# # [0,1]

# Input:
# # nums = [3,2,4], target = 6
# Output:
# # [1,2]
# ```



# - Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# ```python
# Input: nums = [1,2,3,1]
# Output: True

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: True

# Input:  nums = [1,2,3,4]
# Output: False