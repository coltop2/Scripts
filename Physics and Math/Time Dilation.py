import math

def time_dilation(speed_of_light_fraction, gravity_source_mass, distance_from_center):
    c = 299792458  # Speed of light in m/s
    G = 6.67430e-11  # Gravitational constant in m^3/kg/s^2
    M_earth = 5.972e24  # Mass of Earth in kg

    # Calculate time dilation due to velocity
    time_dilation_velocity = math.sqrt(1 - speed_of_light_fraction**2)

    # Calculate time dilation due to gravity
    mass_of_gravity_source = gravity_source_mass * M_earth

    time_dilation_gravity = math.sqrt(1 - (2 * G * mass_of_gravity_source) / (c**2 * distance_from_center))

    # Calculate total time dilation
    total_time_dilation = time_dilation_velocity * time_dilation_gravity

    return total_time_dilation

# Input from the user
speed_of_light_fraction = float(input("Enter the speed of the object in terms of the speed of light (e.g., 0.5 for half the speed of light): "))
gravity_source_mass = float(input("Enter the mass of the gravitational source relative to Earth's mass (e.g., 1 for Earth's mass): "))
distance_from_center = float(input("Enter the distance from the center of mass to the object (in meters): "))

result = time_dilation(speed_of_light_fraction, gravity_source_mass, distance_from_center)
print(f"The total time dilation is {result:.5f}")
