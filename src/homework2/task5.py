# 5 task: count n number of Fibonacci
fib_element = 1
fib_number1 = 1
fib_number2 = 1
fib_sum = 0
if fib_element == 1 or fib_element ==2:
    fib_sum = 1
for el in range(fib_element-2):
    fib_sum = fib_number1 + fib_number2
    fib_number1 = fib_number2
    fib_number2 = fib_sum
print(fib_sum)