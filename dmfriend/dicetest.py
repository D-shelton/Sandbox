import random
STATS = ["str","dex","con","int","wis","cha"]
NUM_STATS = 6

def find_method():
    method = input(
        "Please select the method you wish to use to roll stats.\n"
        "[1] 3d6\n"
        "[2] 4d6 drop lowest\n"
        "[3] Mighty 3d6 - 1 guaranteed 6 per stat\n"
        )
    if method == '1':
        result = roll_straight()
        return result

    if method == '2':
        result = roll_4d6()
        return result

    if method == '3':
        result = roll_mighty3d6()
        return result
       
def roll_dice(num, sides):
    #dice roll function, rolls {num}D{sides}, returns list of rolls
    rolled_nums = []
    for i in range(num):
        roll = random.randint(1, sides)
        rolled_nums.append(roll)
    return rolled_nums

def assign_value(rolled_stats):
    available_stats = STATS
    returned_stats = {}
    available_rolls = rolled_stats
    for i in range(0, len(rolled_stats)):
        print(f"Your available rolls are {available_rolls}")
        current_stat = input("Which stat would you like to set?\n")
        while available_rolls:
            if current_stat in available_stats:
                print(f"Your available rolls are {available_rolls}")
                current_val = input("Which number would you like to assign?\n" )
                while current_val:
                    if current_val in available_rolls:
                        returned_stats[current_stat] = current_val
                        available_rolls.pop(current_val)
                        available_stats.pop(current_stat)
                        current_val = False
                    else: 
                        print(f"Your available rolls are {available_rolls}")
                        current_val = input("Which number would you like to assign?\n" )
            else:
                print(f"Your available rolls are {available_rolls}")
                current_stat = input("Which stat would you like to set?\n")
    return returned_stats


def roll_straight():
    #rolls stats straight in a row, D&D1e method
    statblock = []
    fullroll = []
    for i in range(NUM_STATS):
        dice_roll = roll_dice(3, 6)
        total_roll = sum(dice_roll)
        statblock.append(total_roll)
        fullroll.append(dice_roll)
    print(f"Your rolls were {fullroll}\n")
    return statblock

def roll_4d6():
    #modern roll 4d6 drop 1 method
    statblock = []
    fullroll = []
    for i in range(NUM_STATS):
    #rolls stats equal to NUM_STATS
        dice_roll = roll_dice(4, 6)
        lowest = 21
        for roll in dice_roll:
        #here down searches for lowest roll, removes it from the pool
            if roll < lowest:
                lowest = roll
        if lowest in dice_roll:
            dice_roll.remove(lowest)
        fullroll.append(dice_roll)
        #fullroll shows individual dice in lists divided by roll
        statblock.append(sum(dice_roll))
        #single list with number of rolls equal to NUM_STATS
    print(f"Your rolls were {fullroll}")
    return statblock


def roll_mighty3d6():
    #Roll 2d6+6 for stats, statblock is list of stats, fullroll is individual dice rolls
    statblock = []
    fullroll = []
    for i in range(NUM_STATS):
        dice_roll = roll_dice(2, 6)
        dice_roll.append(6)
        fullroll.append(dice_roll)
        statblock.append(sum(dice_roll))
    print(f"Your rolls were {fullroll}")
    return statblock

def main():
    method = input(
        "Welcome to Uncle DenDen's D&D Stat roller.\n"
        "Please select the method you wish to use to roll stats.\n"
        "[1] 3d6 in order\n"
        "[2] 4d6 drop lowest\n"
        "[3] Mighty 3d6\n"
        )

    if method == '1':
        result = roll_straight()
        print(f"You rolled {result}")

    if method == '2':
        result = roll_4d6()
        picked_stats = assign_value(result)
        print(f"You rolled {picked_stats}")

    if method == '3':
        result = roll_mighty3d6()
        picked_stats = assign_value(result)
        print(f"Your stats are {picked_stats}")
    


if __name__ == '__main__':
    main()


