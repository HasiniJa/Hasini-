'''
Student Name : Hasini Jayasekara
Student ID : 165513235
Lab 07: a
'''

student1 = {'first_name': 'eric', 'last_name':'smith', 'addr1': '217 Au Large Blvd', 'city': 'Toronto', 'prov': 'Ontario', 'pcode': 'M4A 1P3'}

# shipping_label function
def shipping_label(a_dict):
    "Takes a dictionary, generates a string"
    first_name = a_dict['first_name'].capitalize()
    last_name = a_dict['last_name'].capitalize()
    a_str = f"{first_name} {last_name}\n"
    a_str += f"{a_dict['addr1']}\n"
    a_str += f"{a_dict['city']}, {a_dict['prov']}\n"
    a_str += f"{a_dict['pcode']}"
    return a_str

# print the shipping label
if __name__ == "__main__":
    print(shipping_label(student1))