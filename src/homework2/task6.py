# 6 task: define if is a number palindrome or not
number = 12321
number_of_digits = 0
counter = 0
divisible = number
while divisible:
    number_of_digits += 1
    divisible = divisible // 10
for el in range(number_of_digits // 2):
    if (number // (10**el)) % 10 == \
            (number // 10**((number_of_digits - 1) - el)) % 10:
        counter += 1
if counter == number_of_digits // 2:
    print('palindrome')
else:
    print('not palindrome')
