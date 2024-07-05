'''
Name : Hasini Jayasekara
Student ID : 165513234
Lab 04 
'''

data_to_write = ['First Line!', 'Second Line!!', 'Third Line!!!', '...and so on!']

f = open('testing.txt', 'w') 

    # Loop through each element in the data_to_write list
for line in data_to_write:
        # Write each element to the file,in a new line
        f.write(line + '\n')


