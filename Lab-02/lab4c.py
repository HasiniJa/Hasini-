'''
Student Name: Hasini Jayasekara
Student ID : 165513235
Lab4c.py : Circle Area Calculator 

Sample Output 
Circle Area Calculator 
Enter a radius between 0 and 1999. Press Enter to exit: 2 
Radius: 2. Area: 12.566370614359172. 
Enter a radius between 0 and 1999. Press Enter to exit: ten 
Error: ten is not a number. 
Enter a radius between 0 and 1999. Press Enter to exit: 17 
Radius: 17. Area: 907.9202768874502. 
Enter a radius between 0 and 1999. Press Enter to exit: 2001 
Error: 2001 is out of range. 
Enter a radius between 0 and 1999. Press Enter to exit:  
Exiting...
'''
import math

#function calculating area of circle
def rtrn_circle_area(radius):
 return math.pi * radius * radius
 
 while true:
  user_input = input("Enter a radius between 0 and 1999. Press Enter to exit: ")

