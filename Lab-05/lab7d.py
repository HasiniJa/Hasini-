'''
Student Name : Hasini Jayasekara
Student ID : 165513235
'''

import csv
import sys

def read_csv(filename):
    """Reads a CSV file and returns a list of dictionaries."""
    list_of_dicts = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            list_of_dicts.append(row)
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
        if row.get('Country') == 'Canada':
            row['Country'] = 'CA'
    return list_of_dicts

def main(filename):
    data = read_csv(filename)
    data = substitute_data(data)
    write_csv(filename, data)
    print(f"Processed and saved the file: {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python lab7d.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    main(filename)