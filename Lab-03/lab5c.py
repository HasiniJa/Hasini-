'''
Student Name : Hasini Jayasekara
Student ID : 165513235
Lab3: Word Game

Sample Output 
I'm thinking of an animal. Can you guess what it is? 
Enter a letter or a guess. Press enter to quit: kangaroo 
Sorry, that's not it. 
Enter a letter or a guess. Press enter to quit: a 
Yes, my word contains that letter. 
Enter a letter or a guess. Press enter to quit: z 
Sorry, my word doesn't contain that letter. 
Enter a letter or a guess. Press enter to quit: m 
Yes, my word contains that letter. 
Enter a letter or a guess. Press enter to quit: c 
Yes, my word contains that letter. 
Enter a letter or a guess. Press enter to quit: camel 
You win! 
'''
import random
animals = ['snake', 'hamster', 'scorpion', 'beaver', 'mosquito', 'camel', 'vulture', 'horse', 'python', 'capybara' ]

secret=animals(random.choice)

while True:
    user_input= input("I'm thinking of an animal. Can you guess what it is? Enter a letter or a guess. Press enter to quit: ")
    
    if user_input ==" ":
      break

    elif user_input == secret:  
      print("You win!")
      break

    elif len(user_input)== 1:
       if user_input in secret:
          print("Yes, my word contains that letter. ")

       else:
          print("Sorry, my word doesn't contain that letter. ")
          
    else:
       print("Sorry, that's not it. ")
    