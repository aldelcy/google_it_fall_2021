#!/usr/bin/env python3

print("Welcome to Treasure Island. Your mission is to find the treasure!")

left_or_right = input("You're at a crossroad, where would you like to go? Left or Right. ").lower()

colors_choice = {
    "blue"   : "Game Over. You've wondered your way into a volcano.",
    "red"    : "Game Over. Rabbid beasts took your body away.",
    "yellow" : "You win! You've found the treasure!",
    "green"  : "Game Over. You were attacked by a flock of angry brids."
}

if left_or_right == "right":
    print("Game Over. You fell off a cliff.")
elif left_or_right == "left":
    swim_or_wait = input("\n" + "You arrive at the marina where the island is within view" +
    "\n" + "but there are no boats. Do you swim or wait? ").lower()
    if swim_or_wait == "swim":
        print("Game Over. The water was piranha infested...")
    elif swim_or_wait == "wait":
        which_door = input("\n" + "A boat arrives and you head to the island." + "\n" +
        "You arrive at the island where there are 3 doors. Which do you take? " + ", ".join(colors_choice.keys()) + ":" ).lower()
    print( colors_choice[which_door] )
