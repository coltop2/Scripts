import math
import locale

# Set the locale for adding commas to numbers
locale.setlocale(locale.LC_ALL, '')

def calculate_collision_time(mass1, mass2, distance):
    gravitational_constant = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)

    # Calculate the force of attraction between the objects
    force = gravitational_constant * (mass1 * mass2) / distance**2

    # Calculate the acceleration of the objects
    acceleration = force / mass1

    # Calculate the time taken for collision in seconds
    time_seconds = math.sqrt(2 * distance / acceleration)

    # Convert time to years
    time_years = time_seconds / (60 * 60 * 24 * 365.25)

    return time_seconds, time_years

def calculate_velocity(distance, time_seconds):
    # Calculate the velocity given the distance and time
    velocity = distance / time_seconds
    return velocity

# Get user inputs
mass1 = float(input("Enter mass of object 1 (in kg): "))
mass2 = float(input("Enter mass of object 2 (in kg): "))
distance = float(input("Enter initial distance between the objects (in meters): "))

# Calculate the collision time
collision_time_seconds, collision_time_years = calculate_collision_time(mass1, mass2, distance)

# Calculate velocities 0.1 seconds before collision
time_before_collision = collision_time_seconds - 0.1
velocity1 = calculate_velocity(distance, time_before_collision)
velocity2 = calculate_velocity(distance, time_before_collision)

# Format the output with commas for readability
formatted_collision_time_seconds = locale.format_string("%0.2f", collision_time_seconds, grouping=True)
formatted_collision_time_years = locale.format_string("%0.2f", collision_time_years, grouping=True)
formatted_velocity1 = locale.format_string("%0.2f", velocity1, grouping=True)
formatted_velocity2 = locale.format_string("%0.2f", velocity2, grouping=True)

print(f"The objects will collide in approximately {formatted_collision_time_seconds} seconds "
      f"({formatted_collision_time_years} years).")
print(f"Object 1 will be traveling at {formatted_velocity1} m/s 0.1 seconds before collision.")
print(f"Object 2 will be traveling at {formatted_velocity2} m/s 0.1 seconds before collision.")
