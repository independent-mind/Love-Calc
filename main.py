print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1_name2 = (name1 + name2).lower()

t = name1_name2.count("t")
r = name1_name2.count("r")
u = name1_name2.count("u")
e = name1_name2.count("e")
count_true = t + r + u + e

l = name1_name2.count("l")
o = name1_name2.count("o")
v = name1_name2.count("v")
e = name1_name2.count("e")
count_love = l + o + v + e

score = int(str(count_true) + str(count_love))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score > 40) and (score < 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

