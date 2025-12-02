#to find factorial of a number using user defined functions
def Fact(n):
    i=1
    f=1
    while i<=n:
        f=f*i
        i+=1
    return f
    
x=int(input("Enter the number to find it's factorial: "))

print("Factorial: ",Fact(x))