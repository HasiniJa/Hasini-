'''
student name : Hasini Jayasekara
Student ID: 165513235
Lab-04
'''
import sys

def main():

# Check if the correct number of command line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: lab6c.py keyword filename")
        return

    keyword = sys.argv[1]
    filename = sys.argv[2]

    try:
        # Open the file and read the contents
        file = open(filename, 'r') 
        lines = file.readlines()

        # Search for the keyword and print if the keyword is found in each line
        for line_num, line in enumerate(lines, 1):
            if keyword in line:
                print(f"{line_num}: {line.strip()}")

    except FileNotFoundError:
        print(f"ERROR: {filename} not found.")

if __name__ == "__main__":
    main()