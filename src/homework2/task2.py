# 2 task: define the longest word in the sentence without punctuations marks
import string
str_ = 'asfdfsd, asfqqw,.. qwfqvew'
longest_word = ''
for ch in string.punctuation:
    str_ = str_.replace(ch, '')
new_str = str_.split()
for word in new_str:
    if len(longest_word) < len(word):
        longest_word = word
print(longest_word)
