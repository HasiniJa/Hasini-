'''Name: Hasini Jayasekara
   Student ID: 165513235
'''
#defining variables
#number1=input("Enter a number between 0.0 and 0.9")
#num1=float(number1)

#program to get the integer number from 0.0 to 0.9

'''
if(num1>=0.0) and(num1<=0.9):   #checks the input value is between 0.0 and less than 0.9
   decimalvalue=float(num1)     #getting the float value
   if(decimalvalue<0.5):         #again checks whether the decimal value is less than 0.5
      result=int(decimalvalue)   #if its less than 0.5 converts the float into int
      print(result)              #prints the integer value
      
                  
   elif(decimalvalue>=0.5):       #checks whether the input value is greater than or equal 0.5
      resultfloat= decimalvalue+1 #if greater than 0.5 then add 1
      result=int(resultfloat)     #convert the float value to the integer value
      print(result)               #prints the value
else:
   print("Error")
'''
number2=input("Enter any Decimal number")                   #input the decimal number
num2=float(number2)                                         #convert into float value
numericvalue=int(num2)                                      #get the numerical value of the numer
result=num2-numericvalue                                    #get the decimal value by substracting the numeric value from the float value
#print(result)

if(result>=0.5):                                           # checks whether the result is  greater than or equal 0.5
 finalresult=num2+1                                        #if the statement is true final result has been generated by adding 1 to the num2
 numericval=int(finalresult)                               #create another variable and convert the final result in to integer value
 print(numericval)                                         #print the integer value of the number
else:
 numericval2=int(num2)                                    # convert the float value in to integer
 print(numericval2)                                       # print the integer value
 




