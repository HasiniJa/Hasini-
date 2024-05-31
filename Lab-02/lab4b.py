'''
Student Name: Hasini Jayasekara
Student ID : 165513235
Lab4b.py : Functions 
'''

from random import randint 
 
def rtrn_area(length, width):  # There are two parameters. Length and Width
    '''
    This function calculates the Area of rectangle.

    it consist of two parameters. Length and Width.
     
    and it has a return value. it is the area

    formula is area = length * width

    '''   
    return length * width  # return value


def print_all_caps(name, age):  # There are two parameters. name and age 
    '''
    This function prints Name in Capital Letters with the age.

    it consist of two parameters. name and age

    it do not have a return value
    '''
    cap_name = name.upper()

def get_rando():   
    '''
    This function generates a random integer number. 

    it consist of two parameters. 1 and 101.

    it will only return a value between 1 and 101.
    
    There is a return value. it is random Integer number. 
    '''
    return randint(1, 101) # return value with parameters




def is_odd(num):  # parameters :1  parameter name: number 
    '''
    This function checks the number is odd or even number.

    it has 1 parameter.

    there is a return value. it is a boolean value. true or false.
    
    '''
    if num % 2 == 1:  # formula = if number's remainder is 1 
        return True   # returns true
    else:  
        return False # else return false.
    
    if __name__ == "__main__":

        print(is_odd(13)) 

        print(is_odd(get_rando())) 

        lucky_num = get_rando() 

        print(lucky_num)

        print('THIS PERSON\'S NAME IS ' + cap_name + ' AND THEY ARE ' + str(age) + ' YEARS OLD!!!')
        print_all_caps('eric', 41) 
        print_all_caps('melissa', 40)
        
        area = rtrn_area(5,3)
        print(area)



