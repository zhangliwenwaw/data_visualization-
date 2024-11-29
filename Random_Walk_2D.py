import numpy as np
import matplotlib.pyplot as plt

# Define the number of steps
num_steps = 5000

# Generate random step distances in x and y directions
step_distances = np.random.uniform(-4, 4, size=(num_steps, 2))

# Calculate cumulative sum of step distances
positions = np.cumsum(step_distances, axis=0)

# Extract x and y coordinates
x = positions[:, 0]
y = positions[:, 1]

# Calculate color map based on number of steps
colors = np.arange(num_steps)

# Plot the random walk
plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, cmap='Blues', linewidths=0.5, alpha=0.7)
plt.scatter(0, 0, color='red', marker='o', label='Starting Point')
plt.scatter(x[-1], y[-1], color='green', marker='o', label='Ending Point')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Two-Dimensional Random Walk')
plt.legend()
plt.grid(True)
plt.show()