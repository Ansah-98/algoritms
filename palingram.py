from load_words import load 
import cProfile
word_list= [x.lower().strip('\n') for x in load('/usr/share/dict/words')]
words = set(word_list)
def palingram():
    pal = []
    for word in word_list:
        end = len(word)

        rev_word =word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:]in word_list:
                    pal.append((word,rev_word[end-i]))
                if word[:i] ==rev_word[end-1:] and rev_word[:end-i]in word_list:
                    pal.append((rev_word[:end-i],word))

    return pal

palingrams = palingram()
sorted_palingrams = sorted(palingrams)
print(f"number of palingrams {len(sorted_palingrams)}")

for first,second in sorted_palingrams:
    print(first,second)