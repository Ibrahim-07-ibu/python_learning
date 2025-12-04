# Level 3:

# Find the smallest word in a sentence.
# Input: "Python is super powerful"
# Output: is

# def small_wrd(sentence):
#     words = sentence.split()

#     smallest = words[0]

#     for i in words:
#         if len(i) < len(smallest):
#             smallest = i
    
#     return smallest

        
# print(small_wrd("Python is super powerful"))

# A list is strictly increasing if every next element is greater than the previous one.
# Example:
# [1,3,5,9] → True

# def inc_numb(nums):
#     result = True
#     for i in range(1, len(nums)):
#         if nums[i] < nums[i-1]:
#             result = False
#             break
#     print(result)

# inc_numb([5, 2, 2])


# Reverse characters only at even index positions Indices: 0,2,4,6,...
# Input: "abcdefg" Even positioned letters: a, c, e, g → reverse → g, e, c, a
# Final Output: "gbecdfa"

# x = "abcdefg"
# even = ""
# odd = ""

# for i in range(len(x)):
#     if i % 2 == 0:
#         even = x[i] + even      
#     else:
#         odd = odd + x[i]        

# res = ""
# e = 0
# o = 0

# for i in range(len(x)):
#     if i % 2 == 0:
#         res += even[e]
#         e += 1
#     else:
#         res += odd[o]
#         o += 1

# print(res)

# Replace characters at odd indexes with *.
# Example: "hello" → "h*l*o" 

# x = "hello"
# res = ""

# for i in range(len(x)):
#     if i % 2 == 1:
#         res += "*"
#     else:
#         res += x[i]

# print(res)