# Lab Exercise 16: Dice Simulator using random module
import random

def roll_dice(num_dice=1):
    return [random.randint(1, 6) for _ in range(num_dice)]

# ---- Repeated rolls with user choice ----
while True:
    n = int(input("How many dice to roll? "))
    result = roll_dice(n)
    print("You rolled:", result, "| Total:", sum(result))
    again = input("Roll again? (y/n): ").lower()
    if again != "y":
        break

# ---- Frequency analysis (single die, many trials) ----
trials = 6000
frequency = {face: 0 for face in range(1, 7)}

for _ in range(trials):
    frequency[random.randint(1, 6)] += 1

print(f"\nFrequency after {trials} rolls:")
for face, count in frequency.items():
    print(f"Face {face}: {count} times ({count / trials * 100:.2f}%)")

print("\nExpected probability for each face = 1/6 = 16.67%")