import random
a = "Andrew"
print("Hello " + a)


age = random.randint(1,100)
if age > 12 and age < 20:
  print("teen")
elif age >= 20 and age < 65:
  print("adult")
elif age >= 65:
  print("senior")
else:
  print("preteen")