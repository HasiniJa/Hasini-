'''
Student Name : Hasini Jayasekara
Student ID : 165513235
Lab 07: 
'''

meal_plan = {'Breakfast': 'oatmeal', 'Lunch': 'sandwiches', 'Dinner': 'broccoli'} 

def print_meal_plan(meal_plan):
    """
    Print the meal plan in a formatted menu.
    """
    width = 50  # Define the total width for formatting
    title = "MENU FOR TODAY"
    
    # Print the title centered
    print(f"{title:^{width}}")
    # Print the header line composed of equal signs
    print("=" * width)
    
    # Define the fixed spacing for each meal item
    for meal, item in meal_plan.items():
        # Print each meal with fixed spacing
        print(f"{meal:<{width - 8}}{item}")

# Sample usage
if __name__ == "__main__":
    # Define a sample meal plan
  meal_plan = {'Breakfast': 'oatmeal', 'Lunch': 'sandwiches', 'Dinner': 'broccoli'} 
  print_meal_plan(meal_plan)
