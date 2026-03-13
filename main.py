from encoding import encode
from analyses import *
from saving import *

characters = ["babytchi", "marutchi", "tamatchi", "kuchitamatchi", "mametchi", "ginjirotchi", "maskutchi", "kuchipatchi", "nyorotchi", "tarakotchi", "oyajitchi", "bill"]
path = "data/"

current_character = None
combinations = []
appearances = [0]*32

symbol_mode = True



def load_save():
    global combinations, appearances
    
    combinations = read_save(path, current_character)
    
    appearances = [0]*32
    for com in combinations:
        appearances[com] += 1
        



#initialising the cycle of inputing left-right combinations
def start_input():
    saved = True
    print("Input combinations of left and right that your tamagotchi chose. You may use 'l' and 'r', '<' and '>' or ',' and '.'")
    print("s - save, x - exit")
    while True:
        string = input("Input combination: ")
        if string == 's':
            save(combinations, path, current_character)
            saved = True
        elif string == 'x':
            if not saved:
                if input("Save (Y/n)? ") != 'n':
                    save(combinations, path, current_character)
            return
        else:
            saved = False
            encoded = encode(string)
            if encoded != -1:
                combinations.append(encoded)
                appearances[encoded] += 1






def change_mode():
    global symbol_mode
    symbol_mode = not symbol_mode
    print("Mode changed!")

#a loop for inputting statistical analysis commands
def analyse():

    print("Statistically significant means here that there's small chance to get such result if all left-right combinations were equally probable. It doesn't prove that they aren't - sample size and reproduction of results is important to reach conclusions.")
    print("")
    print("l - calculate percentage of games where pressing only left would guarantee winning")
    print("a - check how many times each combination appeared")
    print("e - check all combinations that ever appeared")
    print("n - check all combinations that never appeared")
    print("f - check the combination(s) that appeared the most frequently")
    print("m - change display mode (l/r or </>)")
    while True:
        action = input("Choose type of analysis: ")
        match action:
            case 'l':
                left_winning(combinations)
            case 'a':
                statistics(combinations, appearances, symbol_mode)
            case 'e':
                ever_appeared(combinations, appearances, symbol_mode)
            case 'n':
                never_appeared(appearances, symbol_mode)
            case 'f':
                most_frequent(combinations, appearances, symbol_mode)
            case 'm':
                change_mode()
            case 'x':
                return
            case _:
                print("Unrecognised command.")




def set_path():
    global path
    path = input("Input path to files relative to the main program's folder, eg. 'authors-data/': ")
    load_save()




def ask_action():
    while True:
        print("i - input combinations, a - statistial analysis, p - set path to files, x - exit")
        action = input("Choose an action: ")
        match action:
            case 'i':
                start_input()
            case 'a':
                analyse()
            case 'p':
                set_path()
            case 'x':
                return
            case _:
                print("Unrecognised command.")
                ask_action()


def character_prompt() -> str:
    name = input("Enter character name: ")
    if not name in characters:
        print ("Character not found. Available characters are: " + ", ".join(characters) + ". Input is case-sensitive.")
        name = character_prompt()
    return name
    

#setting the program up for a new character
def initialise():
    
    global current_character
    current_character = character_prompt()
    
    load_save()
    
    ask_action()

    if input("Do you want to continue with another character (y/N)? ") == 'y':
        initialise()


initialise()







