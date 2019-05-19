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

