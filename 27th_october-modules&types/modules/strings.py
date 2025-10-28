import strings


# string
# without importing you can use it 

# lowercase
# uppercase
# sentence -> every word -> capitalize 
# sentence -> beginning word -> capitalize

# within a given sentence,
# lowercase -> upper case, upper case -> lower case

# capitalize
content = "hello world"
print(content.capitalize())

left = "level"
right = "LEVEL"
# uppper case full conversion 
print(right.casefold())

city = "JohanNESburg"
# lowercase -> uppper case 
# uppercase -> lowercase

print(city.swapcase())

proverb ="practice makes a man perfect"

print(proverb.upper())
print(proverb.capitalize())
print(proverb.title())