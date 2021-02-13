# Lab 7, Exercise 2

def lookup(val,d):
    """Check for the type of parameter 'd' expecting a dictionary.
       returns a tuple containning all keys in given dictionary for which the value
       is the same as the given parameter."""
    my_tuple = []
    if not isinstance(d,dict):
        raise TypeError("d must be a dict")
    else:
        for key,value in d.items():
            #print(key,value)
            if value == val:
                my_tuple.append(key)
            else:
                pass
            continue
        my_tuple = tuple(my_tuple)
        #print(my_tuple)
        return my_tuple
