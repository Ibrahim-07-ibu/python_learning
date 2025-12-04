# def merge_two_list(x,y):
#     result = []
#     for i in range(len(x)):
#         result.append(x[i])
#         result.append(y[i])
#     print(result)
# merge_two_list([1, 2, 3],['a', 'b', 'c'])

# def start_end(x):
#     result = []
#     for i in range(len(x)):
#         if  x[i][0] == x[i][-1]:
#             result.append(x[i])
#     print(result)
# start_end(["level", "Apple", "mana", "cool"])

def names_containg_Aa(x):
    result =""
    for i in range(len(x)):
        if "a" in x[i] or "A" in x[i]:
            result = result + " " + x[i]
    print(result)
names_containg_Aa(["Meera", "John", "Kavi", "Sona"])