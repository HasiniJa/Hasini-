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
num1 = randint(1,10)
num2 = randint(1,10)
result= num1+num2

user_input = ("Enter any number to continue 's' to skip or 'q' to quit:")
print(user_input)

while result !=user_input :
    if user_input == 's':
        print("Question skipped. 0 points awarded.")
        break
    elif user_input == 'q':
        print("Question skipped. 0 points awarded.")
        break
    elif user_input != result:
        print("Incorrect. Try again.")
    else:
        grade=int(grade)+1
        finalgrade= grade/4*100
        print(finalgrade)
        print("Correct! You have been awarded 1 point!") 
        print("You received a grade of "+str(finalgrade)+"%.")
    