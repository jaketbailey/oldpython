
#Imports time, sys and random so they can be used
import time
import sys
import random

#Sets the positions as 1
player1pos = 1
player2pos = 1

#Generates the 3 snakes and 2 ladders as random numbers between 4 and 49
snake1 = random.randint(11,15)
snake2 = random.randint(26,30)
snake3 = random.randint(42,48)
ladder1 = random.randint(5,10)
ladder2 = random.randint(16,25)

#Greets the user to the game
print("Welcome to Snakes and Ladders by Jake Bailey!!")

time.sleep(0.5)
#Tells the user that the game is beginning
print("Lets Play!!")

play = "yes"

time.sleep(0.5)
#Asks the user to input the name of player1
p1 = input("Input player one: ")
time.sleep(0.5)
#Asks the user to input the name of player2
p2 = input("Input player two: ")

#If play is equal to yes the board will be printed so the user sees the layout
if play == "yes":
    print("")
    print("[43][44][45][46][47][48][49]")
    time.sleep(0.2)
    print("[42][41][40][39][38][37][36]")
    time.sleep(0.2)
    print("[29][30][31][32][33][34][35]")
    time.sleep(0.2)
    print("[28][27][26][25][24][23][22]")
    time.sleep(0.2)
    print("[15][16][17][18][19][20][21]")
    time.sleep(0.2)
    print("[14][13][12][11][10][09][08]")
    time.sleep(0.2)
    print("[01][02][03][04][05][06][07]")
    print("")
    time.sleep(0.5)
    print("And the snakes are at positions", snake1, ",", snake2, "and", snake3 )
    time.sleep(0.5)
    print("And the ladders are at positions", ladder1,"and", ladder2)

    back1 = 5
    back2 = 13
    back3 = 20
    for1= 23
    for2 = 7


