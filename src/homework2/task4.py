# 4 task: to count the number of uppercase and lowercase letters in the sentence
my_str = ' LoVE Violence FreeDom'
uppercase_letter = 0
lowercase_letter = 0
for ch in my_str:
    if ch.isupper():
        uppercase_letter += 1
    if ch.islower():
        lowercase_letter += 1
print('Sentence contain:', uppercase_letter, 'uppercase letters and',
      lowercase_letter, 'lowercase letters')
