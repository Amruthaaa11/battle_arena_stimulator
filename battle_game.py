# Battle Arena Simulator
# Day 28 Project: Automated Game Battle System

import time
import random

# Dice roll function
def roll_dice(sides):
    return random.randint(1, sides)

# Health calculation
def health_check():
    return ((roll_dice(6) * roll_dice(12)) / 2) + 10

# Strength calculation
def strength_check():
    return ((roll_dice(6) * roll_dice(8)) / 2) + 12
# Character setup
def create_character(number):
    print(f"\nCharacter {number}")
    name = input(f"Enter name for Character {number}: ")
    strength = strength_check()
    health = health_check()
    print(f"Strength of {name}: {strength}")
    print(f"Health of {name}: {health}")
    return name, strength, health

# Battle logic
def battle(char1, strength1, health1, char2, strength2, health2):
    round_num = 1
    print("\n" + "-" * 30)
    print("Battle Begins")

    while health1 > 0 and health2 > 0:
        print(f"\nRound {round_num}")
        roll1 = roll_dice(6)
        roll2 = roll_dice(6)

        if roll1 > roll2:
            print(f"{char1} wins the round")
            damage = abs(strength1 - strength2)
            health2 -= damage
            print(f"{char2} takes {damage} damage")
        elif roll2 > roll1:
            print(f"{char2} wins the round")
            damage = abs(strength2 - strength1)
            health1 -= damage
            print(f"{char1} takes {damage} damage")
        else:
            print("It's a draw")

        print(f"{char1} Health: {max(health1, 0)}")
        print(f"{char2} Health: {max(health2, 0)}")
        round_num += 1
        time.sleep(2)
        print("*" * 30)

    # Declare winner
    print("\nBattle Ends")
    if health1 > health2:
        print(f"{char1} wins with {health1} health remaining")
    else:
        print(f"{char2} wins with {health2} health remaining")

# Game entry point
if __name__ == "__main__":
    char1, strength1, health1 = create_character(1)
    char2, strength2, health2 = create_character(2)
    battle(char1, strength1, health1, char2, strength2, health2)