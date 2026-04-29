# def dup(n):
#     result =[]
#     temp=[]
#     count = 0                   #
#     max = 0                    #
#     for el in n:          #   #
#         if el not in temp: # #
#             temp.append(el) #
#         else: 
#             if el not in result:
#                 result.append(el)
#     print(result)
# dup([1,4,2,7,4,1,8,2,2])   

# def rev_str(sent):
#     result = ""
#     word = ""                                                   
#     for ch in sent:         
#         if ch != " ":       
#             word = ch + word        
#         else:                 
#             result += word + " "
#             word = ""               
#     result += word   
#     print(result)
# rev_str("i love python")

# def str_(ani):                            #
#     result=[]                            #
#     for i in range(len(ani)):       #   #
#         if ani[i-1][0] == ani[i][0]: # #
#             result.append(ani[i])     #
#     print(result)
# str_(["cat", "cow", "dog", "door", "doll", "fish"])

# def small_big(n):                     #
#     count = 0                        #
#     for i in range(0,len(n),+2):#   #
#         if n[i+1] > n[i]:        # # 
#             count+=1              #
#     print(count)
# small_big([1, 5, 2, 6, 3, 9])

# def rev_list(n):
#     rev_list=[]                       #
#     for i in range(-1,len(n)-1): #   #
#         rev_list.append(n[i])     # # 
#     print(rev_list)                #
# rev_list([1,2,3,4,5])

# def grt_avg(n):
#     sum=0
#     avg=0
#     count=0
#     for i in n:
#         sum+=i
#     avg =len(n)/sum
#     for i in n:
#         if i > avg:
#             count +=1
#     print(count)
# grt_avg([4, 8, 1, 9, 3, 10, 5])

# def rev_even(x):
#     result = ""
#     for i in range(len(x)-1,-1,-1):
#         if i % 2 ==0:
#             result += x[i]
#     print(result)
# rev_even("python")