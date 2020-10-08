class Invoice :
    #class varibale

    def __init__(self, partnumber, description, quantity, price):
        self.__partnumber = partnumber
        self.__description = description
        self.__quantity = quantity
        self.__price = price
        self.__invoiceammount = self.__quantity * self.__price


    def Getpartnumber(self):
        return self.__partnumber

    def Getdescription(self):
        return self.__description

    def Getquantity(self):
        if(self.__quantity == 0 or self.__quantity <= 0):
            print("Please enter your quantity correctly")
        return self.__quantity

    def Getprice(self):
        if(self.__quantity == 0 or self.__quantity <= 0):
            print("Please enter your price correctly")
        return self.__price


    def Getinvoiceammount(self):
        if(self.__invoiceammount == 0 or self.__invoiceammount < 0):
            print("ERROR")
        else :
            return self.__invoiceammount



Invoice1 = Invoice(input('Input part number : ')
                    ,str(input('Input Description : '))
                    ,int(input('Input Quantity : '))
                    ,int(input('Input Price : ')))
print("\n")
Invoice2 = Invoice(input('Input part number : ')
                    ,str(input('Input Description : '))
                    ,int(input('Input Quantity : '))
                    ,int(input('Input Price : ')))                    
print("\n")
print("==============YOUR ORDER(1)==============")
print('Your part number     : ', Invoice1.Getpartnumber())
print('Your description     : ', Invoice1.Getdescription())
print('Your quantity        : ', Invoice1.Getquantity())
print('Your price           : ', Invoice1.Getprice())
print('Your invoice amount  : $', Invoice1.Getinvoiceammount())
print('\n')

print("\n")
print("==============YOUR ORDER(2)==============")
print('Your part number     : ', Invoice2.Getpartnumber())
print('Your description     : ', Invoice2.Getdescription())
print('Your quantity        : ', Invoice2.Getquantity())
print('Your price           : ', Invoice2.Getprice())
print('Your invoice amount  : $', Invoice2.Getinvoiceammount())
print('\n')
