#Lab 5 Exercise 5

def cipher(s,n):
    """It takes a string and 'encode' it using the Ceasar cipher concept,
       string shifts to the 'n-th' position"""
    
    a_BC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = s.upper()
    encoded_string = ""
    
    if n == 0:
        return s
    else:
        while True:
            abc_cut1 = a_BC[n:]
            abc_cut2 = a_BC[:n]
            encoded_ABC = abc_cut1 + abc_cut2
            for i in range(len(s)):
                letter = encoded_ABC.find(s[i])
                encoded_letter = a_BC[letter]
                while s[i] in encoded_ABC:
                    encoded_string = encoded_string + encoded_letter
                    break
                if s[i] not in encoded_ABC:
                    encoded_string = encoded_string + s[i]
                continue
            break
        #print(encoded_string)
        return encoded_string
    return s

#cipher("ab c!", 3)