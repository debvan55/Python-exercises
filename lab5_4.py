#Lab 5 Exercise 4

def fib_str(m):
    """'fib_str' takes 'm' as a parameter to be the highest number
       from the Fibonacci sequence that will be displayed as an output"""
    index = 0
    if index < m:
        fib_seq = (0, 1,)
        if m == 1:
            seq_result = ' '.join(map(str,fib_seq))
            print (seq_result)
            return seq_result # fib_seq = "0, 1"
        elif m == 2: 
            fib_seq = fib_seq + (1,)
            initial = int(fib_seq[len(fib_seq)-1])
            secondary = int(fib_seq[len(fib_seq)-2])
            fib_seq = fib_seq + (initial+secondary,)# numb's been added.
            seq_result = ' '.join(map(str,fib_seq))
            print (seq_result)
            return seq_result # fib_seq = "0 1"
        else:
            fib_seq = (0,1,1,)
            while int(fib_seq[len(fib_seq)-1]) < m:
                initial = int(fib_seq[len(fib_seq)-1])
                secondary = int(fib_seq[len(fib_seq)-2])
                
                fib_seq = fib_seq + (initial+secondary,)
            #print (fib_seq)
            new_string = ""
            for i in range(0,len(fib_seq)):
                #print(fib_seq[i])
                if fib_seq[i] <= m:
                    new_string = new_string +" "+ str(fib_seq[i])
                    #print(new_string)
            print(new_string)
            #print (seq_string)
            return str(new_string) # Exits the loop returning a value.
    return str(index) # Exits the loop returning zero.
#######################################################################
#FAIL: fib_str(10) is correct     
# 0 1 1 2 3 5 8 13 21 34 55 89
#FAIL: fib_str(100) is correct
#"0 1 1 2 3 5 8"
#"0 1 1 2 3 5 8 13 21 34 55 89"

#Couldn't pass the test... I dont know why
########################################################################
# fib_str(10)    
# fib_str(100) 

########################################################################
#Option 2 generates Fibonacci numbers and turn'em to string using '.join'
#and map() built-in functions
# def fib_str(m):
#     """'fib_str' takes 'm' as a parameter to be the highest number
#        from the Fibonacci sequence that will be displayed as an output"""
#     index = 0
#     if index < m:
#         fib_seq = (0,)
#         if m == 1:
#             seq_result = ' '.join(map(str,fib_seq))
#             print (seq_result)
#             return seq_result # fib_seq = "0"
#         elif m == 2: 
#             fib_seq = fib_seq + (1,)
#             seq_result = ' '.join(map(str,fib_seq))
#             print (seq_result)
#             return seq_result # fib_seq = "0 1"
#         else:
#             fib_seq = (0,1,1,)
#             while index < m:
#                 initial = int(fib_seq[len(fib_seq)-1])
#                 secondary = int(fib_seq[len(fib_seq)-2])
#                 fib_seq = fib_seq + (initial+secondary,)
#                 index = index +1
#             new_string = fib_seq[0:m]
#             seq_string = ' '.join(map(str,new_string))
#             print (seq_string)
#             return seq_string #str(fib_seq[0:m]) # Exits the loop returning a value.
#   
#     return str(index) # Exits the loop returning zero.
#     
#     #Syntax:
#     #string_name.join(iterable) 
#     #string_name: It is the name of string in which
#     #    joined elements of iterable will be stored.
#     
# fib_str(16)       
