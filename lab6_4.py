#Lab 6 Exercise 4

def words(random_string):
    """Takes a single parameter and returns a single value consisting of each word
       in the given string, on its own line and sorted alphabetically."""
    
    a_BC = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"#Valid characters.
    split_string = random_string.split()
    cap_list = []
    for s in split_string:
        for char in s:
            if char in a_BC:
                pass
            else:    
                s = s.replace(char,'') 
        cap_list.append(s.capitalize())
    cap_list.sort()
    delimeter = '\n'
    end_list = delimeter.join(cap_list)
    #print(end_list)
    return end_list

#string_1 = "Hello, world!  Are YOU, the brave and true, ready to seize the day?"
# string_2 = "asdk 39j00j ofwel;vp 'i9;ou wep9w eo q30pouib ief;"
#Check --> "Asdk\nEo\nIef\nIou\nJj\nOfwelvp\nQpouib\nWepw"
#words(string_2)
#words(string_1)