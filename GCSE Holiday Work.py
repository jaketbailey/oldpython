
import time
import sys
import random

print("Welcome to the guess my random number game!")
time.sleep(0.5)
print("The rules are quite simple: ")
time.sleep(0.5)
print("You have 10 lives, this means you have 10 guesses to get my number at the start and throughout the levels the amount of lives decreases")
time.sleep(0.5)
print("If you succeed and guess my number within those guesses then you will move to the next level")
time.sleep(0.5)
print("If not.. then you have lost the game")
time.sleep(0.5)
print("Every one you get right you move onto the next, harder level in which the maximum level is 5")
time.sleep(0.5)
print("And if you reach level 5 and guess the number correct then you will win the game")
time.sleep(0.5)
print("And you're now ready to go")
time.sleep(0.5)
print("So lets begin")

name = input("So.. player, please enter your name: ")

f = open("game.txt","a")
f.close()

f = open("game.txt", "a")

f.write("The User's name is: ")
f.write(name + "\n")
f.write("")

f.close()

def openfile():
    f = open("game.txt", "a")
    f.write("The user reached level ")
    f.write(str(level))
    f.write("\n And they finished on ")
    f.write(str(lives))
    f.write(" lives." + "\n\n")
    f.close()

num1 = random.randint(0,20)

level = 1

