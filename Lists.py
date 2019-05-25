orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']

new_orders = orders + ['lilac', 'iris']

prices = [5, 3, 4, 5, 4] + [4]

print(prices)
print(new_orders)

list1 = range(5, 15, 3) #returns [5, 8, 11, 14]
print(list(list1))
list2 = range(0,40,5)
print(list(list2)) #returns [0, 5, 10, 15, 20, 25, 30, 35]

first_names = ['Ainsley','Ben' , 'Chani', 'Depak']

age = []

age.append(42)

all_ages = age + [32, 41, 29]

name_and_age = zip(first_names,all_ages)

ids = range(4)

print(list(name_and_age))


