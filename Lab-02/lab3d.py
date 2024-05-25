'''
Student Name: Hasini Jayasekara
Student ID : 165513235
Lab3d.py : Guessing Game
'''
'''
Sample Output 
Guess a number between 1 and 10: 3 
Sorry, that's not it. 
Guess a number between 1 and 10: 5 
Sorry, that's not it. 
Guess a number between 1 and 10: 7 
Correct! You win. 
'''
secret = 7
user_input =input("Guess a number between 1 and 10:")
user_guess=int(user_input)

while user_guess < 10:
    if user_guess == secret:
     print("Correct! You win.")
     break
    else :
     print("Sorry, that's not it.")
     user_input1 =input("Guess a number between 1 and 10:")
     user_guess=int(user_input1)

     

     