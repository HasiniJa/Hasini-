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
def circle_area(radius):

    return math.pi * radius ** 2


def main():
    while True:
        radius = input("Enter a radius between 0 and 1999. Press Enter to exit: ")  #ask the user to input value
        
        if radius == "":                               # checks whether the user has clicked enter as the input value
            print("Program was Cancelled.")
            break
        
        if not radius.replace('.', '', 1).isdigit():    # checks whether the input value is not a numerical value
            print("Error. "+radius+" is not a number.") # error message
            print("Enter a radius between 0 and 1999.")
            continue
        
        input_val = float(radius)                       # converts the input value in to a float value.
        
        if input_val < 0 or input_val > 1999:               # checks whether the input value is in the range
            print("Error.  "+input_val+" is out of range.")
            print("Enter a radius between 0 and 1999.")
        else:
            area = circle_area(input_val)                     # calles the function to calcuate area
            print(f"Radius: {input_val} ., Area: {area} .")   # print statement

if __name__ == "__main__":                                   # calling the function main
    main()
         
