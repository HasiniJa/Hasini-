'''
Student Name: Hasini Jayasekara
Student ID: 165513235
Lab 04
'''
import sys
def main():

# Check if a filename was provided as a command-line argument
   if len(sys.argv) > 1:
        filename = sys.argv[1]
   else:
         # Default to 'readme.txt' if no filename was provided
        filename = 'readme.txt'

   # Open the file 
   file = open(filename, 'r')
   lines= file.readlines()

  # Print the contents in reverse order
   for line in reversed(lines):
     print(line.strip()) # Print each line without leading whitespace

if __name__ == "__main__":
    main()