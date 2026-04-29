def longest_len_word(sentence):
    words =[]
    words = sentence.split()
    max_len = ""
    
    for i in words:
        if len(i) > len(words):
            max_len=i
            break
    print(max_len)
longest_len_word("Data science evolves every year")

def max_vowel(sentence):
    vowel = "aeiouAEIOU"
    count=0
    max=0
    words=sentence.split()
    result=""
    for i in words:
        count =0 
        for el in i:
            if el in vowel:
                count+=1
        if count > max:
            max=count
            result=i
    print(result)
max_vowel("Learning Python is interesting")

def len_more_than_4(sentence):
    words=sentence.split()
    for i in words:
        if len(i) > 4:
            print(i)
    
len_more_than_4("This is a python program")