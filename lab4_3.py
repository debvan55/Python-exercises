#Lab 4 Exercise 3

def is_numeric(n):
    """Takes one parameter and checks; it returns a boolean value."""
    func_input = isinstance(n,(int))
    if func_input:
        return func_input
    return func_input

def is_leapyear(year):
    """It checks whether the input is a leap year or not"""
    if is_numeric(year):
        if year % 4 == 0:
        #First checks ehther is divisible by 4
            if year % 100 == 0:
            #Then check for 100
                if year % 400 == 0:
                #Last checks for 400
                    return is_numeric(year)
                return not is_numeric(year)
            return is_numeric(year)
            #This would return a valid year...
        return not is_numeric(year)    
    return is_numeric(year)
