'''
Student Name: Hasini Jayasekara
Student ID : 165513235
Lab3d.py : Guessing Game

Guess a number between 1 and 10: 3 
Sorry, that's not it. 
Please enter a valid number between 1 and 10. 
Guess a number between 1 and 10: 7 
Sorry, that's not it. 
Guess a number between 1 and 10: 4 
Correct! You win. 
'''
from random import randint

secret = randint(1,10)
user_input =input("Guess a number between 1 and 10: ")
user_guess=int(user_input)

while True:

   if user_guess == secret:
     print("Correct! You win. ")
     break
   else :
     print("Sorry, that's not it. ")
     user_input1 =input("Please enter a valid number between 1 and 10: ")
     user_guess=int(user_input1)

     

     