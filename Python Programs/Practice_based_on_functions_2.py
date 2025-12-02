#Conversion of currency between USD and INR

def into_USD():
    r=float(input("Enter value of Rupees: "))
    u=r/88.75
    print("Value in Dollars=",u)

def into_INR():
    u=float(input("Enter value of Dollars: "))
    r=u*88.75
    print("Value in Rupees=",r)

c=int(input("Enter your choice\n1.Rupees into Dollars\n2.Dollars into Rupees\n3.Exit\n"))

if c==1:
    into_USD()
    
elif c==2:
    into_INR()

elif c==3:
    print("Exiting...\nTHANK YOU")

else:
    print("INVALID INPUT")