import csv
import time
import locale
import os
import socket

def find_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

def generate_csv(start_number, folder_path):
    hostname = socket.gethostname()
    file_name = f"{user_input}_to_1_Divisors_{hostname}.csv"
    file_path = os.path.join(folder_path, file_name)
    start_time = time.time()
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f"{user_input}_to_1 Divisors"])
        writer.writerow(['Number', 'Total Divisors', 'Divisors'])
        while start_number >= 1:
            divisors = find_divisors(start_number)
            formatted_number = locale.format_string('%d', start_number, grouping=True)
            writer.writerow([formatted_number, len(divisors)] + divisors)
            print(f"Found {len(divisors)} divisors for {formatted_number}")
            start_number -= 1
    end_time = time.time()
    duration = end_time - start_time
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines[0] = f"{user_input}_to_1 Divisors\n"
    lines.insert(1, f"Process took {duration:.5f} seconds\n")
    with open(file_path, 'w') as file:
        file.writelines(lines)

    print(f"\n{user_input}_to_1 Divisors")
    print(f"Process took {duration:.5f} seconds")

# Get user input
user_input = input("Enter a starting number: ")

# Validate user input
while not user_input.isdigit():
    print("Invalid input. Please enter a valid number.")
    user_input = input("Enter a starting number: ")

# Convert user input to an integer
start_number = int(user_input)

# Prompt for folder path
folder_path = input("Enter the folder path to save the CSV file: ")

# Create the folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

# Format numbers with comma separators
locale.setlocale(locale.LC_ALL, '')

# Generate CSV with divisors
generate_csv(start_number, folder_path)
