"""f=open("Files_demo.txt","r+t")
data=f.read()
print(data)
print(type(data))"""

"""line1=f.readline()
print(line1)      #Once whole file is read, again it can't go back to previous one.
data2=f.read(7)   #It works on pointer concept. Once pointer has passed an element it reads the next element.
print(data2)"""

"""f=open("Files_demo.txt","w")
f.write("This is a new file . It's is altered using 'write' option. ")"""

"""f=open("Files_demo.txt","a")
f.write("\nNow I am adding this sentence by opening the file in 'append' mode.")
f.close()"""

#If you open a file that doesn't exist in 'write' or 'append' mode, automatically new file will be created.

with open("Files_demo.txt","r") as f:
    data=f.read()
    print(data)     # Data present in Files_demo will be printed. Here 'data' is a variable name. 
    