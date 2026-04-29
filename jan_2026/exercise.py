a=12544

count=0
while a > 0:
    a //= 10
    count+=1
print(count)

S = input("programming")
K = input("gramm")


S = "programming"
K = "gramm"

if K in S:
    result = S.replace(K, "", 1)
    print(result)
else:
    print(S)

