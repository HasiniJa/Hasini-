'''Student Name : Hasini Jayasekara
   Student ID : 165513235
   Lab2: Math Quiz 01
'''
'''
Sample Output
Enter the answer to 12 + 14, or press 's' to skip: 27 
Incorrect. Try again. 
Enter the answer to 12 + 14, or press 's' to skip: 26 
Correct! You have been awarded 1 point!" 
Next question... 
Enter the answer to 23 + 8, or press 's' to skip: s 
Question skipped. 0 points awarded. 
Enter the answer to 30 + 13, or press 's' to skip: 43 
Correct! You have been awarded 1 point!" 
Next question... 
Enter the answer to 17 + 27, or press 's' to skip: 44 
Correct! You have been awarded 1 point!" 
You received a grade of 75.0%.
'''
#defining num variable
num = 0  
grade = 0
finalgrade=0
skip_count=0
question_count =0

while num != 26: 
    user_input = input("Enter the answer to 12 + 14, or press 's' to skip: ") 
    question_count +=1
    if user_input == 's': 
        skip_count = skip_count+1
        print("Question skipped. 0 points awarded. ")
        break 
    else: 
        num = int(user_input) 
    if num !=26:
       print("Incorrect. Try again. ") 
    else: 
        grade=int(grade)+1
        finalgrade= grade/4*100
        print("Correct! You have been awarded 1 point! ") 
print("Next question...")

while num !=31:
   # print(grade)
    user_input = input("Enter the answer to 23 + 8, or press 's' to skip: ")
    question_count= question_count+1
    if user_input =='s':
        print("Question skipped. 0 points awarded. ") 
        skip_count =skip_count +1
        break
    else:
        num = int(user_input)
    if num !=31:
       print("Incorrect. Try again. ") 
    else: 
        grade=int(grade)+1
        finalgrade= grade/4*100
        print("Correct! You have been awarded 1 point! ") 
print("Next question...")

while num !=43:
   # print(grade)
    user_input = input("Enter the answer to 30 + 13, or press 's' to skip: ")
    question_count=question_count+1
    if user_input == 's':
        skip_count =skip_count +1
        print("Question skipped. 0 points awarded. ")
        break
    else:
        num = int(user_input)
    if num !=43:
       print("Incorrect. Try again. ") 
    else: 
        grade=int(grade)+1
        finalgrade= grade/4*100
        print("Correct! You have been awarded 1 point! ") 
print("Next question...")

while num !=44:
   # print(grade)
    user_input = input("Enter the answer to 17 + 27, or press 's' to skip: ")
    question_count=question_count+1
    if user_input == 's':
        skip_count =skip_count +1
        print("Question skipped. 0 points awarded. ")
    if skip_count == question_count:
        print("You have skipped all the questions. You recieved a grade of 0.0% ")
        break
    else:
        num = int(user_input)
  
    if num !=44:
       print("Incorrect. Try again. ") 
    else: 
        grade=int(grade)+1
        finalgrade= grade/question_count*100
        print("Correct! You have been awarded 1 point! ") 

print("You received a grade of "+str(finalgrade)+" .0%.")

