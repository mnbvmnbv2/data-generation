# %%
import matplotlib.pyplot as plt
import numpy as np


# %%
# Random walk 1d
def random_walk_y(size: int, visualize: bool = False):
    y_diff = np.random.randint(-3, 4, size)
    y = np.cumsum(y_diff)

    if visualize:
        plt.plot(y)
        plt.show()

    return y


# %%
# Random walk 1d scaled
def random_walk_y_scaled(size: int, visualize: bool = False):
    # Set the range of the random walk
    min_value = -10
    max_value = 10

    # Initialize the random walk with a starting position
    random_walk = [0]

    # Generate the random walk
    for _ in range(size):
        # Generate a random step
        step = np.random.randint(low=-1, high=2)

        # Calculate the scaling factor
        scale = 1 - abs(random_walk[-1] - min_value) / (max_value - min_value)

        # Scale the step
        step = step * scale

        # Update the position
        random_walk.append(random_walk[-1] + step)

    if visualize:
        # Plot the random walk
        plt.plot(random_walk)

        # Show the plot
        plt.show()

    return random_walk


# %%
# Randomwalk 2d
def random_walk_xy(size: int, visualize: bool = False):
    x_diff = np.random.randint(-4, 4, size)
    y_diff = np.random.randint(-4, 4, size)

    x = np.cumsum(x_diff)
    y = np.cumsum(y_diff)

    if visualize:
        plt.plot(x, y)
        plt.show()

    return x, y


# %%
random_walk_xy(100, visualize=True)
