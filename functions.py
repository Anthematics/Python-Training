def average(num1,num2):
	 return (num1 + num2) / 2 

#order of operations is important here - num1 + num2 / 2 (without brackets) will fail tests because it won't add first then divide!

def introduction(first_name,last_name):
  return str(last_name) + ',' + ' ' + str(first_name) + ' ' + str(last_name)

print(introduction("James", "Bond"))
print(introduction("Maya", "Angelou"))

# shows that you can return parts of print statements and then run with print.

def square_root(num):
	return num**0.5
print(square_root(16))
print(square_root(100))

# Write your tip function here:
def tip (total,percentage):
	return percentage / 100 * total
  
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

def win_percentage(wins,losses):
  return wins / (wins + losses) * 100

# this function works because in params () wins and losses are 
#added to make the resulting number and multiple * 100 or order of operations would cause an issue
# Write your dog_years function here:
def dog_years(name,age):
	age_as_dog = age*7
	return str(name) + ", you are " + str(age_as_dog) + " years old in dog years" 
# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"
