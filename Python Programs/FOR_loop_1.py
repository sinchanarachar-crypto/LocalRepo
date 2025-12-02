L=[]
print(type(L))
n=int(input("Enter total number of Elements: "))
i=1
while (i<=n):
    e=input("Enter the Element: ")
    L.append(e)
    i+=1
    if i>n:
        break

print(L)

x=input("Enter search Element:")

for j in L:
    if j==x:
        print(x,"is found",L.index(j),"position")
        break        #ends at first index and doesn't print the next index if element is repeated
    else:
        print(x,"not found")