'''
Student Name: Hasini Jayasekara
Student ID: 165513235
Lab-04
'''
import sys

def main():
    # Check if the filename is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python challenge6.py <filename>")
        return

    filename = sys.argv[1]

    try:
        # Open the file 
        file= open(filename, 'r') 
        lines = file.readlines() # Read all lines from the file

# Process each line to find the highest alphabetical character
        for line in lines:
            max_char = '' # Initialize the variable to store the maximum character
            for char in line:
                if char.isalpha(): # Check if the character is a letter
                    # Convert to lower case
                    char = char.lower()
                    if max_char == '' or char > max_char:
                        max_char = char # Update the maximum character if current is greater

            if max_char: # If a maximum character was found, print it
                print(max_char)

    except FileNotFoundError:
        print(f"ERROR: {filename} not found.")
        return

if __name__ == "__main__":
    main()