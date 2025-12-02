#RANGE
seq = range(10)

for i in seq:
    print(i)  # prints from 0 10 9

print(seq)  #output: range(0,10)

print("END")

for i in range(5):   #range(stop)
    print(i)      #prints 0 to 4

print("END")

for i in range(2,10):   #range(start,stop)
    print(i)      #prints 2 to 9

print("END")

for i in range(2,10,2):   #range(start,stop,step)
    print(i)      #prints 2 to 8, increasing 2 in every step

print("END")


#PASS in FOE loop
for i in range(10):
    pass
print("NO WORK IS DESCRIBED IN THE FOR LOOP")