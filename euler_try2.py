import pandas as pd

print("Try 1")
# Constants
m = 68.1                      # Mass of the object (kg)
C_d = 0.8                     # Drag coefficient (dimensionless)
A = 0.6                       # Cross-sectional area (m²)
rho = 1.29                   # Air density (kg/m³)
g = 9.81                      # Gravitational acceleration (m/s²)
d_t = 0.1                     # Time step (s)
t_max = 100                   # Total simulation time (s)

# Initial conditions
x = 0                         # Initial position in x (m)
y = 0                         # Initial position in y (m)
v_x = 10                      # Initial velocity in x (m/s)
v_y = 0                       # Initial velocity in y (m/s)

# Time initialization
t = 0

# Initialize DataFrame to store results
data = pd.DataFrame(columns=["t", "x", "y", "v_x", "v_y"])

# Simulation loop
while t <= t_max:
    # Compute air resistance forces
    v = (v_x**2 + v_y**2)**0.5            # Total velocity magnitude
    F_air_x = 0.5 * C_d * rho * A * v_x * abs(v_x)  # Drag in x-direction
    F_air_y = 0.5 * C_d * rho * A * v_y * abs(v_y)  # Drag in y-direction
    
    # Compute accelerations
    a_x = -F_air_x / m                    # Acceleration in x (air resistance opposes motion)
    a_y = -g - (F_air_y / m)              # Acceleration in y (gravity + air resistance)
    
    # Update velocities (Explicit Euler)
    v_x += a_x * d_t                      # Update velocity in x
    v_y += a_y * d_t                      # Update velocity in y
    
    # Update positions (Explicit Euler)
    x += v_x * d_t                        # Update position in x
    y += v_y * d_t                        # Update position in y
    
    # Store results
    data = data._append({"t": t, "x": x, "y": y, "v_x": v_x, "v_y": v_y}, ignore_index=True)
    
    # Print output for current time step
    print(f"t: {t:.2f} s, x: {x:.2f} m, y: {y:.2f} m")
    
    # Increment time
    t += d_t

# Save results to Excel file
data.to_excel("falling_object_simulation.ods", engine="odf", index=False)
