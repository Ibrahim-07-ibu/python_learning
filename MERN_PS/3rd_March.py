def duplicate(x):
    new_x=[]
    for i in x:
        if i not in new_x:
            new_x.append(i)
    print(new_x)
duplicate([2,3,2,4,4,5,6,7,8,9,9,1])
def matrix(a,b):
    for i in range(len(a)):
        list = []
        for j in range(len(a[0])):
            list.append(a[i][j]+b[i][j])
        print(list)

matrix( [[1, 2, 3],[4, 5, 6]],[[7, 8, 9],[1, 0, 1]])