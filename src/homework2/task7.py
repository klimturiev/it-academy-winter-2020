# 7.1 task: Given an integer number, perform the following conditional actions:
# If number is odd, print Weird
# If number is even and in the inclusive range of 2 to 5, print Not Weird
# If number is even and in the inclusive range of 6 to 20, print Weird
# If number is even and greater than 20, print Not Weird
number = int(input())
if number % 2:
    print('Weird')
else:
    if 2 <= number <= 5:
        print('Not Weird')
    elif 5 < number < 21:
        print('Weird')
    else:
        print('Not Weird')


# 7.2 task: define if is a year leap or not
def is_leap(leap_year):
    leap = False
    if not leap_year % 4:
        leap = True
        if not leap_year % 100:
            leap = False
            if not leap_year % 400:
                leap = True
    return leap


year = int(input())
print(is_leap(year))


# 7.3 task: You are given  words. Some words may repeat.
# For each word, output its number of occurrences.
# The output order should correspond
# with the input order of appearance of the word.
number = int(input())
list_ = []
res_list = []
counter = 0
for el in range(number):
    word = input()
    list_.append(word)
res_list = set(list_)
my_dict = {el: list_.count(el) for el in list_}
dict_values = (my_dict.values())
print(len(res_list))
print(*dict_values, sep=' ')
