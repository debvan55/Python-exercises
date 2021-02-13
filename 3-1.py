#Lab3 Exercise 1

def tis_multiple():
    """Initially two prompts are compared with the 'oper' variable,
       a conditional statement is executed returning the desired output."""
    
    div_int = int(input("Pick an integer divisor: "))
    my_int = int(input("Pick an integer: "))
    oper = my_int % div_int

    if oper == 0 :
        print("Yes, "+str(my_int)+" it is a multiple of "+str(div_int))
    else:
        print("No, "+str(my_int)+" is not a multiple of "+str(div_int))

tis_multiple()