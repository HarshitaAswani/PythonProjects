def start_adventure():
    print("Welcome to the Text Adventure Game!")
    print("You are on a quest to find the hidden treasure in a mysterious cave.")
    print("You enter the cave and find yourself in a dark tunnel.")
    print("There are two paths ahead of you: left and right.")

    choice = input("Which path will you choose? (left/right): ").lower()

    if choice == "left":
        print("You chose the left path and encounter a giant spider!")
        fight_or_flee("spider")
    elif choice == "right":
        print("You chose the right path and discover a locked door.")
        open_door()
    else:
        print("Invalid choice. Please choose 'left' or 'right'.")
        start_adventure()

def fight_or_flee(enemy):
    choice = input("Do you want to 'fight' or 'flee' the {}? ".format(enemy)).lower()

    if choice == "fight":
        if enemy == "spider":
            print("You bravely fight the giant spider and defeat it.")
            print("You continue deeper into the cave.")
            treasure_room()
    elif choice == "flee":
        print("You choose to flee from the {} and return to the tunnel.".format(enemy))
        start_adventure()
    else:
        print("Invalid choice. Please choose 'fight' or 'flee'.")
        fight_or_flee(enemy)

def open_door():
    print("You try to open the locked door, but it won't budge.")
    print("You notice a hidden switch nearby.")
    choice = input("Will you 'press' the switch or 'return' to the tunnel? ").lower()

    if choice == "press":
        print("You hear a clicking sound, and the door unlocks.")
        treasure_room()
    elif choice == "return":
        print("You decide not to mess with the switch and return to the tunnel.")
        start_adventure()
    else:
        print("Invalid choice. Please choose 'press' or 'return'.")
        open_door()

def treasure_room():
    print("You enter a magnificent treasure room filled with gold and jewels!")
    print("Congratulations! You have found the hidden treasure.")
    print("You have successfully completed the adventure.")

if __name__ == "__main__":
    start_adventure()

