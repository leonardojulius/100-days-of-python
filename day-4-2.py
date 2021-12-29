import random

#seed_number=input("Create a seed number:")
#random.seed(seed_number)

names_string = input("Give me everybody's names, separated by a comma. ").split(", ")

print(f"{names_string [random.randint(0,len(names_string)-1)]} is going to buy the meal today!")
