class Employee:
    #class variable
   
   def __init__(self, firstName, lastName, salary):
       #instance variable
       self.__first = firstName
       self.__last = lastName
       self.__salary = salary
       self.__bonus = self.__salary * 1.1 
    
   def Getfirstname(self):
       return self.__first 

   def  Getlastname(self):
       return self.__last   

   def Bonussalary(self):
       if (self.__salary >= 0):
           return self.__bonus 

   def getSalary(self):
       if (self.__salary >= 0):
           return self.__salary

Employee1 = Employee(str(input('First name Employee1 : '))
                    ,str(input('Last name Employee1 : '))
                    ,float(input('Input Salary : ')))
print("\n")
Employee2 = Employee(str(input('First name Employee2 : '))
                    ,str(input('Last name Employee : '))
                    ,float(input('Input Salary : ')))


print("\n")
print('Employee1 first name : ', Employee1.Getfirstname())
print('Employee1 last name  : ', Employee1.Getlastname())
print('Employee1 salary     : $', Employee1.getSalary())
print('\n')

print('Employee2 first name : ', Employee2.Getfirstname())
print('Employee2 last name  : ', Employee2.Getlastname())
print('Employee2 salary     : $', Employee2.getSalary())
print('\n')

print('After 10% Raise')
print('Employee1 salary     : $', Employee1.Bonussalary())
print('Employee2 salary     : $', Employee2.Bonussalary())
print('\n')

