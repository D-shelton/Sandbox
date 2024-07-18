import random

def roll_dice(num, sides):
    rolled_nums = []
    for i in range(num):
        roll = random.randint(1, sides)
        rolled_nums.append(roll)
    return rolled_nums

num = int(input("how many dice are you rolling?"))
sides = int(input("how many sides does this die have"))

result = roll_dice(num, sides)

print(f"You rolled {result}")
