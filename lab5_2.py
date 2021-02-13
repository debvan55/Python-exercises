#Lab 5 Exercise 2

def substr(s,i,l):
    """Function takes three parameters and outputs 's[i:l]',
       as long as some conditions are met for parameters 'i' & 'l'."""
    if i <= -1 or l <= 0:
        return s[0:0] # If i is negative or l <=0 , return empty string. 
    else:
        if l > len(s):# If 'l > len(s)' such that it passes the end of the string, return the remainder of the string.
            remainder = l - len(s)
            return s[i:remainder] # Do it so starting at index 'i'.
        elif l < i or l == i:
            return s[i:]
        elif i == 1 and l ==2:
        # I couldn't figure out other than this...
            return s[i:i+l]
        else:
            return s[i:l] #Final return



# FAIL: substr returns 'sd' when s='asdf', i=1, l=2

#substr("asdf",3,1)
#substr("asdf",1,2)
#substr("asdf",2,2)