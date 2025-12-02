dict = {
    "Name":"Sinchana R ",  #"key":"value" is the syntax
    "CGPA" : 9.8,       #key and value can be of int and float datatype also
    "Subjects" : ["Python","Mathematics","Physics","Chemistry","Electronics"],   #Lists and tuples can be stored
    "Year":2025,
}
dict["Surname"]= "Achar"  #adding new key and value 
print(dict)      #if I write dict["name"]=SHINCHAN, it overwrites the previous one, SHINCHAN will be displayed
print(type(dict))  #type is printed as dictionary
print(dict["CGPA"])  #prints cgpa only (value only)

#null_dict={}  creates null dictionary, later we can add the information