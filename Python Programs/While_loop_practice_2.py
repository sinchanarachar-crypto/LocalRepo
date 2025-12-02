#Program to insert elements to tuple and find a particular element
tup=()
x=int(input("Enter total number of elements: "))
y=1
while y<=x:
    e=(input("Enter a element: "))       #inserting elements to tuple manually
    tup=tup+(e,)
    y+=1
print(tup)

f=input("Enter the element which is to be found: ")

# if (f in tup):
#         print("Element found in",tup.index(f),"place")
# else:
#         print("Element not found")


# for j in range(len(tup)):
    
#     if tup[j]==f:
#                                                 #use "for" loop for looping using iterable
#         print("Value found at",j)

#     if f not in tup:
#         print("Not Found")
        
#     else:
#         print("not found")

while True:
        if f not in tup:
                print("value not found")
                break
        if f in tup:
                for j in range(len(tup)):
                        if tup[ j ] == f:
                                print("value found at", j)