import random

input("Hit enter to decide who the next scrum master is")

number = random.randint(1,4)

if number == 1:
	print("Srum master is Robert!")
elif number == 2:
	print("Scrum master is David!")
elif number  == 3:
	print("Scrum master is Paul!")
else:
	print("Scrum master is Tadas!")

input()
