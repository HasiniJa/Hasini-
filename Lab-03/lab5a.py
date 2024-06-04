'''
Student Name : Hasini Jayasekara
Student ID : 165513235
Lab3: 
'''

#sum function to calculate the numbers user entered
def my_sum(user_numbers):
    total = 0
    for user_number in user_numbers:
        total +=user_number
    return total

if __name__ == "__main__": 
    user_numbers = []       # list to get the user inputs
    
    print("AVERAGE CALCULATOR") 
    while True: 
        user_input = input("Enter a number to add to your sum. Pressing Enter will exit. ") 
        if user_input == "": 
            break 
        else:  
            user_numbers.append(int(user_input)) 
    num_sum = my_sum(user_numbers)  # calculating the sum by my sum function
    num_length = len(user_numbers) 
    average = num_sum / num_length 
    print(f"Total sum is: {num_sum}. Total count is: {num_length}. Average for this list is: {average}.") 
    print("Thank you for using average calculator.") 