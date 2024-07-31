'''
Student Name: Hasini Jayasekara
Student ID: 165513235
'''
import os

def check_internet():
    # Check internet connectivity by pinging Google
    response = os.system("ping -c 4 google.com" if os.name != 'nt' else "ping -n 4 google.com")
    
    if response == 0:
        print("The Internet is UP.")
    else:
        print("The Internet is DOWN.")

def greet_user():
    # Get the username of the logged-in user
    user = os.popen('whoami').read().strip()
    print(f"Welcome, {user}.")

def system_info():
    # Print system uptime or system information
    if os.name != 'nt':
        # Unix-based system
        uptime = os.popen('uptime').read().strip()
        print(f"uptime is:\n{uptime}")
    else:
        # Windows system
        system_info = os.popen('systeminfo').read().strip()
        print(f"systeminfo is:\n{system_info}")

def main():
    check_internet()
    greet_user()
    system_info()

if __name__ == "__main__":
    main()
