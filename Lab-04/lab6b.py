'''
Student Name: Hasini Jayasekara
Student ID: 165513235
Lab 04
'''
import sys
def main():

   if len(sys.argv) > 1:
        filename = sys.argv[1]
   else:
        filename = 'readme.txt'

   file = open(filename, 'r')
   lines= file.readlines()

  # Print the contents in reverse order
   for line in reversed(lines):
     print(line.strip())

if __name__ == "__main__":
    main()