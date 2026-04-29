# # Bubble Sort 
# for i in range(len(x)):
#     for j in range(i+1, len(x)):
#         if x[i] > x[j]:
#             x[i], x[j] = x[j], x[i]
# print(x)
# # Selection Sort
# def selection_sort(x):
#     for i in range(len(x)):
#         min_index=i
#         for j in range(i+1,len(x)):
#             if x[j] < x[min_index]:
#                 min_index=j
#         # x[i],x[min_index] = x[min_index] , x[i]
#         temp = x[i]
#         x[i]=x[min_index]
#         x[min_index]=temp
#     print(x)
# selection_sort(x)

# x = [10,45,97,26,77,77,34,12,5,2]
# x.sort()
# def binarySearch(x, n):
#     l = 0
#     r = len(x) - 1

#     while l <= r:
#         m = (l + r) // 2

#         if x[m] == n:
#             return m
        
#         elif x[m] < n:
#             l = m + 1
#         else:
#             r = m - 1

#     return -1

# print(binarySearch(x, 34))

# def linera_search(x, t):
#     n = len(x)
#     for i in range(0, n):
#         if (x[i] == t):
#             return i
#     return -1
# print(linera_search(x,34))