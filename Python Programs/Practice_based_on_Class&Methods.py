class Account:
    def __init__(self,accno,balance):
        self.accno=accno
        self.balance=balance
       
    # Debit Method
    def Debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")

    # Credit Method
    def Credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited")

    #Balance printing
    def get_balance(self):
        print("Current Balance in account is Rs.:",self.balance)
        return self.balance

an=input("Enter Account Number: ")
bl=float(input("Enter Account Balance: "))
Acc1=Account(an,bl)

ch=int(input("Enter the option:\n1.Debit\n2.Credit\n"))
if ch==1:
    amt=float(input("Enter amount debited (in Rs.): "))
    Acc1.Debit(amt)
    Acc1.get_balance()

elif ch==2:
    amt=float(input("Enter amount credited (in Rs.): "))
    Acc1.Credit(amt)
    Acc1.get_balance()

else:
    print("Invalid Option Entry")
