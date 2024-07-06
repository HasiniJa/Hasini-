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
        # Open the file for reading
        file= open(filename, 'r') 
        lines = file.readlines()

        for line in lines:
            max_char = ''
            for char in line:
                if char.isalpha():
                    # Convert to lower case
                    char = char.lower()
                    if max_char == '' or char > max_char:
                        max_char = char

            if max_char:
                print(max_char)

    except FileNotFoundError:
        print(f"ERROR: {filename} not found.")
        return

if __name__ == "__main__":
    main()