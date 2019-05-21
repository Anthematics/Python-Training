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

def graduation_mailer(gpa,credits):
  if gpa >= 2.0 or credits >= 120:
    return True

  def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  elif (gpa >= 2.0) and (credits < 120):
    return "You do not have enough credits to graduate."
  elif (gpa < 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if (gpa < 2.0) and (credits <120):
    return "You do not meet either requirement to graduate!"
  
