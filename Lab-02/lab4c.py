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

 return math.pi * radius **2
 

while True:
 radius = input("Enter a radius between 0 and 1999. Press Enter to exit: ")
 input_val = 0

 if radius == "" :
  print ("Program was Cancelled. ")
  break
 
 elif radius == isinstance(radius,str) : 
   print ("Error. Out of bounds. ")
   print ("Enter a radius between 0 and 1999. ") 
 else:
    input_val += float(radius)
    
 if input_val < 0 or input_val > 1999 :
    print ("Error. Out of bounds. ")
    print ("Enter a radius between 0 and 1999. ")
 else:
  rtrn_circle_area(input_val)

if __name__ == "__main__":
  print("Radius: "+str(input_val)+". Area:  "+str(rtrn_circle_area(input_val))+".")
         
