import time
import os
import sys
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ' : $' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count

        if count >= 3:
            total_price *= 0.9

        return round(total_price)

class Food(MenuItem):
    def __init__(self, name, price, calorie_count):
        super().__init__(name, price)
        self.calorie_count = calorie_count
    
    def info(self):
        return self.name + ' : $' + str(self.price) + ' (' + str(self.calorie_count) + 'kkal)'
    
    def calorie_info(self):
        print('kkal: ' + str(self.calorie_count))

class Drink(MenuItem):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume

    def info(self):
        return self.name + ': $' + str(self.price) + ' (' + str(self.volume) + 'mL)'

os.system('cls')

def main():
    print("=============================")
    print("🛕 WELCOME TO JONI'S CAFE 🛕")
    print("=============================")
    buyer = input("Enter the name of the buyer : ")

    time.sleep(1)
    os.system('cls')
    print("===========================")
    print("PLEASE ORDER FOOD AND DRINK")
    print("===========================")
    time.sleep(2.5)
    os.system('cls')
    print ("Buyer's name :", buyer) 

    print("==================================")
    print("          🍽️    FOOD   🍽️      ")
    print("==================================")
    food1 = Food('Hamburger     🍔', 5, 330)
    food2 = Food('Fried Chicken 🍗', 4, 450)
    food3 = Food('Taco Bell     🌮', 2, 250)
    food4 = Food('Pizza         🍕', 3, 120)
    food5 = Food('Donuts        🍩', 2, 200)

    foods = [food1, food2, food3, food4, food5]

    index = 0
    for food in foods:
        print(str(index) + '. ' + food.info())
        index += 1

    print('\n')
    ans = 0
    food_order = int(input('Enter the food number : '))
    
    if food_order > 4:
        ans = str(input("wrong input, do you want to start again? (Y/n) "))
        if ans == 'Y':
            os.system('cls')
            main()
        else:
            print('bye')
            exit()
            
    selected_food = foods[food_order]


    time.sleep(2.5)
    os.system('cls')
    print ("Buyer's name :", buyer) 

    print("==================================")
    print("        🥂    DRINK   🥂      ")
    print("==================================")
    drink1 = Drink('Hot Tea       ☕', 3, 180)
    drink2 = Drink('Hot Coffee    🍵', 2, 350)
    drink3 = Drink('Soft Drink    🍺', 3, 120)
    drink4 = Drink('Red Wine      🍾', 5, 250)
    drink5 = Drink('Coconut Ice   🥥', 6, 320)

    drinks = [drink1, drink2, drink3, drink4, drink5]

    index = 0
    for drink in drinks:
        print(str(index) + '. ' + drink.info())
        index += 1
    
    print('\n')
    ans = 0
    drink_order = int(input('Enter the drink number : '))
    
    if drink_order > 4:
        ans = str(input("wrong input, do you want to start again? (Y/n) "))
        if ans == 'Y':
            os.system('cls')
            main()
        else:
            print('bye')
            exit()
    selected_drink = drinks[drink_order]    

    time.sleep(2)
    os.system('cls')

    order1 = food_order
    order2 = drink_order

    print("You choose the following menu : " + str(order1) + " and " + str(order2))

    if food_order == 0:
        print('Food is Hamburger 🍔')
    elif food_order == 1:
        print('Food is Fried Chicken 🍗')
    elif food_order == 2:
        print('Food is Taco Bell 🌮')
    elif food_order == 3:
        print('Food is Pizza 🍕')
    elif food_order == 4:
        print('Food is Donuts 🍩')
    
    if drink_order == 0:
        print('Drink is Hot Tea ☕')
    elif drink_order == 1:
        print('Drink is Hot Coffee 🍵')
    elif drink_order == 2:
        print('Drink is Soft Drink 🍺')
    elif drink_order == 3:
        print('Drink is Red Wine 🍾')
    elif drink_order == 4:
        print('Drink is Coconut Ice 🥥')

    count = int(input('How many food and drink packages do you want? (10% discount for 3 or more): '))

    result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

    print('Total price is $ ' + str(result))

    Money = int(input("Enter your cash : $ "))

    if Money < result:
        print("Your cash is not enough")
        ans = str(input("Do you want to order again? (Y/n) "))
        if ans == 'Y':
            os.system('cls')
            main()
        else:
            print('bye')
            exit()

    Change_money = int(Money-result)
    print("Change money : $ ", Change_money)

    time.sleep(2)
    os.system('cls')
    print("=============================")
    print("   📃 BUYERS'S RECEIPT 📃   ")
    print("=============================")
    print('')
    print (" Buyer's Name 👤  :",str(buyer))
    print (" Bill         💵  : $ ",str(result))
    print (" Money        💰  : $ ",str(Money))
    print (" Change money 💸  : $ ",str(Change_money))
    
    time.sleep(1)
    message = '''
=============================  
  THANK YOU FOR ORDERING 😁  
=============================  
              '''    
    def typewriter(message):
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
    typewriter(message)


#main loop
main()