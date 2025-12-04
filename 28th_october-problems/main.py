# #1 
# - Vowel Extractor  
#   Write a program to extract only the vowels from a given word and store them in a list.  
#   Print the list at the end.

def vowel_extractor(word):
    vowels = ('a','e','i','o','u')
    vowels_list = []
    for i in word :
        if i in vowels :
            vowels_list = vowels_list + [i]
    print(vowels_list)

vowel_extractor("education")

# ```python
# Input: word = "education"
# Output: ['e', 'u', 'a', 'i', 'o']
# ```

# #2
# - Find Word with Maximum Vowels
#   Given a list of words, find which word has the highest number of vowels and print that word.

def max_vowel(words):
    vowels = ('a','e','i','o','u')
    max_word = []
    max_count = 0

    for i in words:
        count = 0
        for ch in i:
            if ch in vowels:
                count = count + 1
        if count > max_count:
            max_count = count
            max_word = [i]
    print(max_word)

max_vowel(["cat", "eagle", "umbrella", "sky"])


# ```python
# Input: words = ["cat", "eagle", "umbrella", "sky"]
# Output: umbrella
# ```
# #3
# - Given an array of integers, count how many numbers are even and how many are odd.

def count_numb(numbers):
    odd_count=0
    even_count=0
    for i in numbers:
        if i % 2 == 0:
            even_count += 1
        if i % 2 != 0:
            odd_count += 1
    print(even_count)
    print(odd_count)

count_numb([1, 2, 3, 4, 5, 6, 7])


# ```python
# Example Input: [1, 2, 3, 4, 5, 6, 7]
# Example Output: { even: 3, odd: 4 }
# ```
# #4

# - Given an array of integers and a target element, find the indices of its first and last occurrence.
#   (Bonus point: Try to return the output in a dictionary format)

# ```python
# Example: numbers = [5, 2, 3, 5, 7, 5, 8] key= 5
# Example Output: { firstIndex: 0, lastIndex: 5 }
# ```
# #5

# - Combine Two Lists Alternately
#   Write a Python program to combine two lists by picking elements alternately.
#   (Assume both lists are of the same length.)

# ```python
# Input:
# list1 = [10, 20, 30]
# list2 = [1, 2, 3]
# Output: [10, 1, 20, 2, 30, 3]
# ```