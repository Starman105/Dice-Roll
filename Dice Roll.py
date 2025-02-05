# roll dice 6 times and track how many times we got each number
import random


counts = [0] * 6

times = int(input("Enter the number of times you want to roll the dice: "))

for _ in range(times):
    roll = random.randint(1, 6)
    counts[roll - 1] += 1

print(f"{'Number':<10}{'Count':<10}")
print("-" * 20)
for i in range(6):
    print(f"{i + 1:<10}{counts[i]:<10}")

print("You rolled the dice" , times , "times")