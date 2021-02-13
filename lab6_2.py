#Lab 6 Exercise 2

def make_times_table(n):
    """It returns the times table of 'n' parameter
       and all the precedent numbers in a range on their own lists."""
    list_1 = []
    while len(list_1) < n:
        for i in range(0,n):
            list_2=[] 
            for j in range(0,n):
                value = ((i+1)*(j+1))
                list_2.append(value)
            list_1.append(list_2) 

    #print(list_1)
    return list_1 #Returns a times table matrix.

###################################################################             
# make_times_table(4)
# make_times_table(3)            
# make_times_table(2)            
# make_times_table(0) 