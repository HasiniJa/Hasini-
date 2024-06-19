# Question 1

list1 = [54, 44, 27, 79, 91, 41]
def question1(list1):
 # print the original list
 print(f"Original list {list1}")

 #remove the 4th index
 item =list1.pop(4)
 print(f"List after removing element at index 4 {list1}")

 #adding item to the 2nd index
 list1.insert(1, item)
 print(f"List after adding element at index 2 {list1}")

 #add the item to the end of list
 list1.append(item)
 print(f"List after adding element at last {list1}")


# Question 2

numlist1 = [10, 20, 30, 40]
numlist2 = [100, 200, 300, 400]

def question2(numlist1,numlist2):

  list_length = len(numlist1)

  # iterate through the list 1 
  for i in range(list_length):
     item1 = numlist1[i]

  # Calculate the  index in list2 for reverse order
     item2 = numlist2[list_length - 1 - i]

      # Print the items from both lists
     print(f"{item1} {item2}")




# Question 3

# row counts
rows = 5

def question3(rows):
 
  # Loop through each row from 1 to rows
 for i in range(1, rows + 1):

    # For each row, print numbers from 1 to i
    for j in range(1, i + 1):

        print(j, end=' ') #print j with a space

    print('') # Move to the next line after finishing a row



if __name__ == '__main__':
  
  print("Running Question 1")
  question1_answer =question1(list1)
 
  print("Running Question 2")
  question2_answer =question2(numlist1,numlist2)

  print("Running Question 3")
  question3_answer = question3(rows)
  
  
 

