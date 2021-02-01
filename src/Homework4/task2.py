number_of_countries = int(input())
countries = {}
for data in range(number_of_countries):
    country, *cities = input().split()
    for city in cities:
        countries[city] = country
number_of_cities = int(input())
for data in range(number_of_cities):
    city = input()
    print(countries[city])
