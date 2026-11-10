import sys
import time
import keyboard

from room_manager import load_room

## add to input_manager.py
def restart():
    """Request a game restart."""
    global restart_requested
    restart_requested = True


def show_help():
    """Request the help menu."""
    global help_requested
    help_requested = True

def display_help():
    print("""
HELP INFO

To play this game, use single digit inputs to proceed
through the game.

If you would like to start over at any point press F1
and your choice will be confirmed.

************************************************************

If you would like to go back and alter your choice, press F3.

************************************************************

Like to give feedback or need support?
Email us at amanda92nelson@gmail.com
""")

## keyboard input listeners for help and restart functions
keyboard.add_hotkey('R', restart)
keyboard.add_hotkey('H', show_help)

def teletype_print(text, delay =0.03):
        """Prints to the console character by char"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print() ## print a new line

print(f"\n---------------------------------------------------------------------------------------------------------------------------------------------------------------")
teletype_print("Welcome to ELSWYR: Every path leads somewhere. Not everywhere leads back. \n>> Follow the on screen instructions to play and [ press 'H' at any time for HELP ] \n>> Make your choices wisely...and look to the sky: it could save your life! \n>> To restart at any time, PRESS 'R'", delay = 0.03)
print(f"\n---------------------------------------------------------------------------------------------------------------------------------------------------------------")

## starting room 
current_room = "entrance"
restart_requested = False
help_requested = False

while True:
    
    room = load_room(current_room)

    teletype_print(f"\n--- {room['name']} ---")
    teletype_print(room["description"])

    for index, choice in enumerate(room["choices"], start = 1):
        teletype_print(f"{index}. {choice['text']}")

    selection = input("\nChoose an option: ")
    if not selection.isdigit():
        teletype_print("Please enter a number.")
        continue

    choice_index = int(selection) - 1

    if choice_index < 0 or choice_index >= len(room["choices"]):
        teletype_print("Invalid choice.")
        continue

    choice = room["choices"][choice_index]

    if "next_room" in choice:
        current_room = choice["next_room"]
    elif "action" in choice:
        teletype_print(f"Action selected: {choice['action']}")