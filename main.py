import random
a = "Andrew"
print("Hello " + a)

age = 13
if age > 12:
  print("teen")
else:
  print("preteen")
age = random.randint(10,20)
if age > 12 and age < 20:
  print("teen")
elif age == 20:
  print("not teen")
else:
  print("preteen")