print("The Guessing Game")
import random
number=random.randint(1,20)
guess=0
counter=0
while guess!=number and guess!="exit":
    guess=input("Please guess a number between 1 and 20: ")
    if guess == "exit":
        break
    guess = int(guess)
    counter=counter+1
    if guess < number:
        print("Thats too low!")
    elif guess > number:
        print("Thats too high!")
    else:
        print("Thats right the number was",number,"and it only took you",counter,"guesses!")

input()
