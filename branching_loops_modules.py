# branching_loops_modules.py
# Tim Ubial

import random

is_raining = False
is_cloudy = True

# If statements
if is_raining:
    print("Bring an umbrella. ☂️")
    print("And your raincoat.")
elif is_cloudy:
    print("Bring a sweater.")
else:
    print("Enjoy the sun.")

# For loops
"""There are two main ways to iterate using a for loop.
* iterate over a collection (lists, sets, dictionaries)
* iterate a specific number of times"""

# - Create a list of 10 random numbers
random_nums = []

for _ in range(10):
    random_nums.append(random.randint(0, 100))

# functionally equivalent to the above
random_nums = [random.randint(0, 100) for _ in range(10)]

# - For each number in random_nums, print it out
for number in random_nums:
    print("*", number)

# Add up all numbers inside random_nums
sum_list = 0
for number in random_nums:
    sum_list = sum_list + number
print("The sum of all nums in list is:", sum_list)

sum_list = sum(random_nums)
print(sum_list)

# While loops
"""While loops will loop until the condition is false."""

# Ask the user what 1 + 1 is
user_answer = input("What's 1 + 1? ").strip()

while user_answer != "2" and user_answer != "10":
    print(user_answer == "2")
    print("\nSorry, that's incorrect.")
    user_answer = input("What's 1 + 1? ").strip()

print("You got it!")

# Repeat something n amount of times (n = 100)
n = 100
counter = 0

while True:
    print(f"Iteration: {counter}")
    counter = counter + 1

    if counter > 99:
        break