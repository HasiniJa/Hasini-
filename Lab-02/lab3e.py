'''
Student Name : Hasini Jayasekara
Student ID : 165513235
Lab2: Math Quiz 02
'''
'''
Sample Output 
Enter the answer to 1 + 6, press 's' to skip or 'q' to quit: 27 
Incorrect. Try again. 
Enter the answer to 1 + 6, or press 's' to skip or 'q' to quit: 7 
Correct! You have been awarded 1 point!" 
Next question... 
Enter the answer to 2 + 18, or press 's' to skip: s 
Question skipped. 0 points awarded. 
Enter the answer to 17 + 5, or press 's' to skip: q 
Quiz over. You scored 50.0%.
'''
#defining num variable
from random import randint

result = 0
answer = str(result)
grade = 0
finalgrade=0
    
while result != 'q':
     num1 = randint(1,10)
     num2 = randint(1,10)
     user_input = input("Enter the answer to "+str(num1)+" + "+str(num2)+", or press 's' to skip or 'q' to quit: ") 
     result = num1+num2
     
     if user_input == 's':
        print("Question skipped. 0 points awarded. ")
        break
     elif user_input =='q':
         print("Quiz over. You scored "+str(finalgrade)+"%.")
         break
     else:
         answer= int(user_input)
     if  answer== result:
         print("Correct! You have been awarded 1 point!") 
         grade=int(grade)+1
         finalgrade= grade/4*100
     
     else:
          print("Incorrect. Try again.")
        
        
         
         
     
        
         

        
         
    
    
    
        
       