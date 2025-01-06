G = 6.67 * (10 ** -11)  # Gravitational constant 
M = 6.0 * (10 ** 24)    # Mass of Earth
m = 7.34 * (10 ** 22)   # Mass of the moon
r = 3.84 * (10 ** 8)    # Distance between Earth and the moon

# Write your code here
grav_force = (G*M*m)/(r**2)
print(grav_force)