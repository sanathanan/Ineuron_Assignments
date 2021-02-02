"""
2.1 Write a Python program using function concept that maps list of words 
into a list of integers representing the lengths of the corresponding words.
Hint: If a list [ ab,cde,erty] is passed on to the python function output should 
come as [2,3,4]Here 2,3 and 4 are the lengths of the words in the list.

"""

def len_of_words(words):
    txt = words.split(",")
    l1=[]
    for i in txt:
        l1.append(len(i))
    return l1


words=input("Enter the words: ")
words_length= len_of_words(words)
print(words_length)