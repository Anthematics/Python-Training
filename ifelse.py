x=1
y=2

def greater_than(x,y):
  if x == y:
    return "These numbers are the same"
  elif x > y:
    return x
  else:
  	return y
  
print(greater_than(x,y))

def graduation_reqs(credits):
  if credits >= 120:
    return "You have enough credits to graduate!"
  else:
    return "no"
  
print(graduation_reqs(120))
