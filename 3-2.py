#Lab3 Exercise 2

def whos_larger():
    """Compares the prompted number in a conditional statement
       definning whether is: 'zero','big number','small number',
       'small negative number' or 'big negative number'."""
    
    large_num = int(input("Enter any number. "))
    
    if large_num == 0:
        print("You picked zero")
    elif large_num > 0 :
        if large_num >= 100 :
            print("Thats a big number!")
        else:
            print("That's a small number...")
    elif large_num < 0:
        if large_num <= -100 :
            print("Thats a large negative number!")
        else:
            print("Small negative number...")
    else:
        pass

############
    
def num_measure():
    """Compares the prompted number in a conditional statement
       definning whether is a positive number or not."""
    
    small_num = int(input("What's the smallest positive number that you would consider large? "))
    
    if small_num >= 1:
        whos_larger()
    else:
        print("That's not a positive number")
        return
  
num_measure()