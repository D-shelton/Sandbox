#GOAL: Create a new character using 5e rules and dicetest.py for rolling
#MILESTONE: Create "character" with name and stats
#TO DO: Build newchar template, set charname func, roll stats
INTRO = "Welcome to Uncle DenDen's 5e Character Creator\n\n[M]ake a new character\n[U]pdate a character\n[Q]Quit\n"
NEWCHAR = {
    "charName": None,
    "charStats": {'str':'8','dex':'8', 'con':'8', 'int':'8', 'wis':'8', 'cha':'8'}
}
def make_char():
    #Get CharName, create CharName dict from empty template
    pass

def main():
    choice = input(INTRO)
    while choice.lower() != "q":
        if choice.lower() == 'm':
            print("\nMaking a character is not supported yet\n")
            choice = input(INTRO)
        if choice.lower() == 'u':
            print("\nUpdating a character is not supported yet\n")
            choice = input(INTRO)
        if choice.lower() == "q":
            print("Thank you")
            exit

    



if __name__ == '__main__':
    main()


