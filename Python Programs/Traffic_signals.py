light = input("Light: ").lower()

if(light=="Red".lower()):
    print("STOP")

elif(light=="Yellow".lower()):
    print("Look Around")

elif(light=="Green".lower()):
    print("GO")
    
else:
    print("Invalid Input")