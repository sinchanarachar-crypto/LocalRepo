#To print numbers from backwards

def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)  #recursion of the function 

x=int(input("Enter a number: "))
show(x)

#To print factorial of a number
def factorial(f):
    if (f==0 or f==1):
        return 1
    else:
        return f*factorial(f-1) #recursion is called
    
y=int(input("Enter a number: "))
print("Factorial of ",y,"=",factorial(y))


#To print sum of n natural numbers

def sum(s):
    if s==0:
        return 0
    if s>0:
        return s+sum(s-1)  #recursion
    
a=int(input("Enter a number: "))
print("Sum of natural numbers upto",a,"=",sum(a))
    
#To print elements of list using recursion

L=[]
i=0
l=int(input("Enter length of list: "))

while i<l:
    e=input("Enter the element : ")
    L.append(e)
    i+=1

def pr_list(list,idx=0):
   
    if idx==len(list):
        return
    print(list[idx])
    pr_list(list,idx+1)

pr_list(L)

