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

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", 'poetry', 'history']

grades = [98,97,85,88]

subjects.append("computer science")

grades.append(100)

gradebook = list(zip(subjects,grades)) # if you write it as zip(subjects,grades) it will no longer be a list object to be added to hence the list(zip(var1,var2)) format

gradebook.append(("visual arts", 93))

print(list(gradebook))

print(list(range(2,14,4))) # start at 2 , add 4 , this gives us 6 , add 4 to that giving us 10. 14 doesn't show as lists start@zero.

employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']

index4 = employees[4]

print(index4)
print(len(employees))
print(employees[5])

# messing with length attributes.

# SLICING

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

beginning = suitcase[0:4]
middle = suitcase [2:4]
print(beginning,middle)

# you can slice negative indexes as well as positive ones

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']


start = suitcase[0:3]
print(start)

# above prints 'shirt' , 'shirt' , 'pants'

end = suitcase[-2:]
print(end)
# above prints 'pajamas', 'books'

 votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count('Jake')

print(jake_votes)

#Prints 9 , one for each instance of 'Jake' in the list

#SORTING 

### Exercise 1 & 2 ###
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']

# Sort addresses here:

### Exercise 3 ###
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()
print(names)

### Exercise 4 ###
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

sorted_cities = cities.sort()
sorted_addresses = addresses.sort()

print(cities)

print(sorted_cities,sorted_addresses) 
# why does cities sort and print properly . but sorted cities doesn't?

# A second way of sorting a list is to use sorted. sorted is different from .sort() in several ways:
# It comes before a list, instead of after.
# It generates a new list.
# The sorted method seems better for functional programming purposes.

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

games_sorted = sorted(games)
print(games_sorted)
print (games)
