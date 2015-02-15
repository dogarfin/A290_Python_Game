#! /usr/bin/env python3
import random

numbers = list(x for x in range (1,26))
currentPosition = 0
moves = 0
def printBoard():
    numbers.reverse()
    for i in range (0,len(numbers)):
        if ((i % 5) == 0):
            print ("\n" + "-----------------------") 
        if (i == 24-currentPosition):
            print("X" + " | ", end="")
        else:
            print(str(numbers[i]) + " | ", end="")
    print ("\n" + "----------------------- \n") 
    numbers.reverse()
    print("\nScore at this point is: %d \n" % moves)
def FandB():
    for i in range(0,len(numbers)):
        val = numbers[i-1]
        if (i == 1 or i == 10 or i == 20):
            numbers[i-1] = "FB"
        elif (i == 7 or i == 17 or i == 23):
            numbers[i-1] = "BP"
def main():
    global numbers
    global currentPosition
    global moves
    run = input("Please enter r to roll or e to quit: ")
    moves += 1
    FandB()
    while (currentPosition < 24):
        while (run != "r" and run != "e"):
            run = input("Not valid input. Please enter r to run or e to exit: ")
        if (run == "r"):
            roll = random.randint(1,6)
            print("\nYou rolled a %d!" % roll)
            currentPosition = currentPosition + roll
            print("You moved to spot %d!" % (currentPosition + 1))
            if (currentPosition == 1-1):
                print("\nYou hit FB!! :-) \nSent to spot 7 on the board!! :-)")
                currentPosition = 7 - 1
            elif (currentPosition == 10-1):
                print("\nYou hit FB!! :-) \nSent to spot 17 on the board!! :-)")
                currentPosition = 17 - 1
            elif (currentPosition == 20-1):
                print("\nYou hit FB!! :-) \nSent to spot 23 on the board!! :-)")
                currentPosition = 23 - 1
            elif (currentPosition == 7-1):
                print("\nYou hit BP!! :-( \nSent to spot 1 on the board!! :-(")
                currentPosition = 1 - 1
            elif (currentPosition == 17-1):
                print("\nYou hit BP!! :-( \nSent to spot 10 on the board!! :-(")
                currentPosition = 10 - 1
            elif (currentPosition == 23-1):
                print("\nYou hit BP!! :-( \nSent to spot 20 on the board!! :-(")
                currentPosition = 20 - 1
            printBoard()
            if (currentPosition >= 18):
                while (currentPosition >= 18):
                    run = input("Please enter r to roll or e to exit: ")
                    moves += 1
                    if (run == "e"):
                        break
                    else:
                        roll = random.randint(1,6)
                        print("\nYou rolled a %d!" % roll)
                        ifRoll = currentPosition + roll
                        if (ifRoll == 24):
                            currentPosition = ifRoll
                            printBoard()
                            print("You Win!! \n:-)\n:-)\n\nFinal Score: %d!!!!\n" % moves)
                            break
                        elif (ifRoll > 24):
                            printBoard()
                            print("You have to input the exact right number to end the game\n")
                        else:
                            currentPosition = ifRoll
                            if(numbers[currentPosition] == "BP"):
                                print("\nYou hit BP!! :-( \nSent to spot 20 on the board!! :-(")
                                currentPosition = 20-1
                            printBoard()
            elif (currentPosition == 24):
                break
            else:
                run = input("Please enter r to roll or e to exit: ")
                moves += 1
        else:
            break

main()


