# Count to N!

#   ____   _       _____
#  / ___| | |     |_   _|
# | |     | |       | |
# | |___  | |___    | |
#  \____| |_____|   |_|

# Love CLT
# Discord: https://discord.gg/5bh4cs

# Let's import some modules
import time
import sys

# Counting Function #

# Define function
def Counter():
    # Local variables
    numLoop = 0
    count = 0

    # Ask for users number
    print("\nPlease enter the number you wish to count to:")
    while numLoop == 0:
        userNum = input("")
        try:
            userNum = int(userNum)
            numLoop = 1
            print("\nCounting will commence in 3 seconds!\n")
        except ValueError:
            print("This is not an integer, please enter another number:")
    time.sleep(3)

    # Begin counting
    while count < userNum:
        count = count + 1
        print(count)
        if userNum <= 100:
            time.sleep(0.05) # Looks better
        else:
            time.sleep(0.01) # Counts faster if user picks a number above 100

    # Counting finished
    print("\nWe have reached", userNum)

    # End or restart
    endRes = input("Type Q to exit or enter to count to another number:\n")
    if endRes == "Q" or endRes == "q":
        sys.exit()
    else:
        print("")

# Main program #

# Variables that will be used in main program
go = 1

# Let's introduce users to the program
print("Welcome to 'Count to N' by Cat Like Thief!")
time.sleep(1)
print("Simply enter the number you would like the program to count to and we will count every single number until we "
      "reach the one you requested!")

# Allows for repeating of the program
while go == 1:
    Counter()
