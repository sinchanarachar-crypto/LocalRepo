student={
    "Name":"Sinchana",
    "Class":"12th",
    "Score":{                   #nesting dictionary
        "Mathematics":100,
        "Physics":97,
        "Chemistry":99,
    }
    
}

print(len(list(student.keys())))  #prints length main dictionary keys       even len(student) works
print(student.keys())  #prints main dictionary keys
print(student.values())  #prints main dictionary values
print(student.items())  #prints main dictionary all (key,value) pairs as tuples
print(student.keys())  #prints main dictionary keys
print(student.get("Score"))  #prints the key according to value
student.update({"College":"KJS"}) #Adds new key and value into existing dictionary
print(student)

pairs=list(student.items())    #converting dictionay into list for accessing(it's not required , but a knowledge)
print(pairs[0])   #prints 1st key and it's value



