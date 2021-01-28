list_ = ['a', 'b', 'c']
tuple_ = tuple(list_)
print(tuple_)

_tuple = ('a', 'b', 'c')
_list = list(_tuple)
print(_list)

a, b, c = 'a', 2, 'python'

tpl_ = ('123',)
for element in tpl_:
    print(list(element))
print(len(tpl_))
