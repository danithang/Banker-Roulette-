# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random_length = len(names)
random_name = random.randint(0, random_length -1)
meal_buyer = names[random_name]

print(meal_buyer + " is going to buy the meal today!")



