str="SINCHANA R ACHAR"
print(str)           #Here string starts from 1 itself, but memory allocation happens from 0
print(str[0:7])      #prints from 0 t 6
print(str[11:15])    #prints from 11 to 14
print(len(str))      #(count upto which letter we need+1) count gives us the string we need while using slicing
print(str[-12:-2])   #Negative Slicing