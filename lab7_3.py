# Lab 7, Exercise 3

def histogram(wordlist):
    """Generates an histogram, it gather all letters present in the list and
       creates a dictionary recording the number of times each letter appears
       in the entire wordlist."""
    a_BC = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"#Valid characters.
    final_dicc = {} #Empty dictionary
    key_list = []
    if not isinstance(wordlist,list):
        raise TypeError("wordlist must be a list")
    else:
        for item in wordlist:
            for character in item:
                key_list.append(character)
            continue
        for item in key_list:
            if item not in a_BC:
                pass
            else:
                final_dicc[item] = final_dicc.get(item,0)+1
        print(final_dicc)
        return final_dicc

def prefix_histogram(wordlist,prefix_length):
    """Generates an histogram, it gather prefixes from the given list.
       Prefixes are defined by the parameter 'prefix_length'.
       The dictionary will record the number of times each prefix appears
       in the entire wordlist."""
    prefix_dicc = {}
    prefix_list = []
    if not isinstance(wordlist,list):
        raise TypeError("wordlist must be a list")
    else:
        if not isinstance(prefix_length,int):
            raise TypeError("prefix_length must be an int")
        else:
            if not prefix_length > 0:
                raise ValueError("prefix_length must be greater than 0")
            else:
                for item in wordlist:
                    if len(item) < prefix_length:
                        pass
                    else:
                        prefix_list.append(item[:prefix_length])
                pass
        for item in prefix_list:
            prefix_dicc[item] = prefix_dicc.get(item,0)+1
        #print(prefix_dicc)
        return prefix_dicc

def suffix_histogram(wordlist,suffix_length):
    """Generates an histogram, it gather suffixes from the given list.
       Suffixes are defined by the parameter 'suffix_length'.
       The dictionary will record the number of times each suffix appears
       in the entire wordlist."""
    suffix_dicc = {}
    suffix_list = []
    if not isinstance(wordlist,list):
        raise TypeError("wordlist must be a list")
    else:
        if not isinstance(suffix_length,int):
            raise TypeError("suffix_length must be an int")
        else:
            if not suffix_length > 0:
                raise ValueError("suffix_length must be greater than 0")
            else:
                for item in wordlist:
                    if len(item) < suffix_length:
                        pass
                    else:
                        suffix_list.append(item[len(item)-suffix_length:])
                pass
        for item in suffix_list:
            suffix_dicc[item] = suffix_dicc.get(item,0)+1
        #print(suffix_dicc)
        return suffix_dicc

#SAMPLE LIST & DICCIONARIO
gunSmith = ["kilo 141","Fal","M4A1","FR5.56","ODEN","M13","FN Scar17","AK-47" ]
diccionario = {"uno":1,"dos":2, "tres":3, "cuatro":3}
wordliss = [ "the", "quick", "brown", "fox", "jumped", "jumpily", "over", "lazy", "laser", "dogs" ]

#histogram(gunSmith)
#prefix_histogram(wordliss,4)
# suffix_histogram(wordliss,4)
# suffix_histogram(['loaded', 'hacked', 'jacked', 'smacked', 'snacked', 'read'], 5)