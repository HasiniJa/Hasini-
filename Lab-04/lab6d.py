'''
Student Name: Hasini Jayasekara
Student ID: 165513235
Lab -04
'''

import sys

def main():
    # Check if the filename is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python lab6d.py <filename>")
        return

    filename = sys.argv[1]

    try:
        # Open the file for reading
        with open(filename, 'r') as file:
            lines = file.readlines()

        new_lines = []
        for line in lines:
            words = line.split()
            new_line = []
            sum_numbers = 0

            for word in words:
                try:
                    # Try to convert the word to a float
                    num = float(word)
                    sum_numbers += num
                except ValueError:
                    # If conversion fails, it's a non-numeric word
                    new_line.append(word)

            print(sum_numbers)
            new_lines.append(' '.join(new_line))

        # Write the new lines back to the file
            file = open(filename, 'w') 
            for new_line in new_lines:
                file.write(new_line + '\n')

    except FileNotFoundError:
        print(f"ERROR: {filename} not found.")
        return

if __name__ == "__main__":
    main()