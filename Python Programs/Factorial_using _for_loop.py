#TO FIND THE FACTORIAL OF A GIVEN NUMBER

n=int(input("Enter a number: "))

f=1
for i in range(1,n+1):
    f=f*(i)
    i+=1

print("Factorial:",f)

