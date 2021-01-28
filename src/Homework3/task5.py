lst_ = [1, 2, 3, 1, 4, 5]
new_lst = []
for element in lst_:
    if lst_.count(element) == 1:
        new_lst.append(element)
print(new_lst)
