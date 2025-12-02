#To input in a List and perform works using function defination

lst=[]

n=int(input("Enter length of the List: "))

#def in_lst():
i=0
while (i<n):
    e=input("Enter the Element: ")
    lst.append(e)
    i+=1
    if i>=n:
        break

def pr_lst(list):
    for ele in list:
        print(ele,end=" ")

#in_lst(lst)
pr_lst(lst)