# # 1
# def first_last(x):
#     print(x[0], x[-1])


# first_last("python")


# # 2
# def count_vowel(x):
#     vowel = "aeioe"
#     count = 0
#     for i in range(len(x)):
#         if x[i] in vowel:
#             count += 1
#     print(count)


# count_vowel("python")


# # 3
# def count_word(x):
#     count = 1
#     for i in range(len(x)):
#         if x[i] == " ":
#             count += 1
#     print(count)


# count_word("Python is fun")


# # 4
# def replace_letter(x):
#     result = ""
#     vowel = "aeiou"
#     for i in range(len(x)):
#         if x[i] in vowel:
#             result += "-"
#         else:
#             result += x[i]
#     print(result)


# replace_letter("banana")


# # 5
# def remove_vowel(x):
#     vowel = "aeiou"
#     result = ""
#     for i in range(len(x)):
#         if x[i] not in vowel:
#             result += x[i]
#     print(result)


# remove_vowel("education")


# # 6
# def drop_numbs(x):
#     result = ""
#     num = "1234578960"
#     for i in range(len(x)):
#         if x[i] not in num:
#             result += x[i]
#     print(result)


# drop_numbs("He12llo, Py00th55on")


# # 7
# def rev_str(sent):
#     result = ""
#     word = ""
#     for ch in sent:
#         if ch != " ":
#             word = ch + word
#         else:
#             result += word + " "
#             word = ""
#     result += word
#     print(result)


# rev_str("abc def")


# # 8
# def count_letter(x, y):
#     count = 0
#     for i in range(len(x)):
#         if x[i] == y:
#             count += 1
#     print(count)


# count_letter("mississipi", "s")
# # 9
# def plalindorm(x):
#     new=""
#     for i in range(len(x)):
#         new=x[i]+new
#     if new==x:
#         print("yes")
#     else:
#         print("No")
# plalindorm("level")

# # 10
# def difference_from_average(input_list):
#     total = 0
#     new = []

#     for i in range(len(input_list)):
#         total = total + input_list[i]

#     avg = total / len(input_list)

#     for i in input_list:
#         a = i - avg
#         new.append(a)

#     print(new)
# difference_from_average([10, 20, 30])

# #11
# def square_list(input_list):
#     res = []

#     for i in input_list:
#         new = i ** 2
#         res.append(new)

#     print(res)


# square_list([2, 3, 4, 5])
# # 12
# def count_occurrences(input_list, target):
#     count = 0

#     for i in range(len(input_list)):
#         if input_list[i] == target:
#             count = count + 1

#     print(count)


# count_occurrences([3, 4, 3, 8, 4, 9], 3)
# # 13
# def replace_negatives(input_list):
#     new = []

#     for i in range(len(input_list)):
#         if input_list[i] < 0:
#             new.append(0)
#         else:
#             new.append(input_list[i])

#     print(new)


# replace_negatives([5, -3, 9, -8, 2])

# # 14
# def count_greater_than_50(input_list):
#     count = 0

#     for i in range(len(input_list)):
#         if input_list[i] > 50:
#             count = count + 1

#     print(count)


# count_greater_than_50([20, 60, 75, 45, 90, 35])
# # 15
# def sum_first_last(input_list):
#     new = 0

#     for i in range(len(input_list)):
#         new = input_list[0] + input_list[-1]

#     print(new)


# sum_first_last([10, 20, 30, 40, 50])
# #16
# def print_with_index(input_list):
#     for i in range(len(input_list)):
#         print("index", i, "input", input_list[i])


# print_with_index(["apple", "banana", "grapes"])

# # 17
# def sum_odd_even(input_list):
#     even_sum = 0
#     odd_sum = 0

#     for i in range(len(input_list)):
#         if input_list[i] % 2 == 0:
#             even_sum = even_sum + input_list[i]
#         else:
#             odd_sum = odd_sum + input_list[i]

#     print("even_sum:", even_sum, "odd_sum:", odd_sum)


# sum_odd_even([10, 15, 20, 25, 30])
# # 18
# def replace_all_negatives(input_list):
#     new = []

#     for i in range(len(input_list)):
#         if input_list[i] < 0:
#             new.append(0)
#         else:
#             new.append(input_list[i])

#     print(new)


# replace_all_negatives([10, -5, 20, -10, 30])

