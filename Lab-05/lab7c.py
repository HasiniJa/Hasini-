from lab7b import print_meal_plan

# Define the template dictionary
template = {
    'Breakfast': None,
    'Lunch': None,
    'Dinner': None
}


# List to hold the meal plans for each day
days = []

def main():
    while True:
        # Ask if the user wants to add a day
        add_day = input("Would you like to add a day? (y/n) ").strip().lower()
        
        if add_day == 'y':
            # Create a new dictionary from the template
            new_day = template.copy()  # Use .copy() to avoid modifying the template
            
            # Collect meal ideas from the user
            for meal in new_day.keys():
                new_day[meal] = input(f"Please enter what you would like to eat for {meal}: ").strip()
            
            # Append the new day to the list of days
            days.append(new_day)
        
        elif add_day == 'n':
            # Exit the loop if user doesn't want to add more days
            break
        
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    
    # Ask for the day number to print
    while True:
        try:
            day_number = int(input(f"Please enter a day number for the menu you would like to print (1-{len(days)}): ").strip())
            
            # Check if the number is within range
            if 1 <= day_number <= len(days):
                # Print the selected day's menu
                print_meal_plan(days[day_number - 1])
                break
            else:
                print("Error: Day number out of range.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()