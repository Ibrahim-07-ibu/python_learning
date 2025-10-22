# 1. Write a function to split a given string on hyphens (-) and display each substring on a new line.

sentence = "Emma-is-a-data-scientist"
substrings = sentence.split('-')
for word in substrings:
    print(word)

# 2. Write a Python program to reverse a given string in two ways:
str1 = "Python"
reversed_str = ""
for char in str1:
    reversed_str = char + reversed_str
print(reversed_str)

# 3.  Write a Python program to count the number of consonants in a given string.
string = "Hello World"
count = 0

for char in string:
    if (char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and
        char != 'A' and char != 'E' and char != 'I' and char != 'O' and char != 'U' and
        char != ' '):
        count += 1

print(count)

# 4. Write a Python program to remove all spaces from a given string.
string = "Python is awesome"
result = ""

for char in string:
    if char != " ":
        result += char

print(result)

# 5. Write a Python program that asks the user to enter a password and checks if it is strong. A password is considered strong if:

password = input("Enter your password:")
for char in password:
    if char == '!' or char == '@' or char == '#' or char == '$' or \
       char == '%' or char == '^' or char == '&' or char == '*' or char == '/':
        print("Password is strong")
        break
else:
    print("Password is not strong")

