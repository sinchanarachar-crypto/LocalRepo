student={
    "Name":"Sinchana",
    "Class":"12th",
    "Score":{                   #nesting dictionary
        "Mathematics":100,
        "Physics":97,
        "Chemistry":99,
    }
    
}
print(student)
print(student["Score"])  #prints the sub_dictionary
print(student["Score"]["Mathematics"]) #prints value stored in mathematics