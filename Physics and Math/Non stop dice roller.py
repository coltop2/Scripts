import random
from datetime import datetime
import time


def roll_dice(num_rolls, num_sides):
    return sorted([random.randint(1, num_sides) for _ in range(num_rolls)])


def main():
    start_time = time.time()  # Capture the start time

    dice_input = input("Enter the dice roll in the format XdY: ")
    num_rolls, num_sides = map(int, dice_input.split('d'))

    target_value = int(input("Enter the target value: "))

    rolls_count = 0
    while True:
        rolls_count += 1
        roll_result = roll_dice(num_rolls, num_sides)
        total = sum(roll_result)

        # Print each roll result
        print(f"Roll {rolls_count}: {roll_result}")

        if total == target_value:
            break

    end_time = time.time()  # Capture the end time
    elapsed_time = end_time - start_time  # Calculate elapsed time
    print(f"Target value {target_value} reached in {rolls_count} rolls.")
    print(f"Processing took {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
