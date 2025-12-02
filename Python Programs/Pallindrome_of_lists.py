# list=[]
# a=input("Enter 1st thing: ")
# list.append(a)
# a=input("Enter 2nd thing:")
# list.append(a)                          #How to insert the number of values that I wish
# a=input("Enter 3rd thing:")
# list.append(a)
# list1=list.copy()
# list1.reverse()
# if (list==list1):
#     print("Pallindrome")
# else:
#     print("Not a Pallindrome")

lst = []

b = int(input("Enter an odd number: "))
if b % 2 != 0:

    for i in range(b):
        a = int(input("Enter your number: "))
        lst.append(a)

print(lst)