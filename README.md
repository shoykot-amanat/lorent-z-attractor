# Lorenz Attractor Simulation

This project simulates the Lorenz Attractor using the Runge-Kutta 4th order method for solving differential equations. The code generates a 3D animation of the trajectories of points starting from different initial conditions.

## Features

- Computes the Lorenz Attractor trajectories using RK4 method.
- Visualizes the trajectories in a 3D plot.
- Creates an animation of the trajectories.
- Saves the animation as a GIF file.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/lorenz-attractor.git
    cd lorenz-attractor
    ```

2. Install the required packages:

    ```bash
    pip install numpy matplotlib
    ```

## Usage

To run the Lorenz Attractor simulation and visualize the trajectories, execute the following steps:

1. **Initialize the LorenzAttractor class:**

    ```python
    from lorenz_attractor import LorenzAttractor

    lorenz = LorenzAttractor()
    ```

2. **Compute the trajectories:**

    ```python
    lorenz.compute_trajectories()
    ```

3. **Animate the trajectories:**

    ```python
    lorenz.animate()
    ```

4. **Save the animation as a GIF file (optional):**

    ```python
    lorenz.save_animation()
    ```

## Code Overview

### LorenzAttractor Class

- **`__init__(self, sigma=10, rho=23, beta=8/3, dt=0.01, duration=4, n=10)`**:
  Initializes the Lorenz Attractor with given parameters.
  
- **`rk4singlestep(self, fun, dt, t0, y0)`**:
  Performs a single step of the 4th order Runge-Kutta method.
  
- **`lorenz(self, t, y)`**:
  Defines the Lorenz system of differential equations.
  
- **`initialize_conditions(self)`**:
  Initializes the initial conditions for the simulation.
  
- **`compute_trajectories(self)`**:
  Computes the trajectories of the Lorenz Attractor over time.
  
- **`setup_plot(self)`**:
  Sets up the 3D plot for animation.
  
- **`update(self, frame)`**:
  Updates the plot for each frame of the animation.
  
- **`animate(self)`**:
  Creates and shows the animation.
  
- **`save_animation(self)`**:
  Saves the animation as a GIF file.

## Example

Here is a complete example of how to use the `LorenzAttractor` class:

```python
from lorenz_attractor import LorenzAttractor

# Create an instance of the LorenzAttractor
lorenz = LorenzAttractor()

# Compute the trajectories
lorenz.compute_trajectories()

# Animate the trajectories
lorenz.animate()

# Save the animation as a GIF
lorenz.save_animation()