#While play is equal to yes the game will continue
while play == "yes":
    time.sleep(0.5)
    #Sets roll as an input variable and tells the user to press enter to roll the dice
    roll = input("Press 'ENTER' to roll the dice for player 1")
    #Rolls the two dice
    p1roll = random.randint(1,6)
    p1roll2 = random.randint(1,6)

    #If dice 1 is equal to dice 2 it will say that a double has been rolled
    if p1roll == p1roll2:
        time.sleep(0.5)
        print("You rolled two", p1roll, "'s!!")
        time.sleep(0.5)
        print("So you have rolled a double!!")
        #Adds the two dice and sets it as backmove
        backmove = p1roll + p1roll2
        #Sets player position as itself minus backmove
        player1pos = player1pos - backmove
        #if player1's position is less than or equal to 1 it will set player1's position as 1
        if player1pos <= 1:
            player1pos = 1

        #If not player1's position remains the same
        else:
            #If player position equals one of the snake positions then it will take away the necessary amount of spaces
            if player1pos == snake1:
                print("You landed on a snake!!")
                player1pos = player1pos - back1

            elif player1pos == snake2:
                print("You landed on a snake!!")
                player1pos = player1pos - back2

            elif player1pos == snake3:
                print("You landed on a snake!!")
                player1pos = player1pos - back3

            #If player position equals one of the ladder positions then it will add the necessary amount of spaces
            elif player1pos == ladder1:
                print("You landed on a ladder!!")
                player1pos = player1pos + for1

            elif player1pos == ladder2:
                print("You landed on a ladder!!")
                player1pos = player1pos + for2

    #If dice 1 is not equal to dice 2 it will tell the user a double hasn't been rolled
    if p1roll != p1roll2:
        time.sleep(0.5)
        print("You have rolled a", p1roll, "and a", p1roll2, "!!")
        time.sleep(0.5)
        print("A double has not been rolled!!")
        #Makes the variable formove as dice 1 + dice 2
        formove = p1roll + p1roll2
        #Sets player1's position as itself + formove
        player1pos = player1pos + formove

        #If player position equals one of the snake positions then it will take away the necessary amount of spaces
        if (player1pos == snake1):
            print("You landed on a snake!!")
            player1pos = player1pos - back1

        elif player1pos == snake2:
            print("You landed on a snake!!")
            player1pos = player1pos - back2

        elif player1pos == snake3:
            print("You landed on a snake!!")
            player1pos = player1pos - back3

        #If player position equals one of the ladder positions then it will add the necessary amount of spaces
        elif player1pos == ladder1:
            print("You landed on a ladder!!")
            player1pos = player1pos + for1

        elif player1pos == ladder2:
            print("You landed on a ladder!!")
            player1pos = player1pos + for2

    #if player1's position is greater than or equal to 49 it will tell the user that player 2 has one go to make it a draw otherwise player 1 wins
    if player1pos >= 49:
        time.sleep(0.5)
        print(p1, "has reached the end of the board, they will win if", p2, "can't get there in their next turn, lets give them a chance!!")

    time.sleep(0.5)
    #Tells the user player1's position on the board
    print(p1, "is now at number", player1pos, "on the board.")

    time.sleep(0.5)
    #Sets roll2 as an input variable and tells the user to press enter to roll the dice
    roll2 = input("Press 'ENTER' to roll the dice for player 2")
    # Rolls the two dice
    p2roll = random.randint(1,6)
    p2roll2 = random.randint(1,6)

    #If dice 1 is equal to dice 2 it will say that a double has been rolled
    if p2roll == p2roll2:
        time.sleep(0.5)
        print("You have rolled two", p2roll, "'s!!")
        time.sleep(0.5)
        print("You have rolled a double!!")
        #Adds the two dice and sets it as backmove
        backmove = p2roll + p2roll2
        #Sets player position as itself minus backmove
        player2pos = player2pos - backmove
        #if player2's position is less than or equal to 1 it will set player2's position as 1
        if player2pos <= 1:
            player2pos = 1

        #If not player2's position remains the same
        else:
            #If player position equals one of the snake positions then it will take away the necessary amount of spaces
            if (player2pos == snake1):
                print("You landed on a snake!!")
                player2pos = player2pos - back1

            elif player2pos == snake2:
                print("You landed on a snake!!")
                player2pos = player2pos - back2

            elif player2pos == snake3:
                print("You landed on a snake!!")
                player2pos = player2pos - back3

            #If player position equals one of the ladder positions then it will add the necessary amount of spaces
            elif player2pos == ladder1:
                print("You landed on a ladder!!")
                player2pos = player2pos + for1

            elif player2pos == ladder2:
                print("You landed on a ladder!!")
                player2pos = player2pos + for2

    #If dice 1 is not equal to dice 2 it will tell the user a double hasn't been rolled
    if p2roll != p2roll2:
        print("You have rolled a", p2roll, "and a", p2roll2, "!!")
        time.sleep(0.5)
        print("A double has not been rolled!!")
        #Makes the variable formove as dice 1 + dice 2
        formove = p2roll + p2roll2
        #Sets player2's position as itself + formove
        player2pos = player2pos + formove

        #If player position equals one of the snake positions then it will take away the necessary amount of spaces
        if (player2pos == snake1):
            print("You landed on a snake!!")
            player2pos = player2pos - back1

        elif player2pos == snake2:
            print("You landed on a snake!!")
            player2pos = player2pos - back2

        elif player2pos == snake3:
            print("You landed on a snake!!")
            player2pos = player2pos - back3

        #If player position equals one of the ladder positions then it will add the necessary amount of spaces
        elif player2pos == ladder1:
            print("You landed on a ladder!!")
            player2pos = player2pos + for1

        elif player2pos == ladder2:
            print("You landed on a ladder!!")
            player2pos = player2pos + for2

    time.sleep(0.5)
    #Tells the user where player 2 is on the board
    print(p2, "is now at number", player2pos, "on the board.")

    #If player1's or player2's positions are greater than or equal to 49
    if player1pos or player2pos >= 49:
        # If player1's position is greater than or equal to 49 it will tell the user that player 1 has won the game
        if player1pos >= 49:
            print(p1, "has won the game!!")
            #Play is set to no so the loop ends
            play = "no"

        #If player2's position is greater than or equal to 49 it will tell the user that player 2 has won the game
        if player2pos >= 49:
            print(p2, "Has won the game")
            #Play is set to no so the loop ends
            play = "no"

    #if player1's and player2's positions are greater than or equal to 49 the user will be told it's a draw
    if player1pos >= 49 and player2pos >= 49:
        print("It's a draw!!")

#If not the game will end
else:
    sys.exit(1)


