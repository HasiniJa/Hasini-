'''
Student Name: Hasini Jayasekara
Student ID: 165513235
'''
import os

course_dir = '..'  # change to the parent directory

# Print the absolute path of the current directory
print('Your current directory is: ' + os.path.abspath(course_dir))

# Walk through the directory and list all subdirectories
for root, directories, filenames in os.walk(course_dir):
    for directory in directories:
        print(os.path.join(root, directory))

# Walk through the directory and list all files
for root, directories, filenames in os.walk(course_dir):
    for file in filenames:
        print(os.path.join(root, file))
