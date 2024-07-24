from dicetest import *
#GOAL: Create a new character using 5e rules and dicetest.py for rolling
#MILESTONE: Choose any of the three methods to create a new character
#TO DO: apply remaining roll methods to character creation, build stat assignment functions
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
            char = make_char()
            again = input("\nWould you like to make another character? Y/N: ")
            if again.lower() == 'n':
                choice = 'q'



        if choice.lower() == 'u':
            choice = input("\nUpdating a character is not supported yet, type [m] to make a character and [q] to quit \n")
        if choice.lower() == "q":
            print("Thank you")
            exit

    



if __name__ == '__main__':
    main()


