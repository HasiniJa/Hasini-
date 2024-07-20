'''
Student Name : Hasini Jayasekara
Student ID : 165513235
'''

import csv
import sys

def read_csv(filename):
    """Reads a CSV file and returns a list of dictionaries."""
    list_of_dicts = []
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                list_of_dicts.append(row)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        sys.exit(1)
    return list_of_dicts

def write_csv(filename, list_of_dicts):
    """Writes a list of dictionaries to a CSV file."""
    if not list_of_dicts:
        return
    
    fieldnames = list_of_dicts[0].keys()
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in list_of_dicts:
            writer.writerow(row)

def substitute_data(list_of_dicts):
    """Substitutes specific values in the list of dictionaries."""
    for row in list_of_dicts:
        if row.get('First Name') == 'Christopher':
            row['First Name'] = 'Chris'
        if row.get('Last Name') == 'Patal':
            row['Last Name'] = 'Patel'
        if row.get('Last Name') == 'Smith':
            row['Last Name'] = 'Nichols'
        if row.get('Address') == '81 Vanier':
            row['Address'] = '72 Princeton'
        if row.get('Last Name') == 'Geary':
            row['Address'] = '455 Bloor'
        if row.get('City') == 'North York':
            row['City'] = 'Toronto'
        if 'Country' in row and row['Country'] == 'Canada':
            row['Country'] = 'CA'
    return list_of_dicts

def print_table(list_of_dicts):
    """Prints a table from a list of dictionaries."""
    if not list_of_dicts:
        return
    
    # Get the field names from the first dictionary
    fieldnames = list_of_dicts[0].keys()
    
    # Define column widths (assuming fixed width for simplicity)
    col_widths = {field: max(len(field), 15) for field in fieldnames}

    # Print header
    header = " | ".join(f"{field:<{col_widths[field]}}" for field in fieldnames)
    print(header)
    print("-" * len(header))

    # Print rows
    for row in list_of_dicts:
        print(" | ".join(f"{row[field]:<{col_widths[field]}}" for field in fieldnames))

def main(filename):
    data = read_csv(filename)
    data = substitute_data(data)
    write_csv(filename, data)
    print(f"Processed and saved the file: {filename}")
    print("\nModified Table:")
    print_table(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python challenge7.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    main(filename)