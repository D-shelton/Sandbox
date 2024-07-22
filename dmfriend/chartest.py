from dicetest import *
#GOAL: Create a new character using 5e rules and dicetest.py for rolling
#MILESTONE: Create "character" with name and stats
#TO DO: Build newchar template, set charname func, roll stats
INTRO = "Welcome to Uncle DenDen's 5e Character Creator\n\n[M]ake a new character\n[U]pdate a character\n[Q]Quit\n"
NEWCHAR = {
    "charName": None,
    "charStats": {'str':'8','dex':'8', 'con':'8', 'int':'8', 'wis':'8', 'cha':'8'}
}
STATS = ['str', 'dex', 'con', 'int', 'wis', 'cha']


def make_char():
    char_name = input("\nPlease name your character: ")
    current_char = NEWCHAR
    current_char['charName'] = char_name
    stat_block = find_method()
    for i in range(0, len(stat_block)):
        current_char['charStats'][STATS[i]] = stat_block[i]
    print(current_char)
    return current_char

def main():
    choice = input(INTRO)
    while choice.lower() != "q":
        if choice.lower() == 'm':
            make_char()
            choice = input(INTRO)
        if choice.lower() == 'u':
            print("\nUpdating a character is not supported yet\n")
            choice = input(INTRO)
        if choice.lower() == "q":
            print("Thank you")
            exit

    



if __name__ == '__main__':
    main()


