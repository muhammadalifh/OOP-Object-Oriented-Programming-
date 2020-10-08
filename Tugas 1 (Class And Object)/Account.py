#menggunakan inheritance
#Parent Class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age  = age
        self.gender = gender


    def show_details(self):
        print("\n")
        print("====Personal Details====")
        print("Name   :", self.name)
        print("Age    :", self.age)
        print("Gender :", self.gender)
        return ""
    
        
       
    
#Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def Getcredit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated : £", self.balance)

    def Getdebit(self,amount):
        self.amount = amount
        if (self.amount > self.balance):
            print("Insufficient Funds | Balance Available : £", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated : £", self.balance)
    
    def Getbalance(self):
        print("Account balance: £", self.balance)

    def details(self):
        self.show_details()

    def Errorhandler(self):
        return "Invalid Choice"

User1 = Bank (str(input('Input Your Name    : ')),
               int(input('Input Your Age     : ')),
                str(input('Input Your Gender  : ')))

print("\n")

User2 = Bank (str(input('Input Your Name    : ')),
               int(input('Input Your Age     : ')),
                str(input('Input Your Gender  : ')))


print(User1.show_details())

print('''

        1. CHECK FOR DETAILS

''')
i = int(input("Enter Your choice : " ))

operations1 = {
    "1": User1.Getcredit(2500000), #Baris ini adalah untuk mengganti input credit
    "2": User1.Getdebit(421442), #Baris ini adalah untuk mengganti input debit
    "3": User1.Getbalance(),
    "4": User1.show_details()
}

operations1.get(i, User1.Errorhandler())



print(User2.show_details())

print('''

        2. CHECK FOR DETAILS

''')
i = int(input("Enter Your choice : " ))

operations2 = {
    "1": User2.Getcredit(1500000), #Baris ini adalah untuk mengganti input credit
    "2": User2.Getdebit(1500000), #Baris ini adalah untuk mengganti input debit
    "3": User2.Getbalance(),
    "4": User2.show_details()
}

operations2.get(i, User2.Errorhandler())

   