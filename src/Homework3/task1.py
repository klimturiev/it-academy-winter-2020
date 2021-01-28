"""
Программа, которая печатает цифры от 1 до 100,
но вместо чисел, кратных 3 пишет Fizz,
вместо чисел кратный 5 пишет Buzz,
а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""

for ele in range(1, 101):
    if not ele % 3:
        if not ele % 5:
            print('FizzBuzz')
        else:
            print('Fizz')
    elif not ele % 5:
        print('Buzz')
    else:
        print(ele)
