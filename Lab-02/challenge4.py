'''
Student Name: Hasini Jayasekara
Student ID : 165513235
Challenge4.py : Calculate Trend

Sample Output
Enter the starting X value: 1 
Enter the next Y value: 1 
Enter the new X value: 3 
Enter the new Y value: 3 
Slope is: 1.0 
Enter the new X value: 3 
Enter the new Y value: 3 
Slope is: 0.0 
Enter the new X value: 5 
Enter the new Y value: 4 
Slope is: 0.5 
Enter the new X value: 0 
Enter the new Y value: 1 
Slope is: 0.6 
Enter the new X value: 3 
Enter the new Y value: 0 
Slope is: -0.3333333333333333
'''

#creating function slope
def rtrn_slope(xval1, yval1, xval2, yval2):
    
    if(xval1 == xval2):                   #checks whether values are equal
      return float("Slope is undefined")  # returns the error message scope is undefined
    slope = (yval2 - yval1) / (xval2 - xval1)   #formula 
    return slope

def valid_input(prompt): # function for validating the input
     
     while True:
          value = input(prompt)
          
          if value.isdigit(): #check input value is a number
              inputval= int(value)
              if 0 <= inputval <= 10: #checks if the input value is between 0 and 10
                return inputval
              else:
                print("Value must be between 0 and 10.") #error message
          else:
              print("Value must be numerical value.") # error message

def main() :
     print("Calculating Trend")
     xval1 = valid_input("Enter the starting X value: ") #Entering the x value for point 1
     yval1 = valid_input("Enter the starting Y value: ") #Entering the y value for point 1

     while True:
        xval2 = valid_input("Enter the new X value: ")   #Entering the x value for point 2
        yval2 = valid_input("Enter the new Y value: ")   #Entering the y value for point 2

        slope = rtrn_slope(xval1,xval2,yval1,yval2)     # calling function to calculate the slope
        print(f"Slope is: {slope}")                     # printing slope value

        xval1, yval1 = xval2, yval2  # updates the current point to the new point to continue
if __name__ == "__main__":
    main()

     
    
