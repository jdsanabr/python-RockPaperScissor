import random

"""
It's time to play some rock paper scissors! Need I say more?

Though this is a simple program, the primary purpose of this is for me to continue familiarizing
myself with Python syntax.
"""


# list of actions available to both players in this game
listOfActions = ["r", "p", "s"]

# this will count the total number of rounds
round = 1

# this will count the number of rounds the user is winning so far
userVictories = 0

# this will count the number of rounds the CPU is winning so far
cpuVictories = 0


print("Welcome! Let's play some rock, paper, scissors!")

print("Do you want to play a Best of 3 or Best of 5?")

numOfRounds = int(input("Type '3' for Best of 3 or '5' for Best of 5: "))

print("Type 'r' for rock, 'p' for paper, and 's' for scissors. Let's begin!")


while round <= numOfRounds:
    userChoice = input("Rock paper scissors GO! ")
    cpuChoice = random.choice(listOfActions)
    print("I choose", cpuChoice)

    if userChoice == cpuChoice:
        print("Draw. No one gets the point.")
        print("Score is: User ", userVictories, " - CPU ", cpuVictories)

    # scenarios where user wins
    # r > s, p > r, s > p
    elif (userChoice == "r" and cpuChoice == "s") or \
            (userChoice == "p" and cpuChoice == "r") or \
            (userChoice == "s" and cpuChoice == "p"):
        round += 1
        print("Point goes to you.")
        userVictories += 1
        print("Score is: User ", userVictories, " - CPU ", cpuVictories)
    else:
        print("Point goes to me.")
        cpuVictories += 1
        print("Score is: User ", userVictories, " - CPU ", cpuVictories)
        round += 1

print("Game set! The final score: User ", userVictories, " - CPU ", cpuVictories)
