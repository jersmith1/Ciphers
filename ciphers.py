from crypto_helpers import*

def caesar(s, k, m):
    if m == 1:
        #following lines determine whart is executed based on the mode chosen if encrypt k=k if decreypt need the negative to move to the leftr
        k = k
    elif m == (0 - 1):
        k = (0 - k)
    else:
        raise ValueError ("mode not supported")
    new_string = ""
    #creates a new string to use so that each new character can be added to it in the for loop
    for i in range(len(s)):
        #for loop to iterate through strings 
        new_string += (shift_char(s[i], k))
        #adds each new character to the formerly empty string
    return new_string

def vigenere(s, k, m):
    k = pad_keyword(k, len(s))
    #makes the keyword the same length as the string that we want to encrypt or decrypt
    b = get_keys(k)
    #gets the position in the alphabet of each character in the keyword string
    string =""
    #creats an new empty string to add characters to
    for i in range(len(s)):
        #for loop to iterate through lists and strings
        if m == 1:
            #the following statements show what occurs for each mode selected
            string += (shift_char(s[i], b[i]))
        elif m == (0 - 1):
            string += (shift_char(s[i], -b[i]))
        else:
            raise ValueError ("mode not supported")
    return string