# 19
# def sub_seq_and_list(x,y):
#     for i in range(len(x) - len(y) + 1):
#         match = True
#         for j in range(len(y)):
#             if x[i + j] != y[j]:
#                 match == False
#                 break
#         if match ==True:
#             print(True)
#             return
#     print(False)
# sub_seq_and_list([1, 5, 8, 3, 7, 9, 3, 7, 9, 2]
# ,	[3, 7, 9]
# )
# 20
# def str_rotate(s_1, s_2):
#     if len(s_1) != len(s_2):
#         return False
#     return s_2 in (s_1 + s_1)

# print(str_rotate("ABCDE", "CDEAB"))
# 21
# def count_passed(marks):
#     count = 0
#     for i in range(len(marks)):
#         if marks[i] >= 40:
#             count +=1
#     print(count)
# count_passed([23,3,2,34,43,7,88,7,8,8,8,87,87,85,])
# 22
# def count_cost(prizes):
#     count = 0
#     for i in range(len(prizes)):
#         if prizes[i] >= 1000:
#             count += 1
#     print(count)
# count_cost([23453453,45,243535,234545,5,3,55,3,4,43435,53535,343223])
# 23
# def print_len_more_than_6(cities):
#     for i in range(len(cities)):
#         if len(cities[i]) >= 6:
#             print(cities[i])
# print_len_more_than_6(["chennai","london","delhi","mumbai","banguluru","pune","Washington DC"])
# 24
# def delete_k(arr,k):
#     result=[]
#     for i in range(0,len(arr)-k):
#         result.append(arr[i])
#     print(result)
# delete_k([10,20,30,40,50],1)
# 25
# def sum_consecutive_pairs(x):
#     sum = 0
#     for i in range(len(x)-1):
#         sum = x[i] + x[i+1] + sum
#     print(sum)
# sum_consecutive_pairs([1,2,3,4,5])
# 26
# def existance_of_k(arr,k):
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] ==k:
#             count+=1
#     print(count)
# existance_of_k([4, 1, 1, 4, 2, 4, 3, 1, 5],4)
# 27
# def missing_numb(x, y):
#     for i in x:
#         if i not in y:
#             return i
# print(missing_numb([10, 20, 30, 40, 50], [40, 10, 20, 50]))
# 28
# def encrypt_sent(sent):
#     words = "qwertyuioplkjhgfdsazxcvbnm"
#     result_sent = ""
#     for i in range(len(sent)):
#         if sent[i] in words:
#             result_sent += sent[i]
#         else:
#             if result_sent != "" and result_sent[-1] != " ":
#                 result_sent += " "
#     return result_sent
# print(encrypt_sent("secret   mission   starts   now"))
# 29
# def recover_message(s):
#     words = s.split()
#     result = ""
#     for i in range(len(words) - 1, -1, -1):
#         result += words[i]
#         if i != 0:
#             result += " "
#     return result
# print(recover_message("iron man is flying"))
# # 29
# def highest_marks(names, maths_marks, physics_marks, chemistry_marks):
#     max_total = -1
#     top_student = ""

#     for i in range(len(names)):
#         if maths_marks[i] > 90 and physics_marks[i] > 90 and chemistry_marks[i] > 90:
#             total = maths_marks[i] + physics_marks[i] + chemistry_marks[i]
#             if total > max_total:
#                 max_total = total
#                 top_student +=names[i]+" "

#     if max_total == -1:
#         print("No student found")
#     else:
#         print(top_student)
# highest_marks(["jason", "priya", "madhan", "syed"], [91, 92, 81, 95], [91, 89, 100, 91], [91, 95, 100, 92])
# highest_marks(["Ameer", "Bobby", "Clara", "Divya", "Elvin", "Fazil", "Geeta", "Hari", "Ila", "Jay"], [85, 88, 89, 90, 86, 87, 84, 83, 89, 88], [84, 87, 88, 89, 85, 86, 83, 82, 88, 87], [86, 85, 84, 83, 87, 88, 82, 81, 85, 86])
# def calculate_ride_cost(t, k):
#     if k < 0:
#         print("Invalid Input")
#         return

#     if t == 'P':
#         rate = 30
#     elif t == 'L':
#         rate = 40
#     elif t == 'O':
#         rate = 20
#     else:
#         print("Invalid Input")
#         return

#     total = k * rate
#     total_cost = total + (total * 0.10)

#     print(int(total_cost))
# calculate_ride_cost('P', 10)