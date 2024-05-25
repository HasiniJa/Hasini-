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
while num != 26: 
    user_input = input("Enter the answer to 12 + 14, or press 's' to skip: ") 
    if user_input == 's': 
        break 
    else: 
        num = int(user_input) 
    if num != 26: 
        print("Incorrect. Try again.") 
    else: 
        grade=int(grade)+1
        finalgrade= grade/4*100
        print("Correct! You have been awarded 1 point!") 
print("Next question...") 

while num !=31:
   # print(grade)
    user_input = input("Enter the answer to 23 + 8, or press 's' to skip: ")
    if user_input == 's':
        print("Question skipped. 0 points awarded.")
        break
    else:
        num = int(user_input)
    if num !=31:
         print("Incorrect. Try again.")
    else: 
        grade=int(grade)+1
        finalgrade= grade/4*100
       # print(finalgrade)
        print("Correct! You have been awarded 1 point!") 
print("Next question...") 

while num !=43:
   # print(grade)
    user_input = input("Enter the answer to 30 + 13, or press 's' to skip: ")
    if user_input == 's':
        print("Question skipped. 0 points awarded.")
        break
    else:
        num = int(user_input)
    if num !=43:
         print("Incorrect. Try again.")
    else: 
        grade=int(grade)+1
        finalgrade= grade/4*100
        #print(finalgrade)
        print("Correct! You have been awarded 1 point!") 
print("Next question...") 

while num !=44:
   # print(grade)
    user_input = input("Enter the answer to 17 + 27, or press 's' to skip:")
    if user_input == 's':
        print("Question skipped. 0 points awarded.")
        break
    else:
        num = int(user_input)
    if num !=44:
         print("Incorrect. Try again.")
    else: 
        grade=int(grade)+1
        finalgrade= grade/4*100
        print(finalgrade)
        print("Correct! You have been awarded 1 point!") 
        print("You received a grade of "+str(finalgrade)+"%.")
