
"""
making a python program that prints out a word if its a palindrome(meaning the word and its reverse are the same)

"""
from load_words import load

words =[x.lower().strip('\n') for x in load('/usr/share/dict/words')] 
pal =[]
for word in words:
    reverse = word[::-1]
    if reverse == word and len(word)>1:
        pal.append(word)

print(pal)