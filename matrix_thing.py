import numpy as np
import matplotlib.pyplot as plt

# Define the number of layers and the number of vectors per layer
num_layers = 3
vectors_per_layer = [8, 12, 16]  # Increasing number of vectors per layer

# Store the original vectors
original_vectors = []

for layer in range(num_layers):
    r = (layer + 1) / num_layers  # Radius of the circle
    theta = np.linspace(0, 2*np.pi, vectors_per_layer[layer], endpoint=False)

    for angle in theta:
        # Compute unit vector components
        dx = np.cos(angle) * 0.2
        dy = np.sin(angle) * 0.2
        x, y = r * np.cos(angle), r * np.sin(angle)  # Position on the circle
        
        # Store as (tail_x, tail_y, head_x, head_y)
        original_vectors.append([x, y, x + dx, y + dy])

# Convert to a NumPy array
original_vectors = np.array(original_vectors)

# Define a transformation matrix
transformation_matrix = np.array([[1, -0.5], [0.5, 1]])  # Example shear transformation

# Apply the transformation to all vectors
transformed_vectors = []
for vec in original_vectors:
    tail = np.array([vec[0], vec[1]])
    head = np.array([vec[2], vec[3]])
    
    new_tail = transformation_matrix @ tail
    new_head = transformation_matrix @ head
    
    transformed_vectors.append([new_tail[0], new_tail[1], new_head[0], new_head[1]])

# Convert to a NumPy array
transformed_vectors = np.array(transformed_vectors)

# Plot both original and transformed vectors
plt.figure(figsize=(10, 5))

# Plot original vectors
plt.subplot(1, 2, 1)
plt.title("Original Vectors")
ax1 = plt.gca()
ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-1.5, 1.5)
ax1.set_aspect('equal')
ax1.axis('off')

for vec in original_vectors:
    plt.arrow(vec[0], vec[1], vec[2]-vec[0], vec[3]-vec[1], head_width=0.05, head_length=0.05, color='red')

# Plot transformed vectors
plt.subplot(1, 2, 2)
plt.title("Transformed Vectors")
ax2 = plt.gca()
ax2.set_xlim(-1.5, 1.5)
ax2.set_ylim(-1.5, 1.5)
ax2.set_aspect('equal')
ax2.axis('off')

for vec in transformed_vectors:
    plt.arrow(vec[0], vec[1], vec[2]-vec[0], vec[3]-vec[1], head_width=0.05, head_length=0.05, color='blue')

plt.show()
  