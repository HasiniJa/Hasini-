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
skip_count =0
question_count=0

while True:
        num1 = randint(1,10)
        num2 = randint(1,10)
        correct_answer = num1 + num2    
        user_input = input("Enter the answer to "+str(num1)+" + "+str(num2)+", or press 's' to skip or 'q' to quit: ")
        question_count= question_count+1
        if user_input== 'q':
                if question_count > 0:
                    finalgrade = (grade / question_count) * 100
                else:
                    finalgrade = 0
                print("Quiz over. You scored "+str(finalgrade)+".0%.")
                break
        elif user_input == 's':
                skip_count =skip_count +1
                print("Question skipped. 0 points awarded. ")

                if question_count == skip_count :
                    finalgrade = 0
                    print("You have skipped all the questions. You recieved a grade of 0.0% ")
                    
                else:
                   finalgrade = (grade / question_count) * 100
                print("You scored "+str(finalgrade)+".0%.")
                
                
        else:
         answer= int(user_input)
         if  answer== correct_answer:
               print("Correct! You have been awarded 1 point!") 
               grade=int(grade)+1
               finalgrade= grade/question_count*100
         else:
               print("Incorrect. Try again.")





        
        
         
         
     
        
         

        
         
    
    
    
        
       