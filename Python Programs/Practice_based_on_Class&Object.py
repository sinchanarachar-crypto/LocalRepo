#Create a class 'Student' that takes name and marks of 3 subjects as arguements in constructor. Use methods to find average of marks

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi!",self.name,"\nYour average score is ",sum/3)

a=input("Enter name of Student: ")
mark=[]
i=0
for i in range(3):
    mark.append(int(input("Enter marks: ")))

S1=Student(a,mark)
S1.get_avg()