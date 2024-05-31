'''
Student Name: Hasini Jayasekara
Student ID : 165513235
Lab4a.py : Input Validation

Sample Output 
Enter a number between 1 and 10: 1 
Sorry, try again.  
Enter a number between 1 and 10: hamburger 
Error: not a number or out of bounds. 
Enter a number between 1 and 10: 100 
Error: not a number or out of bounds. 
Enter a number between 1 and 10: 6 
Correct! You win 
'''
from random import randint

secret = randint(1,10)

while True:
 user_input =input("Enter a number between 1 and 10: ")

 if user_input .isnumeric():
    user_guess= int(user_input)
 else:
   
   print("Error: not a number or out of bounds. ")
   print("Enter a number between 1 and 10: ")
   continue
   
 
 if user_guess < 1 or user_guess > 10:
     print("Error: not a number or out of bounds. ")
     print("Enter a number between 1 and 10: ")
 elif user_guess == secret:
     print("Correct! You win. ")
     break
 else :
     print("Sorry, that's not it. ")
     


     

     