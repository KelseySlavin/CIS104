import random

def RollNumber():
    return random.randint (1,7)

Roll = True

while(Roll):

    RandNumber = RollNumber()

    print("You rolled a: "+  str(RandNumber))

    KeepRolling = input("Would you like to roll again? yes or no?: ")

    if not(KeepRolling.upper() == "YES"):
        Roll=False

print("Thank you for playing")
