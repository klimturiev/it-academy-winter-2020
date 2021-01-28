letters = 'abcd'

"""
Генератор списков, чтобы получить
следующий список: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
"""
list_ = [x + y for x in letters[:2] for y in letters[1:]]
print(list_)

# Получить следующий список от исходного: ['ab', 'ad', 'bc']
new_list = list_[::2]
print(new_list)


new_list2 = [str(el) + 'a' for el in range(1, 5)]
print(new_list2)

print(new_list2.pop(1))

list_copy = new_list2[:].append('2a')
