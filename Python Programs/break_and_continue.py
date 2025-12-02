i=0
while i<=5:
    print(i)
    i+=1
    if i==3:   #prints only 0,1,2
        break
print ("End")

j=0
while (j<=5):
    if (j==3):  
        j+=1 #prints 0,1,2,4,5
        continue
    print(j)
    j+=1
print ("End")