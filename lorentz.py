import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import time

class LorenzAttractor:
    def __init__(self, sigma=10, rho=23, beta=8/3, dt=0.01, duration=4, n=10):
        self.sigma = sigma
        self.rho = rho
        self.beta = beta
        self.dt = dt
        self.duration = duration
        self.n = n
        self.num_steps = int(duration / dt)
        self.initialize_conditions()
        self.compute_trajectories()

    def rk4singlestep(self, fun, dt, t0, y0):
        f1 = fun(t0, y0)
        f2 = fun(t0 + dt / 2, y0 + dt / 2 * f1)
        f3 = fun(t0 + dt / 2, y0 + dt / 2 * f2)
        f4 = fun(t0 + dt, y0 + dt * f3)
        yout = y0 + dt / 6 * (f1 + 2 * f2 + 2 * f3 + f4)
        return yout

    def lorenz(self, t, y):
        dy = [
            self.sigma * (y[1] - y[0]),
            y[0] * (self.rho - y[2]) - y[1],
            y[0] * y[1] - self.beta * y[2]
        ]
        return np.array(dy)

    def initialize_conditions(self):
        xvec = np.linspace(-10, 10, self.n)
        yvec = np.linspace(-10, 10, self.n)
        zvec = np.linspace(-10, 10, self.n)
        x0, y0, z0 = np.meshgrid(xvec, yvec, zvec)
        self.yIC = np.zeros((3, self.n**3))
        self.yIC[0, :] = x0.reshape(self.n**3)
        self.yIC[1, :] = y0.reshape(self.n**3)
        self.yIC[2, :] = z0.reshape(self.n**3)

    def compute_trajectories(self):
        self.y_single_steps = np.zeros((3, self.num_steps, self.n**3))
        yin = self.yIC
        start_time = time.time()
        for step in range(self.num_steps):
            tstep = step * self.dt
            yout = self.rk4singlestep(self.lorenz, self.dt, tstep, yin)
            yin = yout
            self.y_single_steps[:, step, :] = yout
        end_time = time.time()
        print('Elapsed time is', end_time - start_time)

    def setup_plot(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(projection='3d')
        self.ax.set_xlim([-20, 20])
        self.ax.set_ylim([-20, 20])
        self.ax.set_zlim([-20, 20])
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.colors = plt.cm.jet(np.linspace(0, 1, self.n**3))
        self.scatter = self.ax.scatter(self.y_single_steps[0, 0, :], 
                                       self.y_single_steps[1, 0, :], 
                                       self.y_single_steps[2, 0, :], 
                                       c=self.colors, s=5)
        self.trail_length = 20

    def update(self, frame):
        start = max(0, frame - self.trail_length)
        self.scatter._offsets3d = (self.y_single_steps[0, frame, :], 
                                   self.y_single_steps[1, frame, :], 
                                   self.y_single_steps[2, frame, :])
        self.ax.view_init(elev=30 + frame / 5, azim=frame % 360)
        self.ax.set_title(f'Trajectories from Different Initial Conditions\nTime: {frame * self.dt:.2f}s')
        return self.scatter,

    def animate(self):
        self.setup_plot()
        self.ani = FuncAnimation(self.fig, self.update, frames=self.num_steps, blit=False, interval=30, repeat=True)
        plt.show()

    def save_animation(self):
        self.ani.save('lorentz_attractor.gif', writer='pillow', fps=30)
