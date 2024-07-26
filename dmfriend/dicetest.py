import random
STATS = ['str', 'dex', 'con', 'int', 'wis', 'cha']

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

def assign_stats(rolled_stats):
    final_stats = []
    used_stats = []
    print(f"Your available stat choices are {rolled_stats}\n")
    while len(rolled_stats) != 0:
        currentStat = input("Which stat would you like to assign? ")
        if currentStat.lower() in STATS:
            used_stats.append(currentStat)
            pickedStat = input("Which roll would you like to apply?")
            if pickedStat in rolled_stats:
                pass
                #apply the stat to its location and send it

    #this is a temp plan, maybe use while stats in rolled_stats instead
    #ask "which stat would you like to update"
    #assign stat to that index place (make list of indexed stats?)
    #output should be an ordered stat block in order of STR DEX CON INT WIS CHA
    #output is currently a list, change to dict or rely on list order?

def roll_straight():
    #rolls stats straight in a row, D&D1e method
    statblock = []
    fullroll = []
    for i in range(len(STATS)):
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
    for i in range(len(STATS)):
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
    statblock = assign_stats(statblock)
    #assign_stats(statblock) will take the statblock and let the user assign values to stats
    return statblock


def roll_mighty3d6():
    #Roll 2d6+6 for stats, statblock is list of stats, fullroll is individual dice rolls
    statblock = []
    fullroll = []
    for i in range(len(STATS)):
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
        print(f"You rolled {result}")

    if method == '3':
        result = roll_mighty3d6()
        print(f"You rolled {result}")
    


if __name__ == '__main__':
    main()


