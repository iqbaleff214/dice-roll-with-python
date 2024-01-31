# dice.py

import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DICE_HEIGHT = len(DICE_ART[1])
DICE_WIDTH = len(DICE_ART[1][0])
DICE_FACE_SEPARATOR = " "

def validate(input):
    if input.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input)
    
    print("Please enter a number between 1 and 6.")
    raise SystemExit(1)
    
def roll_dice(num_dice):
    result = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        result.append(roll)
    
    return result

def show_dice(dice_values):
    dice_images = []
    for dice_value in dice_values:
        dice_images.append(DICE_ART[dice_value])

    dice_images_rows = []
    for i in range(DICE_HEIGHT):
        dice_row = []
        for dice in dice_images:
            dice_row.append(dice[i])

        dice_images_rows.append(DICE_FACE_SEPARATOR.join(dice_row))

    header = " RESULTS ".center(len(dice_images_rows[0]), "~")

    return "\n".join([header] + dice_images_rows)

num_dice_input = input("How many dice do you want to roll? [1-6] ")
num_dice = validate(num_dice_input)

print(show_dice(roll_dice(num_dice)))
