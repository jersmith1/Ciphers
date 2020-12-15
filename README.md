# Ciphers
Mcgill Comp202 A2-Part2

Question 2: Ciphers (60 points)
Caesar’s cipher is a very well known and simple encryption scheme. The point of an encryption scheme is to transform a message so that only those authorized will be able to read it. Caesar’s cipher conceal a message by replacing each letter in the original message, by a letter corresponding to a certain number of letters to the right on the alphabet. Of course the message can be retrieved by replacing each letter in the encoded message (the ciphertext) with the letter corresponding to the same number of position to the left on the alphabet. To achieve this, the cipher has a key that needs to be kept private. Only those with the key can encode and decode a message. Such a key determines the shift that needs to be performed on each letter. For example, here is how a string containing the entire alphabet will be encrypted using a key equal to 3:
Original: abcdefghijklmnopqrstuvwxyz Encrypted: defghijklmnopqrstuvwxyzabc
Vigen`ere’s cipher is a slightly more complex encryption scheme, also used to transform a message. The key of this cipher consists of a word and the cipher works by applying different shifts to the letters in the message based on the letter of the keyword. Each letter can be associated with a number corresponding to its position in the English alphabet (starting to count from 0). For instance, the letter ‘a’ is associated to 0, ‘c’ to 2, and ‘z’ to 25. Therefore, the keyword of the cipher will provide as many integers as letters in the word and these integers will be used to implement different shifts. Let’s see how: suppose the message to encrypt is “elephants” and the keyword is “rats”. The first thing to do is to repeat the keyword until its length matches the one of the message.
Message: e l e p h a n t s Keyword: r a t s r a t s r
Now, each letter of “ratsratsr” is associated to both a letter in the message and an integer. We can encrypt each letter of the message using a shift that corresponds to the integer associated to it through the keyword. In this case ‘r’ corresponds to 17, so the first letter of the message which is an ‘e’ will be encrypted using a ‘v’, the second letter ‘l’ as an ‘l’ since ‘a’ is associated to 0, and so on. The entire message will be encrypted as “vlxhyaglj”.
The goal of this exercise is to write two modules with several functions in order to create a program that encodes and decodes messages using Caesar’s and Vigen`ere’s ciphers.
The helper functions
Let’s start by creating a module called crypto helpers which contains several helper functions that we need to use to implement the ciphers. At the beginning of the file, create a global variable as follows:
   ALPHABET = ‘abcdefghijklmnopqrstuvwxyz’
Note that we used all caps for the name of the variable because this is meant to represent an constant in your program.
For full marks, all the following functions must be part of this module:
• in_engl_alpha: This function takes a string as input and returns true if this is a non-empty string containing only characters from the English alphabet, false otherwise. Note that this function should not be case sensitive. For example,
        >>> in_engl_alpha(‘a’)
        True
        >>> in_engl_alpha(‘G’)
        True
        >>> in_engl_alpha(‘cat’)
        True
        >>> in_engl_alpha(‘cats and dogs’)
        False
 Page 8
>>> in_engl_alpha(‘@’) False
>>> in_engl_alpha(‘`e’) False
• shift_char: This function takes a string representing a single character as input, and an integer n. The function should verify that the string received represents a single character, if not a ValueError with the appropriate error message should be raised. Otherwise, if the character is a letter of the English alphabet, the function returns the lower case letter which appears n position later in the alphabet. If the character received as input is not a letter of the English alphabet, the function returns the character itself with no modification. For example,
  >>> shift_char(‘a’, 3)
  ‘d’
  >>> shift_char(‘z’, 2)
  ‘b’
  >>> shift_char(‘A’, -2)
  ‘y’
  >>> shift_char(‘@’, 12)
  ‘@’
  >>> shift_char(‘g’, 86)
  ‘o’
  >>> shift_char(‘cat’, 5)
  Traceback (most recent call last):
  ValueError: the input string should contain a single character
• get_keys: This function takes a string as input and returns an list of integers. The elements of the list correspond to the position (counting from 0) of each character in the string as a letter of the English alphabet. If the string received as input is a non-empty string containing characters other than letters from the English alphabet, then the function should raise a ValueError with the appropriate error message. For example,
  >>> get_keys(‘hello’)
  [7, 4, 11, 11, 14]
  >>> get_keys(‘AbC’)
  [0, 1, 2]
  >>> get_keys(‘’)
  []
  >>> get_keys(‘c@t’)
  Traceback (most recent call last):
  ValueError: the input string must contain only characters from the English alphabet.
• pad_keyword: This function takes as input a string and an integer n. It returns a string of length n obtained by concatenating characters of the input string together until the desire length is matched. Note that n can be smaller than the length of the input string. If the input string is empty, the function raise a ValueError with the appropriate message. For example,
  >>> pad_keyword(‘cat’, 10)
  ‘catcatcatc’
  >>> pad_keyword(‘artichoke’, 5)
  ‘artic’
Page 9

The ciphers
Let’s now create a module called ciphers. In this module you will write the functions that implement the Caesar’s and the Vigen`ere’s cipher. To do so, make sure to import the crypto helpers module so that you can use the helper functions listed above.
For full marks, all the following functions must be part of this module:
• caesar: This function takes as input a string (the message to encrypt/decrypt), a integer k (the key of the cipher), and another integer m representing the mode (encrypt/decrypt). If m is 1 the function will be encrypting the message, if instead it is −1 the function will be decrypting the message. If it has any other value, the function raises a ValueError indicating that no other mode is supported. This function returns a string obtained by encrypting or decrypting (depending on m) the message received as input using the Caesar’s cipher with key k. For example,
    >>> caesar(‘abc’, 10, 1)
    ‘klm’
    >>> caesar(‘wtaad’, 15, -1)
    ‘hello’
    >>> caesar(‘apple’, -2, 1)
    ‘ynnjc’
    >>> caesar(‘cats and dogs’, 5, 1)
    ‘hfyx fsi itlx’
    >>> caesar(‘hello’, 11, 5)
    Traceback (most recent call last):
    ValueError: mode not supported
• vigenere: This function takes as input a string representing the message to encrypt/decrypt, another string representing the key of the cipher, and an integer m representing the mode (encrypt or decrypt). If m is 1 the function will be encrypting the message, if instead it is −1 the function will be decrypting the message. If it has any other value, the function raises a ValueError indicating that no other mode is supported. This function returns a string obtained by encrypting or decrypting (depending on m) the message received as input using the Vigen`ere’s cipher with key received as input. Go back at the beginning of this section to review how Vigen`ere’s cipher works. Note that this function will raise an error if the string representing the key is empty. For example,
    >>> vigenere(‘BaNAna’, ‘apple’, 1)
    ‘bpclra’
    >>> vigenere(‘bpclra’, ‘apple’, -1)
    ‘banana’
    >>> vigenere(‘elephants and hippos’, ‘rats’, 1)
    ‘vlxhyaglj tfu aagphk’
    >>> vigenere(‘vlxhyaglj tfu aagphk’, ‘RATS’, -1)
    ‘elephants and hippos’
    >>> vigenere(‘hello’, ‘cat’, 5)
    Traceback (most recent call last):
    ValueError: mode not supported
 Page 10