while level < 6:
    lives = 10

    time.sleep(1)
    print("Hello", name, "Welcome to level 1!")
    time.sleep(1)
    print("In this level you have", lives, "lives to guess my number")
    time.sleep(1)
    print("I'm thinking of a number between 0 and 20, can you guess it?")

    time.sleep(1)
    guess = int(input("Please enter your guess: "))

    while guess != num1:

        lives = lives - 1

        if guess > num1:

            time.sleep(1)
            print("Your guess was wrong so you have", lives, "lives left")
            time.sleep(1)
            print("However your guess is greater than my number")
            time.sleep(1)
            guess = int(input("Please enter your guess: "))

            if lives == 0:
                time.sleep(1)
                print("You've now lost the game, thank you for playing!")
                openfile()
                sys.exit(1)

            else:
                continue

        elif guess < num1:

            time.sleep(1)
            print("Your guess was wrong so you have", lives, "lives left")
            time.sleep(1)
            print("However your guess is less than my number")
            time.sleep(1)
            guess = int(input("Please enter your guess: "))

            if lives == 0:
                time.sleep(1)
                print("You've now lost the game, thank you for playing!")
                openfile()
                sys.exit(1)

            else:
                continue

    if guess == num1:

        if 0 <= lives < 11:

            level = level + 1
            time.sleep(1)
            print("Well done!!")
            time.sleep(1)
            print("You've guessed my number!!")
            time.sleep(1)
            print("You'll now move onto level", level, "well done!!")

        else:
            time.sleep(1)
            print("You guessed the number, but you took too many guesses so you've lost, sorry")
            openfile()


    lives = 9

    time.sleep(1)
    print("Hello", name, "Welcome to level 2!")
    time.sleep(1)
    print("In this level you have", lives, "lives to guess my number")
    time.sleep(1)
    print("I'm thinking of a number between 10 and 40, can you guess it?")

    num1 = random.randint(10, 40)

    time.sleep(1)
    guess = int(input("Please enter your guess: "))

    while guess != num1:

        lives = lives - 1

        if guess > num1:

            time.sleep(1)
            print("Your guess was wrong so you have", lives, "lives left")
            time.sleep(1)
            print("However your guess is greater than my number")
            time.sleep(1)
            guess = int(input("Please enter your guess: "))

            if lives == 0:
                time.sleep(1)
                print("You've now lost the game, thank you for playing!")
                openfile()
                sys.exit(1)

            else:
                continue

        elif guess < num1:

            time.sleep(1)
            print("Your guess was wrong so you have", lives, "lives left")
            time.sleep(1)
            print("However your guess is less than my number")
            time.sleep(1)
            guess = int(input("Please enter your guess: "))

            if lives == 0:
                time.sleep(1)
                print("You've now lost the game, thank you for playing!")
                openfile()
                sys.exit(1)

            else:
                continue

    if guess == num1:

        if 0 <= lives < 11:

            level = level + 1

            time.sleep(1)
            print("Well done!!")
            time.sleep(1)
            print("You've guessed my number!!")
            time.sleep(1)
            print("You'll now move onto level", level, "well done!!")

        else:
            time.sleep(1)
            print("You guessed the number, but you took too many guesses so you've lost, sorry")
            openfile()

    lives = 8

    time.sleep(1)
    print("Hello", name, "Welcome to level 3!")
    time.sleep(1)
    print("In this level you have", lives, "lives to guess my number")
    time.sleep(1)
    print("I'm thinking of a number between 30 and 60, can you guess it?")

    num1 = random.randint(30, 60)

    while guess != num1:

        lives = lives - 1

        if guess > num1:

            time.sleep(1)
            print("Your guess was wrong so you have", lives, "lives left")
            time.sleep(1)
            print("However your guess is greater than my number")
            time.sleep(1)
            guess = int(input("Please enter your guess: "))

            if lives == 0:
                time.sleep(1)
                print("You've now lost the game, thank you for playing!")
                openfile()
                sys.exit(1)

            else:
                continue

        elif guess < num1:

            time.sleep(1)
            print("Your guess was wrong so you have", lives, "lives left")
            time.sleep(1)
            print("However your guess is less than my number")
            time.sleep(1)
            guess = int(input("Please enter your guess: "))

            if lives == 0:
                time.sleep(1)
                print("You've now lost the game, thank you for playing!")
                openfile()

                sys.exit(1)


            else:
                continue

    if guess == num1:

        if 0 <= lives < 11:

            level = level + 1

            time.sleep(1)
            print("Well done!!")
            time.sleep(1)
            print("You've guessed my number!!")
            time.sleep(1)
            print("You'll now move onto level", level, "well done!!")

        else:
            time.sleep(1)
            print("You guessed the number, but you took too many guesses so you've lost, sorry")
            openfile()

    time.sleep(1)
    guess = int(input("Please enter your guess: "))

    lives = 7

    time.sleep(1)
    print("Hello", name, "Welcome to level 4!")
    time.sleep(1)
    print("In this level you have", lives, "lives to guess my number")
    time.sleep(1)
    print("I'm thinking of a number between 40 and 80, can you guess it?")

    num1 = random.randint(40, 80)

    time.sleep(1)
    guess = int(input("Please enter your guess: "))

    while guess > num1 or guess < num1:

        lives = lives - 1

        if guess > num1:

            time.sleep(1)
            print("Your guess was wrong so you have", lives, "lives left")
            time.sleep(1)
            print("However your guess is greater than my number")
            time.sleep(1)
            guess = int(input("Please enter your guess: "))

            if lives == 0:
                time.sleep(1)
                print("You've now lost the game, thank you for playing!")
                openfile()
                sys.exit(1)

            else:
                continue

        elif guess < num1:

            time.sleep(1)
            print("Your guess was wrong so you have", lives, "lives left")
            time.sleep(1)
            print("However your guess is less than my number")
            time.sleep(1)
            guess = int(input("Please enter your guess: "))

            if lives == 0:
                time.sleep(1)
                print("You've now lost the game, thank you for playing!")
                openfile()
                sys.exit(1)

            else:
                continue

    else:

        if 0 <= lives < 11:

            level = level + 1

            time.sleep(1)
            print("Well done!!")
            time.sleep(1)
            print("You've guessed my number!!")
            time.sleep(1)
            print("You'll now move onto level", level, "well done!!")

        else:
            time.sleep(1)
            print("You guessed the number, but you took too many guesses so you've lost, sorry")
            openfile()

    time.sleep(1)
    guess = int(input("Please enter your guess: "))

    lives = 6

    time.sleep(1)
    print("Hello", name, "Welcome to level 5!")
    time.sleep(1)
    print("In this level you have", lives, "lives to guess my number")
    time.sleep(1)
    print("I'm thinking of a number between 50 and 100, can you guess it?")

    num1 = random.randint(50, 100)

    time.sleep(1)
    guess = int(input("Please enter your guess: "))

    while guess != num1:

        lives = lives - 1

        if guess > num1:

            time.sleep(1)
            print("Your guess was wrong so you have", lives, "lives left")
            time.sleep(1)
            print("However your guess is greater than my number")
            time.sleep(1)
            guess = int(input("Please enter your guess: "))

            if lives == 0:
                time.sleep(1)
                print("You've now lost the game, thank you for playing!")
                openfile()
                sys.exit(1)

            else:
                continue

        elif guess < num1:

            time.sleep(1)
            print("Your guess was wrong so you have", lives, "lives left")
            time.sleep(1)
            print("However your guess is less than my number")
            time.sleep(1)
            guess = int(input("Please enter your guess: "))

            if lives == 0:
                time.sleep(1)
                print("You've now lost the game, thank you for playing!")
                openfile()
                sys.exit(1)

            else:
                continue

    else:

        if 0 <= lives < 11:

            level = level + 1

            time.sleep(1)
            print("Well done!!")
            time.sleep(1)
            print("You've guessed my number!!")
            time.sleep(1)
            print("You'll now move onto level", level, "well done!!")

        else:
            time.sleep(1)
            print("You guessed the number, but you took too many guesses so you've lost, sorry")
            openfile()

else:
    time.sleep(1)
    print("You've won the game!!")
    time.sleep(1)
    print("Congratulations!!")
    time.sleep(1)
    print("Thank you for playing the game!!")
    openfile()
    sys.exit(1)