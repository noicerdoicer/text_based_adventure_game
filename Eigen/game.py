import sys
import os



# Constant Variables

# Door Colors
DOOR_ONE = "red"
DOOR_TWO = "blue"

# Enemies
ENEMY_RED_DOOR = "a red Dragon"


def main():
    player_name = input("Whats your Name ? >")
    what = "knight"

    print(f'Your name is {player_name}. You are a {what}')
    start_adventure()


##### ROOMS #####
def red_door_room():
    print(f'You have picked the {DOOR_ONE} Door.')

    print(f'There you see {ENEMY_RED_DOOR}.')
    print("It stares at you through one narrowed eye.")
    print("Do you flee for your life or stay?")

    next_move = input("What do you want to do ? >")

    if "flee" in next_move:
        print("Your are back at the beginning of the adventure.")
        os.system('cls')  # Clears the console
        start_adventure()
    else:
        print("It eats you. Well, that was tasty!")

        print("Game over")
        # Opens soundfile in windows audioplayer
        #os.system("start C:\\Users\\Simon\\Documents\\GitHub\\text_based_adventure_game\\Sounds\\Peter.mp3")
        print("Game will be closed.")
        os.system('cls')  # Clears the consolePeter
        sys.exit()


### END ROOMS ###


def blue_door_room():
    message = f'You have picked the {DOOR_TWO} Door.'
    return message


def start_adventure():
    print(
            f'There are two doors. One is {DOOR_ONE} [1], the other is {DOOR_TWO} [2]')
    door_pick = int(input("Which door (Color) do you want to pick ? >"))

    if door_pick == 1:
        red_door_room()
    elif door_pick == 2:
        blue_door_room()
    else:
        print("Something went wrong")


if __name__ == '__main__':
    main()
