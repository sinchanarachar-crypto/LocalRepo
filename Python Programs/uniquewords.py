data = input("Enter the Sentence: \n")
new_data = data.split()

dict = dict()


for word in new_data:
    if word  in dict:
        dict[word] += 1

    if word not in dict:
        dict[word] = 1
        

print(dict)