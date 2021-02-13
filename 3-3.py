#Lab 3 Exercise 3

def num_category(n):
    """This function categorize the parameter 'n'
       depending on whether its value is: 'Even', 'Lucky',
       'Even and Lucky' or 'Just a number'."""
    
    if n % 2 == 0 and n % 7 == 0 or n % 13 == 0:
        print("Even and Lucky!!")
    elif n % 2 == 0:
        print("Even")
    elif n % 7 == 0 or n % 13 == 0 :
        print("Lucky")
    else:
        print("Just a number...")

###############

def plus_num():
    """It simply checks whether the number is positive or negative,
       then runs 'num_category'. """
    positiv_num = int(input("Pick a positive number: "))
    if positiv_num < 0 :
        print("You're so negative!")
        return
    else:
        num_category(positiv_num)

plus_num()
        
    