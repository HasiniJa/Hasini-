'''
Student Name : Hasini Jayasekara
Student ID : 165513235
Lab3: Word Game

Sample Output 
Your word: 
_ _ _ _ _ 
Enter your guess: e 
_ _ _ e _ 
Enter your guess: m 
_ _ m e _ 
Enter your guess: a 
_ a m e _ 
Enter your guess: camel 
You win! 
'''
import random

#fruits list
fruits = ['apple', 'banana', 'grapes', 'blueberries', 'pinaple' ]

#selecting random fruit
fruit_guess= random.choice(fruits)

# initializing empty set to keep track on guessing letters. 
letter_guess= set()

#intialize number of attempts user have :5
user_attempts=5

while user_attempts > 0:
    
    secret_fruit ='_'

    for letter in fruit_guess:
      if letter in  letter_guess:
         secret_fruit+=letter
      else:
         secret_fruit += '_'

#print the food item
    print(''.join(secret_fruit))
    
    if '_' not in secret_fruit:
      print("You win!.")
      break
    user_guess = input("Enter your guess: ").strip().lower()
        
    if len(user_guess) != 1:
            print("Please enter a single letter.")
            continue

    if user_guess in secret_fruit:
            print("You've already guessed that letter.")
            continue
              # Add the guessed letter to the list
    secret_fruit.append(user_guess)

    if user_guess in secret_fruit:
            print(f"Good job! {user_guess} is in the word.")
    else:
            user_attempts -= 1
            print(f"Sorry, {user_guess} is not in the word. You have {user_attempts} attempts left.")

    if user_attempts == 0:
        print(f"Game over! The word was: {secret_fruit}")

