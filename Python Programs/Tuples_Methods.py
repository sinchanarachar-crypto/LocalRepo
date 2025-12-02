tup=(2,1,3,1)
print(tup.index(1))    #returns index of first occurance        # but how to find second repetition index
print(tup.count(1))    #returns how many times a value is repeated

lst = [2, 2, 4, 5]

for i in lst:
    print(lst.index(i), end = " ")  #this gives output index of 2 as 0 for both 2's



"""
L=[3,2,1,2,0]
lst=[]
for i in L:
    if i in lst:
        print(L.index(i),len(lst),end="")      This is to find second index in tuple
        lst.appen(i)
    if i not in lst;
        lst.append(i)
print(lst)
"""
    