# Dice Roller
import random
import time

exit = ''
while exit.lower() != 'q':
    exit = input("1. Roll Dice(y)\n2. Exit(q)\n")
    roll = random.randrange(1,6)
    for i in range(3):
        print("...")
        time.sleep(1)
    print("You rolled a " + str(roll) + "\n")
    time.sleep(2)


        
    