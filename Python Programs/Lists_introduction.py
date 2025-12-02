#List is same as string, but the thing is that, it contains different datatypes
marks=[100,99,98,95]
print(marks)  #prints all things inside the list named marks
print(type(marks))  #prints that marks is a list type
print(marks[0])  #prints the value of 1st datatype stored in the list
print(len(marks)) #prints the length of the list

"""Strings are immutable while lists are mutable;i.e.,
index value can be accessed but can't be changed in string but both can be done in lists"""

student=["Sinchana", 18, "AIML","RVCE"]
print(student[0])
student[0]="Shinchan"
print(student[0])