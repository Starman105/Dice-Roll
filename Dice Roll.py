# roll dice 6 times and track how many times we got each number
import random

Total_rolls = 0

Count_one = 0
Count_two = 0
Count_three = 0
Count_four = 0
Count_five = 0
Count_six = 0

times = int(input("Enter the number of times you want to roll the dice: "))

input("Press Enter to roll the dice " + str(times) + " times")
for i in range(times):
    roll = random.randint(1,6)
    Total_rolls += 1
    if roll == 1:
        Count_one += 1
    elif roll == 2:
        Count_two += 1
    elif roll == 3:
        Count_three += 1
    elif roll == 4:
        Count_four += 1
    elif roll == 5:
        Count_five += 1
    elif roll == 6:
        Count_six += 1

print("Total rolls: ", Total_rolls)
print("Count of 1: ", Count_one)
print("Count of 2: ", Count_two)
print("Count of 3: ", Count_three)
print("Count of 4: ", Count_four)
print("Count of 5: ", Count_five)
print("Count of 6: ", Count_six)