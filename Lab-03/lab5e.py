'''
Student Name : Hasini Jayasekara
Student ID : 165513235
Lab3: Average Calculator

Sample Output

Usage: Enter one or more command line arguments. 
python lab5e.py 2 ten 17 39 
Number found: 2. 
Error: ten is not a number. 
Number found: 17. 
Number found: 39. 
Average for 3 numbers: 19.3 
 
'''
import sys

#main function
def main():
    
    if len(sys.argv) == 1: 
     print('Usage: Please enter an argument.') 
     sys.exit(1) 
    else: 
     print('Thank you! Program succeeded.') 
    sys.exit(0) 

numbers = []
 
 #using for loop to iterate over the arguments.
for arg in sys.argv[1:]: #skipping the first argument(file name)
 
 # check if its a valid numerical number
 if arg.lstrip('-').isdigit():
   number = int(arg)
   print(f"Number found: {number}.")
   numbers.append(number)
 else:
     # If argument is not valid numerical value, print an error message
    print(f"Error: {arg} is not a number.")

     #calculating numbers if they are valid
if numbers:
      average = sum(numbers) / len(numbers)
      print(f"Average for {len(numbers)} numbers: {average:.1f}")
else:
        print("No valid numbers entered.")

if __name__ == "__main__":
    main()
    