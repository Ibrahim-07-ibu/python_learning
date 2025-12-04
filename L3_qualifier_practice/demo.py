# Remove consecutive duplicate characters

# Given a string, remove only the consecutive duplicates.

# Input:  "aaabbcdddda"
# Output: "abcda"

def removing_duplicate(words):
    result = ""
    for i in words:
        if i not in words:
            result += i
    print(result)



def repeated_el(numb):
    most_num = numb[0]
    most_count = 0

    for i in range(len(numb)):
        count = 0
        for j in range(len(numb)):
            if numb[i] == numb[j]:
                count += 1
        
        if count > most_count or (count == most_count and numb[i] > most_num):
            most_count = count
            most_num = numb[i]
    
    print(most_num)


repeated_el([4, 1, 2, 4, 3, 4, 2, 2])



