def checking_the_first_el(words):
    result = ""
    for el in words:
        if el[0] in el.upper():
            result += el
    print(result)

checking_the_first_el(["apple", "ball", "Cat", "Dog"])

def checking_the_len_even(nums):
    result = []
    for el in nums:
        if el >= 1000 and el <=9999 and el % 2 == 0:
            result.append(el)
    print(result)
checking_the_len_even([1234,3423,12421,4431,3151,22])

def collect_lowercase(words):
    result = ""
    for l in words:
        if l != l.upper():
            result = result + l
    print(result)
collect_lowercase("TYCEUvufvUTDydRDiyrDITdoU")


def find_the_float(nums):
    result = []
    for i in nums:
        if type(i) == float:
            result.append(i)
    print(result)


find_the_float([10, 3.5, "hello", 8.2, 6])
