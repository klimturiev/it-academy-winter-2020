# 1 task: define total price of goods

roubles = 15
coins = 125
number_of_goods = 15
total_coins = (number_of_goods * coins) % 100
total_roubles = (number_of_goods * roubles) + (number_of_goods * coins) // 100
print(total_roubles, 'roubles', total_coins, 'coins')
