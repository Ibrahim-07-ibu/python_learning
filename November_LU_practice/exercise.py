# def end_in_ing(words):
#     result = []
#     for i in range(len(words)):
#         if words[i][-3] == "i" and words[i][-2] == "n" and words[i][-1] == "g":
#             result.append(words[i])
#     print(result)
# end_in_ing(["playing", "run", "walking", "see", "coding"])

# def mid_vowel_first_last_consonant(words):
#     result = ""
#     vowel="aeiouAEIOU"
#     for i in range(len(words)):
#         if len(words[i]) %2 != 0:
#             if  words[i][0] not in vowel and words[i][-1] not in vowel:
#                 mid = len(words) / 2
#                 if mid == 0 and  mid[i] in vowel:
#                     result = words[i]
#                 print(words[i])
# mid_vowel_first_last_consonant(["cat", "idea", "apple", "road", "pep", "axis"])

# def find_indices(arr, target):
#     indices = []
#     for i in range(len(arr)):
#         if arr[i] == target:
#             indices.append(i)
#     return indices


# print(find_indices([1, 2, 3, 2, 4, 2],2))


# def top_vowel_students(students, scores):
#     vowels = "AEIOUaeiou"
#     total = 0
#     for score in scores:
#         total += score
#     avg = total / len(scores)
#     result = []
#     for i in range(len(students)):
#         name = students[i]
#         count = 0
#         for ch in name:
#             if ch in vowels:
#                 count += 1
#         if count >= 3 and scores[i] > avg:
#             result.append(name)
#     print(result)


# top_vowel_students(
#     ["Aravind", "Bala", "Eeshwar", "Louis", "Gita"], [85, 70, 92, 88, 60]
# )


