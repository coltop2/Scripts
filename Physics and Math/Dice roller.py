import csv
import random
from datetime import datetime
import os
import time


def roll_dice(num_rolls, num_sides):
    return sorted([random.randint(1, num_sides) for _ in range(num_rolls)])


def main():
    start_time = time.time()  # Capture the start time

    dice_input = input("Enter the dice roll in the format XdY: ")
    num_rolls, num_sides = map(int, dice_input.split('d'))
    num_times = int(input("Enter how many times to roll: "))

    current_datetime = datetime.now().strftime("%m.%d.%Y.%H%M%S")
    file_name = f"{current_datetime}.{dice_input}.{num_times}times.csv"

    data_path = input("Enter the directory where you want to save the CSV file: ")
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    file_path = os.path.join(data_path, file_name)

    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for roll_number in range(1, num_times + 1):
            roll_result = roll_dice(num_rolls, num_sides)
            total = sum(roll_result)

            # Print roll number
            print(f"Roll {roll_number}: {roll_result}")

            csv_writer.writerow(roll_result + [total])
            print("Total:", total)

    end_time = time.time()  # Capture the end time
    elapsed_time = end_time - start_time  # Calculate elapsed time
    print(f"Data has been saved to {file_path}")
    print(f"Processing took {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
