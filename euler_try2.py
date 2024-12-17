def euler_method(m, g, dt, t_max, vx_init, vy_init):
    # Initial conditions
    x = 0.0
    y = 10.0  # initial height
    vx = vx_init  # initial x-speed
    vy = vy_init  # initial y-speed

    # Lists to store the results
    x_values = [x]
    y_values = [y]

    for t in range(int(t_max / dt)):
        # Update velocities
        vx += 0.0  # assuming no x-acceleration
        vy -= g * dt

        # Update positions
        x += vx * dt
        y += vy * dt

        # Store the results
        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

# Example usage
m = 1.0  # mass of the object
g = 9.81  # acceleration due to gravity
dt = 0.01  # time step
t_max = 10.0  # maximum time
vx_init = 5.0  # initial x-speed
vy_init = 0.0  # initial y-speed

x_values, y_values = euler_method(m, g, dt, t_max, vx_init, vy_init)

# Print the results
for t, (x, y) in enumerate(zip(x_values, y_values)):
    print(f"t = {t * dt:.2f} s: x = {x:.2f} m, y = {y:.2f} m")

