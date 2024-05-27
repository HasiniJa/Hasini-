'''
Student Name : Hasini Jayasekara
Student ID : 165513235
Lab2: Challenge3 - Binary Converter
'''

# ask the user to input any decimal number
user_input =input("Enter any decimal number: ")

#convert it to a numeric value
num1 = int(user_input)

#defining empty variable to store the result
result = ""

while num1 > 0:

    #getting the remainder of the user input
    remainder = num1 % 2

    #storing the remainder of the user input
    result = str(remainder)+ result

    #get the quotient of the user input
    num1 = num1 // 2

#print the binary value   
print("The binary value for "+user_input+"  is "+result+"")




