"""
2.2 Write a Python function which takes a character (i.e. a string of length 1) 
and returns True if it is a vowel, False otherwise.

"""
def vowels(char):

    if (char == "a" or char =="e" or char =="i" or char =="o" or char =="u" 
       or char =="A" or char =="E" or char =="I" or char =="O" or char =="U"):
        return True
    else:
        return False
    

char=input("Enter the character:")
vowels_words = vowels(char)

if vowels_words == True:
    print(char,"- The Entered character is a vowel")
else:
    print(char, "- The Entered character is not a vowel")

