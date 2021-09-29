
#Imports time
import time
#Imports sys
import sys
#Imports os.path
import os.path

#Waits a second
time.sleep(1)
#Welcomes the user to the program
print("Welcome to the Holiday project program by Jake Thomas Bailey")

#Waits a second
time.sleep(1)
#Tells the user that the program contains a series of individual programs
print("This program contains a series of different programs, these include:")
#Waits a second
time.sleep(1)
#Tells the user the first program is a BMI Calculator
print("A BMI Calculator")
#Waits a second
time.sleep(1)
#Tells the user the second program is a normal Calculator
print("A Calculator")
#Waits a second
time.sleep(1)
#Tells the user the final program is a Guess my number game
print("A Guess my Number Game")

#Waits a second
time.sleep(1)
#Asks the user if they want to use the program
use = input("Would you like to use this program? ")

#While the variable use is equal to 'yes'
while use == "yes":

    #Waits a second
    time.sleep(1)
    #Asks the user which program they want to use
    which = input("Which program would you like to use? ")

    #Defines the subroutine BMI
    def BMI():
        #Welcomes the user to the BMI calculator
        print("Welcome to the BMI calculator!!")
        #Waits a second
        time.sleep(1)

        #Asks the user to input their weight
        w = float(input("Please input your weight: "))
        #Prints a gap
        print("")
        #Waits a second
        time.sleep(1)

        #Asks the user to input their weight
        kgorstone = input("If you input your weight in kilograms type 'yes' if not type 'no': ")
        #Prints a space
        print("")
        #Waits a second
        time.sleep(1)

        #If the variable kgorstone equals 'yes'
        if kgorstone == "yes":
            #The variable w stays the same
            w = w

        #If kgorstone equals 'no'
        elif kgorstone == "no":
            #Waits a second
            time.sleep(1)
            #Asks the user to input the stone value
            stone = int(input("Please input the stone value: "))
            #Prints a space
            print("")
            #Waits a second
            time.sleep(1)
            #Asks the user to input the pounds value
            lb = int(input("Please input the pounds value: "))
            #Prints a space
            print("")

            #Sets the variable stonekg to stone * 6.35029318
            stonekg = stone * 6.35029318
            #Sets the variable lbkg to lb * 0.45359237
            lbkg = lb * 0.45359237

            #Sets the variable kilo to stonekg + lbkg
            kilo = stonekg + lbkg

            #Sets the variable w equal to kilo
            w = kilo

        #Waits a second
        time.sleep(1)
        #Asks the user to input their height
        h = float(input("Please input your height: "))
        #Prints a blank space
        print("")

        #Waits a second
        time.sleep(1)
        #Asks the user to input their height
        metersorfeet = input("If you input your height in meters type 'yes' if not type 'no': ")
        #Prints a blank space
        print("")

        #If the variable metersorfeet is equal to 'yes'
        if metersorfeet == "yes":
            #The variable h stays the same
            h = h

        #If metersorfeet is equal to 'no'
        elif metersorfeet == "no":

            #Waits a second
            time.sleep(1)
            #Asks the user to input the foot value
            feet = int(input("Please enter the foot value: "))
            #Prints a blank space
            print("")
            # Waits a second
            time.sleep(1)
            #Asks the user to input the inch value
            inch = int(input("Please enter the inch value: "))
            #Prints a blank space
            print("")

            #Sets the variable feetm to feet * 0.3
            feetm = feet * 0.3
            #Sets the variable inchm to inch * 0.025
            inchm = inch * 0.025

            #Sets the variable m to feetm + inchm
            m = feetm + inchm

            #Sets the variable h equal to m
            h = m

        #Sets the variable BMI equal to w / (h*h)
        BMI = w / (h * h)

        #If BMI is less than 18.5
        if BMI < 18.5:
            #Waits a second
            time.sleep(1)
            #Tells the user that they're BMI suggests they're underweight and gives them some advice
            print("Your BMI is", BMI,
                  "this means that you're underweight, perhaps try to eat some more food to supply your body with the nutrients it needs and to reduce your risK of anemia and osteoporosis")

        #If the 18.5 is greater than or equal to BMI and BMI is less than 25
        elif 18.5 <= BMI < 25.0:
            #Waits a second
            time.sleep(1)
            #Tells the user that they're BMI suggests they're a normal weight and gives them some advice
            print("Your BMI is", BMI,
                  "this means that you're at a normal, healthy weight, keep eating how you usually do and you should stay at your healthy weight")

        #If 25 is greater than or equal to BMI and BMI is less than 30
        elif 25.0 <= BMI < 30.0:
            #Waits a second
            time.sleep(1)
            # Tells the user that they're BMI suggests they're overweight and gives them some advice
            print("Your BMI is", BMI,
                  "this means that you're overweight and you should start to eat less food to reduce the risk of heart problems")

        #If 30 is greater than or equal to BMI
        elif 30.0 <= BMI:
            #Waits a second
            time.sleep(1)
            # Tells the user that they're BMI suggests they're obese and gives them some advice
            print("Your BMI is", BMI,
                  "this means that you're obese and you should start to eat less for to reduce the risk of heart problems")
            #Prints a blank space
            print("")

        #Waits a second
        time.sleep(1)
        #Thanks the user for using the BMI calculator
        print("Thank you for using this BMI calculator")

        #Asks the user what program they want to use next and if not to type 'end'
        which = input("Which program would you like to use next, if not any type 'end' ")

    #Defines the subroutine calc
    def calc():

        #Welcomes the user to the Calculator
        print("Welcome to the Calculator")

        #Asks the user how many numbers they wish to input
        howmany = input(
            "How many numbers to you wish to times, divide, subtract or add? 2 - 4 or do you not want to use this, if so type 'no': ")

        #While the variable howmany is not equal to 'no'
        while howmany != "no":
            #If howmany is equal to '2'
            if howmany == "2":
                #Asks the user if they want to times, divide, add or subtract
                calculation = input("Do you wish to times, divide, add or subtract? ")

                #If the variable calculation is equal to 'times'
                if calculation == "times":

                    #Waits a second
                    time.sleep(1)
                    #Asks the user to input the first number
                    num1 = float(input("Please enter the first number: "))
                    #Waits a second
                    time.sleep(1)
                    #Asks the user to input the second number
                    num2 = float(input("Please enter the second number: "))

                    #Tells the user the answer is being processed
                    print("Your answer is being processed")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)

                    #Sets the variable answer to num1 * num2
                    answer = num1 * num2
                    #Tells the user the answer to their answer and thanks them for using the calculator
                    print("Your answer is", answer, "Thank you for using the calculator.")
                    #Waits for a second
                    time.sleep(1)

                    #Asks the user how many numbers they wish to use in their calculation
                    howmany = input(
                        "How many numbers to you wish to times, divide, subtract or add? 2 - 4 or do you not want to use this, if so type 'no': ")
                    # Waits for a second
                    time.sleep(1)

                #If calculation is equal to 'divide'
                elif calculation == "divide":

                    # Waits for a second
                    time.sleep(1)
                    #Asks the user to input their first number
                    num1 = float(input("Please enter the first number: "))
                    # Waits for a second
                    time.sleep(1)
                    #Asks the user to input their second number
                    num2 = float(input("Please enter the second number: "))

                    #Tells the user their answer is being processed
                    print("Your answer is being processed")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)

                    #Sets the variable answer to num1 / num2
                    answer = num1 / num2

                    #Tells the user their answer and thanks them for using the calculator
                    print("Your answer is", answer, "Thank you for using the calculator.")
                    # Waits for a second
                    time.sleep(1)

                    #Asks how many numbers the user wishes to use in their calculation
                    howmany = input(
                        "How many numbers to you wish to times, divide, subtract or add? 2 - 4 or do you not want to use this, if so type 'no': ")
                    #Waits for a second
                    time.sleep(1)

                #If the variable calculation is equal to 'add'
                elif calculation == "add":

                    # Waits for a second
                    time.sleep(1)
                    #Asks the user to enter their first number
                    num1 = float(input("Please enter the first number: "))
                    # Waits for a second
                    time.sleep(1)
                    #Asks the user to enter their second number
                    num2 = float(input("Please enter the second number: "))

                    #Tells the user answer is being processed
                    print("Your answer is being processed")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    # Waits for half a second
                    time.sleep(0.5)

                    #Sets the variable answer to num1 + num2
                    answer = num1 + num2

                    #Tells the user their answer and thanks them for using the calculator
                    print("Your answer is", answer, "Thank you for using the calculator.")
                    #Waits for a second
                    time.sleep(1)

                    #Asks the user how many numbers they wish to use in the calculation
                    howmany = input(
                        "How many numbers to you wish to times, divide, subtract or add? 2 - 4 or do you not want to use this, if so type 'no': ")
                    #Waits for a second
                    time.sleep(1)

                #If the variable calculation is equal to 'substact'
                elif calculation == "subtract":

                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their first number
                    num1 = float(input("Please enter the first number: "))
                    #Waits for second
                    time.sleep(1)
                    #Asks the user to input their second number
                    num2 = float(input("Please enter the second number: "))

                    #Tells the user the answer is being processed
                    print("Your answer is being processed")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)

                    #Sets the variable answer to num1 - num2
                    answer = num1 - num2

                    #Tells the user the answer and thanks them for using the calculator
                    print("Your answer is", answer, "Thank you for using the calculator.")
                    #Waits for a second
                    time.sleep(1)

                    #Asks the user how many numbers they wish to use in the calculation
                    howmany = input(
                        "How many numbers to you wish to times, divide, subtract or add? 2 - 4 or do you not want to use this, if so type 'no': ")
                    #Waits for a second
                    time.sleep(1)

                #Else
                else:
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user to try again
                    print("Please try again...")
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user is they wish to times, divide, add or subtract
                    calculation = input("Do you wish to times, divide, add or subtract?")

            #If howmany is equal to '3'
            elif howmany == "3":
                #Asks the user if the wish to times, divide, add or subtract
                calculation = input("Do you wish to times, divide, add or subtract? ")

                #If calculation is equal to 'times'
                if calculation == "times":
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their first number
                    num1 = float(input("Please enter the first number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their second number
                    num2 = float(input("Please enter the second number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their third number
                    num3 = float(input("Please enter the third number: "))

                    #Tells the user their answer is being processed
                    print("Your answer is being processed")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)

                    #Sets the variable answer to num1* num2 * num3
                    answer = num1 * num2 * num3

                    #Tells the user their answer and thanks them for using the calculator
                    print("Your answer is", answer, "Thank you for using the calculator.")
                    #Waits for a second
                    time.sleep(1)

                    #Asks the user how many numbers they wish to use in their calculation
                    howmany = input(
                        "How many numbers to you wish to times, divide, subtract or add? 2 - 4 or do you not want to use this, if so type 'no': ")
                    #Waits for a second
                    time.sleep(1)

                #If calculation is equal to divide
                elif calculation == "divide":

                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their first number
                    num1 = float(input("Please enter the first number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their second number
                    num2 = float(input("Please enter the second number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their third number
                    num3 = float(input("Please enter the third number: "))

                    #Tells the user their answer is being processed
                    print("Your answer is being processed")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)

                    #Sets the variable answer to num1 / num2 / num3
                    answer = num1 / num2 / num3

                    #Tells the user their answer and thanks them for using the calculator
                    print("Your answer is", answer, "Thank you for using the calculator.")
                    #Waits for a second
                    time.sleep(1)

                    #Asks the user how many numbers they wish to use in their calculation
                    howmany = input(
                        "How many numbers to you wish to times, divide, subtract or add? 2 - 4 or do you not want to use this, if so type 'no': ")
                    #Waits for a second
                    time.sleep(1)

                #If the variable calculation is equal to 'add'
                elif calculation == "add":

                    #Waits for a second
                    time.sleep(1)
                    #Asks the user for their first number
                    num1 = float(input("Please enter the first number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their second number
                    num2 = float(input("Please enter the second number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their third number
                    num3 = float(input("Please enter the third number: "))

                    #Tells the user their answer is being processed
                    print("Your answer is being processed")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)

                    #Sets the variable answer to num1 + num2 + num3
                    answer = num1 + num2 + num3

                    #Tells the user their answer and thanks them for using the calculator
                    print("Your answer is", answer, "Thank you for using the calculator.")
                    #Waits for a second
                    time.sleep(1)

                    #Asks the user how many numbers they wish to use in their calculation
                    howmany = input(
                        "How many numbers to you wish to times, divide, subtract or add? 2 - 4 or do you not want to use this, if so type 'no': ")
                    #Waits for a second
                    time.sleep(1)

                #If calculation is equal to 'subtract'
                elif calculation == "subtract":
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their first number
                    num1 = float(input("Please enter the first number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their second number
                    num2 = float(input("Please enter the second number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their third number
                    num3 = float(input("Please enter the third number: "))

                    #Tells the user their answer is being processed
                    print("Your answer is being processed")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)

                    #Sets the variable answet to num1 - num2 - num3
                    answer = num1 - num2 - num3

                    #Tells the user their answer and thanks them for using the calculator
                    print("Your answer is", answer, "Thank you for using the calculator.")
                    #Waits for a second
                    time.sleep(1)

                    #Asks the user how many numbers they want to use in their calculation
                    howmany = input(
                        "How many numbers to you wish to times, divide, subtract or add? 2 - 4 or do you not want to use this, if so type 'no': ")
                    #Waits for a second
                    time.sleep(1)

                #Else
                else:
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user to try again
                    print("Please try again...")
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user if they wish to times, divide, add or subtract
                    calculation = input("Do you wish to times, divide, add or subtract?")

            #If howmany is equal to '4'
            elif howmany == "4":
                #Asks the user if they wish to times, divide, add or subtract
                calculation = input("Do you wish to times, divide, add or subtract? ")

                #If calculation is equal to 'times'
                if calculation == "times":
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user to input their first number
                    num1 = float(input("Please enter the first number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user to input their second number
                    num2 = float(input("Please enter the second number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user to input their third number
                    num3 = float(input("Please enter the third number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user to input their fourth number
                    num4 = float(input("Please enter the fourth number: "))

                    #Tells the user their answer is being processed
                    print("Your answer is being processed")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)

                    #Sets answer to num1 * num2 * num3 * num4
                    answer = num1 * num2 * num3 * num4

                    #Tells the user their answer and thanks them for using the calculator
                    print("Your answer is", answer, "Thank you for using the calculator.")
                    #Waits for a second
                    time.sleep(1)

                    #Asks the user how many numbers they wish to use in their calculation
                    howmany = input(
                        "How many numbers to you wish to times, divide, subtract or add? 2 - 4 or do you not want to use this, if so type 'no': ")
                    #Waits for a second
                    time.sleep(1)

                #If calculation is equal to 'divide
                elif calculation == "divide":
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their first number
                    num1 = float(input("Please enter the first number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their second number
                    num2 = float(input("Please enter the second number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their third number
                    num3 = float(input("Please enter the third number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their fourth number
                    num4 = float(input("Please enter the fourth number: "))

                    #Tells the user the answer is being processes
                    print("Your answer is being processed")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)

                    #Sets the variable answer to num1 / num2 / num3 / num4
                    answer = num1 / num2 / num3 / num4

                    #Tells the user their answer and thanks them for using the calculator
                    print("Your answer is", answer, "Thank you for using the calculator.")
                    #Waits for a second
                    time.sleep(1)

                    #Asks the user how many numbers they wish to use in their calculation
                    howmany = input(
                        "How many numbers to you wish to times, divide, subtract or add? 2 - 4 or do you not want to use this, if so type 'no': ")
                    #Waits for a second
                    time.sleep(1)

                #If the variable calculation is equal to 'add'
                elif calculation == "add":
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their first number
                    num1 = float(input("Please enter the first number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their second number
                    num2 = float(input("Please enter the second number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their third number
                    num3 = float(input("Please enter the third number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their fourth number
                    num4 = float(input("Please enter the fourth number: "))

                    #Tells the user the answer is being processed
                    print("Your answer is being processed")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)

                    #Sets the variable answer to num1 + num2 + num3 + num4
                    answer = num1 + num2 + num3 + num4

                    #Tells the user their answer and thanks them for using the calculator
                    print("Your answer is", answer, "Thank you for using the calculator.")
                    #Waits for a second
                    time.sleep(1)

                    #Asks the user how many numbers they wish to use in their calculation
                    howmany = input(
                        "How many numbers to you wish to times, divide, subtract or add? 2 - 4 or do you not want to use this, if so type 'no': ")
                    #Waits for a second
                    time.sleep(1)

                #If calculation is equal to 'subtract'
                elif calculation == "subtract":
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their first number
                    num1 = float(input("Please enter the first number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their second number
                    num2 = float(input("Please enter the second number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their third number
                    num3 = float(input("Please enter the third number: "))
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to input their fourth number
                    num4 = float(input("Please enter the fourth number: "))

                    #Tells the user their answer is being processed
                    print("Your answer is being processed")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)
                    #Prints a dot
                    print(".")
                    #Waits for half a second
                    time.sleep(0.5)

                    #Sets the variable answer to num1 - num2 - num3 - num4
                    answer = num1 - num2 - num3 - num4

                    #Tells the user their answer and thanks them for using the calculator
                    print("Your answer is", answer, "Thank you for using the calculator.")
                    #Waits for a second
                    time.sleep(1)

                    #Asks the user how many numbers they wish to use in their calculation
                    howmany = input(
                        "How many numbers to you wish to times, divide, subtract or add? 2 - 4 or do you not want to use this, if so type 'no': ")
                    #Waits for a second
                    time.sleep(1)

                #Else
                else:
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user to try again
                    print("Please try again...")
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user whether they wish to times, divide, add or subtract
                    calculation = input("Do you wish to times, divide, add or subtract?")

        #Else
        else:
            #Waits for a second
            time.sleep(1)
            #Thanks the user for using the calculator
            print("Thank you for using the calculator")
            #Asks the user if they want to use the program
            use = input("Would you like to use this program? ")

    #Defines the subroutine guessnum
    def guessnum():

        #Imports random
        import random

        #Welcomes the user to the guess my number game
        print("Welcome to the guess my random number game!")
        #Waits for half a second
        time.sleep(0.5)
        #Tells the user the rules are simple
        print("The rules are quite simple: ")
        #Waits for half a secondos
        time.sleep(0.5)
        #Tellse the user that they have 10 lives to begin with and this decreases throughout the levels
        print(
            "You have 10 lives, this means you have 10 guesses to get my number at the start and throughout the levels the amount of lives decreases")
        #Waits for half a second
        time.sleep(0.5)
        #Tells the user that is the number is guessed then the user will move to the next level
        print("If you succeed and guess my number within those guesses then you will move to the next level")
        #Waits for half a second
        time.sleep(0.5)
        #Tells the user that if not, you loose the game
        print("If not.. then you have lost the game")
        #Waits for half a second
        time.sleep(0.5)
        #Tells the user that if you guess the number you move up a level, the max level is 5
        print("Every one you get right you move onto the next, harder level in which the maximum level is 5")
        #Waits for half a second
        time.sleep(0.5)
        #Tells the user that if you guess the number at level 5 you win
        print("And if you reach level 5 and guess the number correct then you will win the game")
        #Waits for half a second
        time.sleep(0.5)
        #Tellse the user they're ready to go
        print("And you're now ready to go")
        #Waits for half a second
        time.sleep(0.5)
        #Tells the user they can begin
        print("So lets begin")

        #Asks the user to enter their name
        name = input("So.. player, please enter your name: ")

        #If the file "game.txt" exists 
        if os.path.exists("game.txt"):
            #Appends the file
            f = open("game.txt", "a")
            #Closes the file
            f.close()

        #Else
        else:
            #Opens the file
            f = open("game.txt", "w")
            #Closes the file
            f.close()

        #Opens the file to append
        f = open("game.txt", "a")

        #Writes 'The User's name is: ' to the file
        f.write("The User's name is: ")
        #Writes the variable name to the file and creates a new line
        f.write(name + "\n")
        #Writes a blank space to the file
        f.write("")

        #Closes the file
        f.close()

        #Defines the subroutine openfile
        def openfile():
            #Opens the file to append
            f = open("game.txt", "a")
            #Writes 'The user reached level ' to the file
            f.write("The user reached level ")
            #Writes the variable level as string to the file
            f.write(str(level))
            #Writes a new line to the file and 'And they finished on '
            f.write("\n And they finished on ")
            #Writes the variable lives as string to the file
            f.write(str(lives))
            #Writes ' lives.' and two new lines to the file
            f.write(" lives." + "\n\n")
            #Closes the file
            f.close()

        #Sets the variable num1 and a random number between 0 and 20
        num1 = random.randint(0, 20)

        #Sets the variable level to 1
        level = 1

        #While level is less than 6
        while level < 6:
            #Sets the variable lives to 10
            lives = 10

            #Waits for second
            time.sleep(1)
            #Welcomes the user to level 1
            print("Hello", name, "Welcome to level 1!")
            #Waits for second
            time.sleep(1)
            #Tellse the user how many lives they have
            print("In this level you have", lives, "lives to guess my number")
            #Waits for second
            time.sleep(1)
            #Tellse the user that the number is being generated
            print("I'm thinking of a number between 0 and 20, can you guess it?")

            #Waits for second
            time.sleep(1)
            #Asks the user to make a guess
            guess = int(input("Please enter your guess: "))

            #While guess is not equal to num1
            while guess != num1:

                #Sets the variable lives to itself - 1
                lives = lives - 1

                #If guess is greater than num1
                if guess > num1:

                    #Waits for second
                    time.sleep(1)
                    #Tells the user that their guess was wrong and how many lives they have left
                    print("Your guess was wrong so you have", lives, "lives left")
                    #Waits for second
                    time.sleep(1)
                    #Tells the user the number they guessed is greater than the number
                    print("However your guess is greater than my number")
                    #Waits for second
                    time.sleep(1)
                    #Asks the user to take a guess
                    guess = int(input("Please enter your guess: "))

                    #If lives equals 0
                    if lives == 0:
                        #Waits for second
                        time.sleep(1)
                        #Tells the user that they've lost the game and thanks them for playing
                        print("You've now lost the game, thank you for playing!")
                        #Calls the subroutine openfile()
                        openfile()
                        #Asks the user if they want to use the program
                        use = input("Would you like to use this program? ")

                    #Else
                    else:
                        #The program continues
                        continue

                #If guess is less than num1
                elif guess < num1:

                    #Waits for second
                    time.sleep(1)
                    #Tells the user that their guess was wrong and how many lives they have
                    print("Your guess was wrong so you have", lives, "lives left")
                    #Waits for second
                    time.sleep(1)
                    #Tells the user their guess is less than the number
                    print("However your guess is less than my number")
                    #Waits for second
                    time.sleep(1)
                    #Tells the user to make a guess
                    guess = int(input("Please enter your guess: "))

                    #If lives equals 0
                    if lives == 0:
                        #Waits for second
                        time.sleep(1)
                        #Tells the user they've lost the game and thanks them for playing
                        print("You've now lost the game, thank you for playing!")
                        #Calls the subrouting openfile()
                        openfile()
                        #Asks the user to make a guess
                        use = input("Would you like to use this program? ")

                    #Else
                    else:
                        #The program continues
                        continue

            #If guess is equal to num1
            if guess == num1:

                #If 0 is less than or equal to lives and lives us less than 11
                if 0 <= lives < 11:
                    #Sets the variable level to itself + 1
                    level = level + 1
                    #Waits for second
                    time.sleep(1)
                    #Tells the user well done
                    print("Well done!!")
                    #Waits for second
                    time.sleep(1)
                    #Tells the user that they've guessed the number
                    print("You've guessed my number!!")
                    #Waits for second
                    time.sleep(1)
                    #Tells the user they will move onto the next level
                    print("You'll now move onto level", level, "well done!!")

                #Else
                else:
                    #Waits for second
                    time.sleep(1)
                    #Tells the user that they guessed the number, but in too many guesses so they have lost
                    print("You guessed the number, but you took too many guesses so you've lost, sorry")
                    #Calls the subroutine openfile()
                    openfile()

            #Sets the variable lives to 9
            lives = 9

            #Waits for second
            time.sleep(1)
            #Welcomes the user to level 2
            print("Hello", name, "Welcome to level 2!")
            #Waits for second
            time.sleep(1)
            #Tells them how many lives they have
            print("In this level you have", lives, "lives to guess my number")
            #Waits for second
            time.sleep(1)
            #Tells the user that the number is being made
            print("I'm thinking of a number between 10 and 40, can you guess it?")

            #Sets the variable num1 to a random number between 10 and 40
            num1 = random.randint(10, 40)

            #Waits for second
            time.sleep(1)
            #Asks the user to make a guess
            guess = int(input("Please enter your guess: "))

            #While guess is not equal to num1
            while guess != num1:

                #Sets the variable lives to itself - 1
                lives = lives - 1

                #If guess is greater than num1
                if guess > num1:

                    #Waits for second
                    time.sleep(1)
                    #Tells the user how many lives they have
                    print("Your guess was wrong so you have", lives, "lives left")
                    #Waits for second
                    time.sleep(1)
                    #Tells the user the guess was greater than the number
                    print("However your guess is greater than my number")
                    #Waits for second
                    time.sleep(1)
                    #Asks the user to make a guess
                    guess = int(input("Please enter your guess: "))

                    #If lives equals 0
                    if lives == 0:
                        #Waits for second
                        time.sleep(1)
                        #Tells the user they've lost the game and thanks them for playing
                        print("You've now lost the game, thank you for playing!")
                        #Calls the subroutine openfile()
                        openfile()
                        #Asks the user if they'd like to use the program
                        use = input("Would you like to use this program? ")

                    #Else
                    else:
                        #The program continues
                        continue

                #If guess is less than num1
                elif guess < num1:

                    #Waits for second
                    time.sleep(1)
                    #Tells the user how many lives they have
                    print("Your guess was wrong so you have", lives, "lives left")
                    #Waits for second
                    time.sleep(1)
                    #Tells the user their guess was less than the number
                    print("However your guess is less than my number")
                    #Waits for second
                    time.sleep(1)
                    #Asks the user to make a guess
                    guess = int(input("Please enter your guess: "))

                    #If lives equals 0
                    if lives == 0:
                        #Waits for second
                        time.sleep(1)
                        #Tells the user they've lost the game and thanks them for playing
                        print("You've now lost the game, thank you for playing!")
                        #Calls the subrouting openfile()
                        openfile()
                        #Asks the user if they'd like to use the program still
                        use = input("Would you like to use this program? ")

                    #Else
                    else:
                        #The program continues
                        continue

            #If guess is equal to num1
            if guess == num1:

                #If 0 is less than or equal to lives and lives is less than 11
                if 0 <= lives < 11:

                    #The variable level is set to itself + 1
                    level = level + 1

                    #Waits for second
                    time.sleep(1)
                    #Tells the user well done
                    print("Well done!!")
                    #Waits for second
                    time.sleep(1)
                    #Tells the user they've guessed the number
                    print("You've guessed my number!!")
                    #Waits for second
                    time.sleep(1)
                    #Tells the user they'll now move onto level 3
                    print("You'll now move onto level", level, "well done!!")

                #Else
                else:
                    #Waits for second
                    time.sleep(1)
                    #Tells the user they guessed the number in too many guesses so they lost
                    print("You guessed the number, but you took too many guesses so you've lost, sorry")
                    #Calls the subroutine openfile()
                    openfile()

            #Sets the variable lives to 8
            lives = 8

            #Waits for second
            time.sleep(1)
            #Welcomes the user to level 3
            print("Hello", name, "Welcome to level 3!")
            #Waits for second
            time.sleep(1)
            #Tells the user how many lives they have
            print("In this level you have", lives, "lives to guess my number")
            #Waits for second
            time.sleep(1)
            #Tells the user the number is being thought of
            print("I'm thinking of a number between 30 and 60, can you guess it?")

            #Sets the variable num1 to a random number between 30 and 60
            num1 = random.randint(30, 60)

            #While guess is not equal to num1
            while guess != num1:

                #Sets the variable to itself - 1
                lives = lives - 1

                #If guess is greater than num1
                if guess > num1:

                    #Waits for second
                    time.sleep(1)
                    #Tells the user how many lives they have
                    print("Your guess was wrong so you have", lives, "lives left")
                    #Waits for second
                    time.sleep(1)
                    #Tells the user that the guess was greater than the number
                    print("However your guess is greater than my number")
                    time.sleep(1)
                    #Tells the user to make a guess
                    guess = int(input("Please enter your guess: "))

                    #If lives equals 0
                    if lives == 0:
                        #Waits for second
                        time.sleep(1)
                        #Tells the user that they've lost the game and thanks them for playing
                        print("You've now lost the game, thank you for playing!")
                        #Calls the subroutine openfile()
                        openfile()
                        #Asks the user if they would like to use this program
                        use = input("Would you like to use this program? ")

                    #Else
                    else:
                        #The program will continue
                        continue

                #If guess is less than num1
                elif guess < num1:

                    #Waits for second
                    time.sleep(1)
                    #Tells the user how many lives they have left
                    print("Your guess was wrong so you have", lives, "lives left")
                    #Waits for second
                    time.sleep(1)
                    #Tells the user that their guess is less than the number
                    print("However your guess is less than my number")
                    #Waits for second
                    time.sleep(1)
                    #Asks the user to make a guess
                    guess = int(input("Please enter your guess: "))

                    #If lives equals 0
                    if lives == 0:
                        #Waits for a second
                        time.sleep(1)
                        #Tells the user they've lost the game and thanks them for playing
                        print("You've now lost the game, thank you for playing!")
                        #Calls the subroutine openfile()
                        openfile()

                        #Asks the user if they would like to use this program
                        use = input("Would you like to use this program? ")

                    #Else
                    else:
                        #The program continues
                        continue

            #If guess equals num1
            if guess == num1:

                #If 0 is less than or equal to lives and lives is less than 1
                if 0 <= lives < 11:

                    #Sets the variable level to itself + 1
                    level = level + 1

                    #Waits for a second
                    time.sleep(1)
                    #Tells the user well done
                    print("Well done!!")
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user they've guessed the number
                    print("You've guessed my number!!")
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user they will move onto level 4
                    print("You'll now move onto level", level, "well done!!")

                #Else
                else:
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user they guessed the number but took too many guesses so they lost
                    print("You guessed the number, but you took too many guesses so you've lost, sorry")
                    #Calls the subroutine openfile()
                    openfile()

            #Waits for a second
            time.sleep(1)
            #Asks the user to enter the guess
            guess = int(input("Please enter your guess: "))

            #Sets the variable lives to 7
            lives = 7

            #Waits for a second
            time.sleep(1)
            #Welcomes the user to level 4
            print("Hello", name, "Welcome to level 4!")
            #Waits for a second
            time.sleep(1)
            #Tells the user how many lives they have
            print("In this level you have", lives, "lives to guess my number")
            #Waits for a second
            time.sleep(1)
            #Tells the user the number is being made
            print("I'm thinking of a number between 40 and 80, can you guess it?")

            #Sets the variable num1 to a random number between 40 and 80
            num1 = random.randint(40, 80)

            #Waits for a second
            time.sleep(1)
            #Asks the user to make a guess
            guess = int(input("Please enter your guess: "))

            #While guess is greater than num1 or guess is less than num1
            while guess > num1 or guess < num1:

                #Sets the variable lives to itself - 1
                lives = lives - 1

                #If guess is greater than num1
                if guess > num1:

                    #Waits for a second
                    time.sleep(1)
                    #Tells the user how many lives they have left
                    print("Your guess was wrong so you have", lives, "lives left")
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user their guess is greater than the number
                    print("However your guess is greater than my number")
                    #Waits for a second
                    time.sleep(1)
                    #Asks to make a guess
                    guess = int(input("Please enter your guess: "))

                    #If lives equals 0
                    if lives == 0:
                        #Waits for a second
                        time.sleep(1)
                        #Tells the user they've lost them and thanks them for playing
                        print("You've now lost the game, thank you for playing!")
                        #Calls the subroutine openfile()
                        openfile()
                        #Asks the user if they'd like to use this program
                        use = input("Would you like to use this program? ")

                    #Else
                    else:
                        #The program continues
                        continue

                #If guess is less than num1
                elif guess < num1:

                    #Waits for a second
                    time.sleep(1)
                    #Tells the user how many lives they have left
                    print("Your guess was wrong so you have", lives, "lives left")
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user the guess is less than the number
                    print("However your guess is less than my number")
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to make a guess
                    guess = int(input("Please enter your guess: "))

                    #If lives equals 0
                    if lives == 0:
                        #Waits for a second
                        time.sleep(1)
                        #Tells the user they've lost the game
                        print("You've now lost the game, thank you for playing!")
                        #Calls the subroutine openfile()
                        openfile()
                        #Asks the user if they'd like to use the program
                        use = input("Would you like to use this program? ")

                    #Else
                    else:
                        #The program continues
                        continue

            #Else
            else:

                #If 0 <= lives <11:
                if 0 <= lives < 11:

                    #The variable level is set to itself + 1
                    level = level + 1

                    #Waits for a second
                    time.sleep(1)
                    #Tells the user well done
                    print("Well done!!")
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user they guessed the number
                    print("You've guessed my number!!")
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user they'll move onto level 5
                    print("You'll now move onto level", level, "well done!!")

                #Else
                else:
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user they guessed the number but took too many guesses so they lost
                    print("You guessed the number, but you took too many guesses so you've lost, sorry")
                    #Calls the subroutine openfile()
                    openfile()

            #Waits for a second
            time.sleep(1)
            #Asks the user to make a guess
            guess = int(input("Please enter your guess: "))

            #Sets s the variable lives to 6
            lives = 6

            #Waits for a second
            time.sleep(1)
            #Welcomes the user to level 5
            print("Hello", name, "Welcome to level 5!")
            #Waits for a second
            time.sleep(1)
            #Tells the user how many lives they have
            print("In this level you have", lives, "lives to guess my number")
            #Waits for a second
            time.sleep(1)
            #Tells the user the number is being made
            print("I'm thinking of a number between 50 and 100, can you guess it?")

            #The variable num1 is set to a random number between 50 and 100
            num1 = random.randint(50, 100)

            #Waits for a second
            time.sleep(1)
            #Asks the user to make a guess
            guess = int(input("Please enter your guess: "))

            #While guess is not equal to num1
            while guess != num1:

                #Sets the variable lives to itself - 1
                lives = lives - 1

                #If guess is greater than num1
                if guess > num1:

                    #Waits for a second
                    time.sleep(1)
                    #Tells the user how many lives they have
                    print("Your guess was wrong so you have", lives, "lives left")
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user their guess if greater than the number
                    print("However your guess is greater than my number")
                    #Waits for a second
                    time.sleep(1)
                    #Asks the user to enter a guess
                    guess = int(input("Please enter your guess: "))

                    #If lives equals 0
                    if lives == 0:
                        #Waits for a second
                        time.sleep(1)
                        #Tells the user they have lost the game and thanks them for playing
                        print("You've now lost the game, thank you for playing!")
                        #Calls the subrouting openfile()
                        openfile()
                        #Asks the user if they want to usethis program
                        use = input("Would you like to use this program? ")

                    #Else
                    else:
                        #The program continues
                        continue

                #If guess is less than num1
                elif guess < num1:

                    #Waits for a second
                    time.sleep(1)
                    #Tells the user how many lives they have
                    print("Your guess was wrong so you have", lives, "lives left")
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user their guess is less than the number
                    print("However your guess is less than my number")
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user to make a guess
                    guess = int(input("Please enter your guess: "))

                    #If lies equals 0
                    if lives == 0:
                        #Waits for a second
                        time.sleep(1)
                        #Tells the user they lost and thanks them for playing
                        print("You've now lost the game, thank you for playing!")
                        #Calls the subroutine openfile()
                        openfile()
                        #Asks the user if they would like to use this program
                        use = input("Would you like to use this program? ")

                    #Else
                    else:
                        #The program will continue
                        continue

            #Else
            else:

                #If 0 is less than or equal to lives and lives is less than 11
                if 0 <= lives < 11:

                    #Sets the variable level to itself + 1
                    level = level + 1

                    #Waits for a second
                    time.sleep(1)
                    #Tells the user well done
                    print("Well done!!")
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user they've guessed the number
                    print("You've guessed my number!!")
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user they won
                    print("You won!!")

                #Else
                else:
                    #Waits for a second
                    time.sleep(1)
                    #Tells the user they guessed the number but took too many guesses so they lost the game
                    print("You guessed the number, but you took too many guesses so you've lost, sorry")
                    #Calls the subroutine openfile()
                    openfile()

        #Else
        else:
            #Waits for a second
            time.sleep(1)
            #Tells the user they've won the game
            print("You've won the game!!")
            #Waits for a second
            time.sleep(1)
            #Tells them congratulations
            print("Congratulations!!")
            #Waits for a second
            time.sleep(1)
            #Thanks the user for playing
            print("Thank you for playing the game!!")
            #Calls the subroutine openfile()
            openfile()
            #Asks the user if they would like to use this program
            use = input("Would you like to use this program? ")

    #If which is equal to 'bmi'
    if which == "bmi":

        #The BMI() subroutine is called
        BMI()

    #If which is equal to 'calculator'
    elif which == "calculator":

        #The calc() subroutine is called
        calc()

    #If which is equal to 'guess my number'
    elif which == "guess my number":

        #The guessnum() subroutine is called
        guessnum()

    #Else
    else:

        #Waits for a second
        time.sleep(1)
        #Asks the user which program they would like to use
        which = input("Which program would you like to use?")

#Else
else:
    #Waits for a second
    time.sleep(1)
    #Thanks the user for using the program
    print("Thank you for using this program, the program will now end.")
    #The program ends
    sys.exit(1)
