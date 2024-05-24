from mpmath import mp
import time

def calculate_pi(digits):
    mp.dps = digits + 10  # Add extra precision for accurate rounding

    # Chudnovsky algorithm
    pi = mp.mpf(0)
    k = 0
    while True:
        numerator = mp.mpf(((-1)**k) * (mp.fac(6 * k)) * (545140134 * k + 13591409))
        denominator = mp.mpf((mp.fac(3 * k)) * (mp.fac(k)**3) * (640320**(3 * k + 3/2)))
        term = mp.mpf(numerator / denominator)
        pi += term
        if mp.fabs(term) < mp.mpf(1e-100):  # Convergence condition
            break
        k += 1

    pi = 1 / (12 * pi)

    pi_str = str(pi)[:digits+2]  # Convert pi to string and remove the extra precision
    return pi_str

# Get user input for the number of digits
num_digits = int(input("Enter the number of digits to calculate pi: "))

# Calculate pi and measure the execution time
start_time = time.time()
pi_value = calculate_pi(num_digits)
end_time = time.time()
execution_time = end_time - start_time

print("Pi:", pi_value)
print("Calculation time:", execution_time, "seconds")
