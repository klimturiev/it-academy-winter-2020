# 3 task: delete similar symbols and remove spaces from the string
str_ = ' abc bcd cde def '
my_str = str_.replace(' ', '')
str_without_repeats = ''
for ch in my_str:
    if ch not in str_without_repeats:
        str_without_repeats += ch
print(str_without_repeats)
