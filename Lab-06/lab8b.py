'''
Student Name: Hasini Jayasekara
Student ID: 165513235
Lab-06 - lab8b.py
'''

import re
import sys

def main(filename):
    # Compile the regex for matching phone numbers
    phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
    
    try:
        # Open the file and read its contents
        with open(filename, 'r') as file:
            contents = file.read()
        
        # Find all phone numbers in the file
        phone_numbers = phone_regex.findall(contents)
        
        # Print the number of results found
        print(f"Number of phone numbers found: {len(phone_numbers)}")
        
        # Ask the user if they would like to see the results
        user_input = input("Would you like to see the results? (y/n): ").strip().lower()
        
        if user_input == 'y' or user_input == '':
            for phone_number in phone_numbers:
                print(f"Found phone number: {phone_number}")
        else:
            print("Terminating the program.")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python lab8b.py <filename>")
    else:
        main(sys.argv[1])