#Imports time
import time
#Imports sys
import sys

#Asks the user whether they want to change their password and sets the variable to "change"
change = input("Would you like to change your password? ")

#While the answer to "change" equals 'yes'
while change == "yes":
    #Waits a second
    time.sleep(1)
    #Asks the user to input their password and sets the variable to "password"
    password = input("Input your password: ")
    #If the password length is greater than or equal to 8
    if len(password) >= 8:
        #Waits a second
        time.sleep(1)
        #Tells the user they have 8 characters or more in their password
        print ("Your password has 8 characters or more ✔")
        #If any letter in the password is uppercase
        if any(letter.isupper() for letter in password):
            #Waits a second
            time.sleep(1)
            #Tells the user they have an uppercase letter in the password
            print ("Your password contains an uppercase letter ✔")
        #Else
        else:
            #Waits a second
            time.sleep(1)
            #Tells the user the password doesn't contain a uppercase letter
            print ("Your password contains an uppercase letter ✘")
            #Waits a second
            time.sleep(1)
            #Asks the user to ainput the password with a uppercase letter
            password = input("Input your password with at least 1 uppercase letter: ")
        #If any letter in their password is lowercase
        if any(letter.islower() for letter in password):
            #Waits a second
            time.sleep(1)
            #Tells the user their password has a lowercase letter
            print ("Your password also contains a lowercase letter ✔")
        #Else
        else:
            #Waits a second
            time.sleep(1)
            #Tells the user their password doesn't contain a lowercase letter
            print ("Your password also contains a lowercase letter ✘")
            #Waits a second
            time.sleep(1)
            #Asks the user to input their password with a lowercase letter
            password = input("nput your password with at least 1 lowercase letter: ")

        #Waits a second
        time.sleep(1)
        #Asks the user to confirm their password
        confirmpass = input("Please confirm your password: ")
        #While confirmpass isn't equal to password
        while confirmpass != password:
            #Waits a second
            time.sleep(1)
            #Tells the user that wasn't the same password
            print ("That password was not the same as the password")
            #Waits a second
            time.sleep(1)
            #Asks the user to confirm their password
            confirmpass = input("Please confirm your password: ")
        #Else
        else:
            #Waits a second
            time.sleep(1)
            #Tells the user their password has been changed
            print ("Your password has been changed")
            #Exits program
            sys.exit(10)

    #Elif password length is less than 8
    elif len(password) < 8:
        #Waits a second
        time.sleep(1)
        #Tells the user they have less than 8 characters
        print ("Your password has 8 characters or more ✘")

#Else
else:
    #Exits
    sys.exit(10)
    
