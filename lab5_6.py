#Lab 5 Exercise 6

def num_vowels(word):
    """It counts the number of vowels in parameter 'word',
       also checks for 'y' in the place of a vowels."""
    vowels_= "aeiou"
    count =  0
    word = word.lower() # Turns input to lower-case
    
    for i in range(len(word)):
        if word[i] == "y":
            exeption = word.index("y")
            if exeption == 0 or word[i+1] in vowels_:
                pass
            elif exeption == 0 and word[i+1] not in vowels_ :
                count = count + 1
                break
            
        elif word[i] in vowels_:
            count = count + 1
       
    print(count)
    return count
    
#######################################################################
      
#num_vowels("yak")

    
    