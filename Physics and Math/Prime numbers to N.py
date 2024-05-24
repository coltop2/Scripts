import os
import csv
import time
import locale
from datetime import datetime
import socket

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input("Enter a number: "))
data_path = input("Enter the data path: ")

# Set locale to use commas for thousands separator
locale.setlocale(locale.LC_ALL, '')

start_time = time.time()

count = 0
primes = []
for i in range(1, n + 1):
    if is_prime(i):
        count += 1
        primes.append(i)
        print("Found", count)

end_time = time.time()

file_name = "Prime Numbers to {:,}_{hostname}.csv".format(n, hostname=socket.gethostname())
now = datetime.now()
timestamp = now.strftime("%H%M.%m.%d.%Y")
file_path = os.path.join(data_path, "{} {}".format(timestamp, file_name))

if os.path.exists(file_path):
    print("CSV file already exists. Renaming with current timestamp.")

with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["{:n} Prime Numbers found from 1 to {:n}".format(count, n)])
    writer.writerow(["Process took {:.4f} seconds".format(end_time - start_time)])
    writer.writerow(["Number", "Prime", "Difference"])

    previous_prime = 0
    for i, prime in enumerate(primes, 1):
        difference = prime - previous_prime
        writer.writerow([i, prime, difference])
        previous_prime = prime

print("{:n} Prime Numbers found from 1 to {:n}".format(count, n))
print("Process took {:.4f} seconds".format(end_time - start_time))
print("CSV file '{}' created successfully.".format(file_path))
