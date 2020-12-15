#Jeremy Smith - ID# 260948914

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def in_engl_alpha(s):
    """
    (str) -> bool
    takes a string of any length as input, if each character in the string is also in the variable 'ALPHABET' true is returned, otherwise returns false
    there is no input validation required per the outline
    >>>in_engl_alpha('d')
    True
    >>>in_engl_alpha('pEopLE')
    True
    >>>in_engl_alpha('$ad*')
    False
    >>>in_engl_alpha(' ')
    False
    >>>in_engl_alpha('T')
    True
    """
    #assigns an initial value i before it is used
    for i in range(len(s)):
        #as long as i is less than or equal to the length of the string, the result of the boolean expression will be returned
        s = s.lower()
        if s[i] in ALPHABET:
            return True
        else:
            #when any character is not in the alphabet 
            return False
    #keeps adding 1 to i after each looping to avoid infinite loop and to test each character

def shift_char(s, n):
    """
    (str, int) -> str
    takes a string and an integer as input, verifies that the string is a single character and returns, if the character is in ALPHABET, the lower case letter n spots later in the alphabet
    >>>shift_char('sds',9)
    Traceback (most recent call last):
    ValueError: the input string should contain a single character
    >>>shift_char('a',12)
    'm'
    >>>shift_char('P',3)
    's'
    >>>shift_char('Q',-3)
    'n'
    >>>shift_char('$',17)
    '$'
    >>>shift_char('&&&',5)
    Traceback (most recent call last):
    ValueError: the input string should contain a single character
    """
    s = s.lower()
    #converts the string s into all lowercase
    n = n%len(ALPHABET)
    if (len(s) != 1):
        #when the string is longer than 1 character a Value error will be raised and the program will end
        raise ValueError ("the input string should contain a single character")
    else:
        #what the program runs when no errors are raised
        x = in_engl_alpha(s)
        #x is assigned to the boolean result of in_engl_alpha(s) so the function is not called everytime it is reference
        if (x == True):
            #if the character is in the alphabet we find the index of the character in ALPHABET and add n, this is the index of the new character we are returning
            i = ALPHABET.index(s) + n
            i = i%len(ALPHABET)
            s = ALPHABET[i]
        else:
            #if the character is not in ALPHABET the character itself is returned
            s = s
    return s

def get_keys(s):
    """
    (str)->list (of ints)
    the function takes a string as an input and returns a list of integers corresponding to the position starting from 0 of each character in the string in the english alphabet
    >>>get_keys('jeremy')
    [9, 4, 17, 4, 12, 24]
    >>>get_keys('')
    []
    >>>get_keys('@#f%^&')
    Traceback (most recent call last):
    ValueError: All characters of the input string must be in the alphabet
    >>>get_keys('JeReMy')
    [9, 4, 17, 4, 12, 24]
    """
    s = s.lower()
    #makes all characters in the input string lowercase letters
    i = 0
    #starts the index at 0 so that 'a' the first element of ALPHABET is included
    my_list=[]
    #creates an empty list, the position of each letter in the string in the alphabet will be added to this list and returned once completed
    if in_engl_alpha(s) == False:
        #raises a ValueError when one of the characters in the string is not in the alphabet by calling on the in_engl_alpha function previously defined
        raise ValueError ("All characters of the input string must be in the alphabet")
    else:
        #what runs when all characters are a part of the english alphabet
        for i in range(len(s)):
            #iterates through the string and appends each corresponding position in the alphabet as an integer in my_list
            my_list.append(ALPHABET.index(s[i]))
            i+=1
        return my_list
        
def pad_keyword(s, n):
    """
    (str, int) -> str
    takes a string and an integer as input and returns a string on n length
    >>>pad_keyword('telephone',4)
    'tele'
    >>>pad_keyword('jay',13)
    'jayjayjayjayj'
    >>>pad_keyword('',4)
    Traceback (most recent call last):
    ValueError: The input string must not be empty
    >>>pad_keyword('hello',-5)
    ''
    """
    if s == "":
        #raises a value error when the input string is empty
        raise ValueError ("The input string must not be empty")
    else:
        #all scenarios where the input string contains one or more character(s)
        if n < len(s):
            #when the string is longer than n only the first n characters are being returned
            return(s[0:n])
        else:
            #when the string is shorter than n characters
            i=0
            while len(s)<n:
                #keeps adding the next charcater of the string until the length of the string is equal to n once they are equal, the new string is returned
                s = s + s[i]
                i+=1
            return s
            