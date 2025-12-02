#type conversions

#conversion(automatic)
a=2
b=7.12
sum=a+b #answer will be 9.12 and 2 will be converted to 2.0 while calculating
print(sum)

#casting(manual)
a,b=1,2   #"2" is consisderd as a string, adding string to integer is not possible
c = int(b)  #Manual conversion of b into int
sum2 = a+c
print(sum2)


