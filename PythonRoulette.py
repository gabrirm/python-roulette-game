


#Python roulette

import random


class Roulette():

    
    
    def __init__(self, name, money):
        self.name = name
        self.balance = float(money)
        

    def __repr__(self):
        return "Greetings Mr.{}, You will be playing the french roulette. This is your current balance: {} Good luck!".format(self.name, self.money, self.balance)

    numbers = []
    for i in range(1, 37):
        numbers.append(i)
    

    def bet(self, betType, numbers = [], betprice = []):
        red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
        even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
        zero = 0
        
        #where the roulette ball lands
        bet = []
        bet.append(random.randint(0, 36))
        
        if betType == "red" and bet in red == True:
            self.balance += betprice[0] * 2
        else:
            self.balance -= betprice[0]
            print("Oh, the ball landed on a black number :(. This is your current balance: ".format(self.balance))

        if betType == "black" and bet in black == True:
            self.balance += betprice[0] * 2
        else:
            self.balance -= betprice[0]
            print("Oh, the ball landed on a red number :(. This is your current balance: ".format(self.balance))

        if betType == "numbers":
            if numbers[0] in bet:
                self.balance += betprice[0] * 36
            else:
                self.balance -= betprice[0]
            if numbers[1] in bet:
                self.balance += betprice[1] * 36
            else:
                self.balance -= betprice[1]
            if numbers[2] in bet:
                self.balance += betprice[2] * 36
            else:
                self.balance -= betprice[2]
            if numbers[3] in bet:
                self.balance += betprice[3] * 36
            else:
                self.balance -= betprice[3]
            if numbers[4] in bet:
                self.balance += betprice[4] * 36
            else:
                self.balance -= betprice[4]
            if numbers[5] in bet:
                self.balance += betprice[5] * 36
            else:
                self.balance -= betprice[5]
            if numbers[6] in bet:
                self.balance += betprice[6] * 36
            else:
                self.balance -= betprice[6]
            if numbers[7] in bet:
                self.balance += betprice[7] * 36
            else:
                self.balance -= betprice[7]
            
            
            print("After the spin, this is your remaining balance: {}".format(self.balance))

player_name = str(input("Hi! Welcome to the french roulette! Please type your name: "))
player_balance = float(input("Introduce the money you would like to play with, please: "))
player_bet_type = str(input("There are 3 types of bets at this casino: you can guess if the ball will land on a red number, a black number, or you can bet on a series of numbers(8). Please type 'red'/'black'/'numbers': "))
player = Roulette(player_name, player_balance)
player_numbers = []

player_bet_on_numbers = []

player_price_on_bet = []

if player_bet_type == 'red' or player_bet_type == 'black':
    player_price_on_bet.append(float(input("Now select the quantity of money you would like to bet: ")))

else:
    print("Now select the 8 numbers you would like to play with: ")
    for i in range(1, 9):
        player_numbers.append(int(input()))

if player_bet_type == 'numbers':
    print("Now select the price of the bet for EACH number: ")
    for i in range(1, 9):
        player_price_on_bet.append(float(input()))



choice = input("Would you like to spin the wheel? If so, Good luck! Please, type 'yes' or 'no': ")


while choice == 'yes' and player.balance > 0:
    print("The roulette is spinning!")
    player.bet(player_bet_type, player_numbers, player_price_on_bet)
    choice = input("Would you like to play again? Please type 'yes' or no': ")
    player_bet_type = input("Please type 'red', 'black' or 'numbers': ")
    if player_bet_type == 'red' or player_bet_type == 'black':
        player_price_on_bet.append(float(input("Now select the quantity of money you would like to bet: ")))
    else:
        print("Now select the 8 numbers you would like to play with: ")
    for i in range(1, 9):
        player_numbers.append(int(input()))

    if player_bet_type == 'numbers':
        player_price_on_bet.append(float(input("Now select the price of the bet for EACH number: ")))
    
    if player_balance <= 0:
        print("You ran out of money! :( Thanks for playing!")
        break
else:
    print("Thanks for playing! This is your final balance: {}".format(player_balance))










          

           

            


            

