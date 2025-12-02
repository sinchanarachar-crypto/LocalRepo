"""WAP to enter 3 subject marks from the user and store them in dictionary
Start with empty dictionary and add one by one.
Use subject name as key and marks as value"""

score={}

a=input("Enter Subject Name: ")
b=int(input("Enter the marks: "))
score.update({a:b})

a=input("Enter Subject Name: ")
b=int(input("Enter the marks: "))
score.update({a:b})

a=input("Enter Subject Name: ")
b=int(input("Enter the marks: "))
score.update({a:b})


print(score)