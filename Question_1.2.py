"""
1.2 Write a function filter_long_words() that takes a list of words and an 
integer n and returns the list of words that are longer than n.

""" 

# Using Function
def filter_long_words(lst_of_words,num):
    
    l1=[]
    txt= lst_of_words.split(" ")
    for i in txt:
        if len(i) > num:
            l1.append(i)
    return l1


lst_of_words = input("Enter the Words in String Format: ")
num = int(input("Enter the length of the words you need: "))

longer_words = filter_long_words(lst_of_words,num)

print(longer_words)



# Using Filter and lamda function

def filter_long_words(str,num):
    return filter(lambda x: len(x)>num, str)

longer_words = filter_long_words(["The", "quick","brown","fox","jumps","over","the","lazy","dog"],3)

print(list(longer_words))