#
# ROCK, PAPER, SCISSORS - Iterācija 1
# 
# 1. Spēle prasa ievadīt ciparu no 1 līdz 3 (izmanto input, https://www.w3schools.com/python/python_user_input.asp)
# 2. Dators iedomājas ciparu no 1 līdz 3  (izmanto random, https://www.w3schools.com/python/ref_random_randint.asp)
# 3. Atkarībā no ievadītajiem cipariem un datora, izdrukā paziņojumu par zaudējumu, uzvaru, vai neizšķirtu (izmanto if, else https://www.w3schools.com/python/python_conditions.asp)
#

ROCK = "1"
SCISSOR = "2"
PAPER = "3"

print("Welcome to Rock, Paper, Scissors!")
import random

options = ["1", "2", "3"]

user_choice = input("Choose ROCK = 1, SCISSOR = 2, or PAPER = 3")
computer_choice = random.choice(options)

if user_choice == "1" and computer_choice == "1":

    print("Computer picked 1 - Rock, It's a tie!")

elif user_choice == "2" and computer_choice == "2":

    print("Computer picked 2 - Scissors, It's a tie!")

elif user_choice == "3" and computer_choice == "3":

    print("Computer picked 3 - Paper, It's a tie!")

elif user_choice == "1" and computer_choice == "2":
    print("Computer picked 2 - Scissors, You win!")

elif user_choice == "3" and computer_choice == "1":

    print("Computer picked 1- Rock, You win!")

elif user_choice == "2" and computer_choice == "3":

    print("Computer picked 3 - Paper, You win!")

elif user_choice == "1" and computer_choice == "3":

    print("Computer picked 3 - Paper, Computer wins!")

elif user_choice == "2" and computer_choice == "1":

    print("Computer picked 1 - Rock, Computer wins!")

elif user_choice == "3" and computer_choice == "1":

    print("Computer picked 2 - Scissors, Computer wins!")
