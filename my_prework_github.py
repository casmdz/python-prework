#QUESTON 1
#Write a function to print "hello_USERNAME!"
#username is the input of the finction. The first line of code has been defined as below. 

#from ch8

def hello_name(user_name):
    """Say hello to user"""
    print("hello_" + user_name.upper() + "!")
hello_name('USERNAME')

#QUESTION 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

#my notes
#ch7 modulo operator (%) divides one num by another num and returns the remainder
#it returns 0 if the nums are divisible by each other 
#continue a loop based on the result of a conditional test, loop that counts from ... but only prints the odd... page 126


def first_odds():
  for number in range(0, 101):
    if number % 2 == 0:
        continue
    else:
      print(number)
first_odds()


#my notes the actual chapters
#if number % 2 == 0:
#    print("\nThe number " + str(number) + " is even")
#else:
#    print("\nThe number " + str(number) + " is odd.")

print('')
#QUESTION 3
#Please write a Python function, max_num_in_list to return the max number of a given list.


#>>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#>>> min(digits)
#0
#>>> max(digits)
#9
#>>> sum(digits

def max_num_in_list(a_list):
  """Print the max num in list"""
  a_list = [1, 101]
#  max_num = a_list[0]
  for num in a_list:
    max_num = max_num >= 1

print(max(max_num_in_list))



#  first_odds = range(0, 101)

#  if max_num % 2 == 0:
#    return max(first_odds)

