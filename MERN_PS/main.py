def unique(x):
    result =""
    for i in range(0,len(x)):
        if x[i] not in result:
            result += x[i]
        else:
            return "not Unique"
    return "unique"
print(unique("ibrahm"))