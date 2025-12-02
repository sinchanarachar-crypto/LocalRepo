#Program to print squares of given starting number to ending number continuously
s=int(input("Enter starting number: "))
i=s
e=int(input("Enter ending number: "))
while i<=e:
    print(i*i)
    i+=1
print("End")
