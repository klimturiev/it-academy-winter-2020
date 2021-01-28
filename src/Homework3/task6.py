lst_ = [1, 1, 1, 0, 0, 2, 2, 3, 3]

for element in lst_:
    if not element:
        lst_.remove(element)
        lst_.insert(len(lst_), element)
print(lst_)
