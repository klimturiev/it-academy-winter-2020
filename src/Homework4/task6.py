import string
str_ = 'Today I am so happy to see you. And you?'
for ch in string.punctuation:
    str_ = str_.replace(ch, '')
lst_ = str_.split()
set_ = set(lst_)
print(len(set_))
