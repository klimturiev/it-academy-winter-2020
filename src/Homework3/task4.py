str_ = '1 1 1 4 1 1'
list_ = str_.split()
dict_ = {element: list_.count(element) for element in list_}
for key, value in dict_.items():
    if value > 1:
        number_of_pairs = value * (value - 1) / 2
        print('Number of pairs', key, ':', int(number_of_pairs))
