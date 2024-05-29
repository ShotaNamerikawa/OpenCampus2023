import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import patches
import numpy as np


class Animation:
    """
    make animation from position function.

    Attributes
    ----------
    calc_func(function):: function returning landing time, hitting time, and motion of monkey and bullet.
                          Be careful about order of arguments and returned values!
    vx_bullet:: x component of initial velocity of bullet.
    l_monkey:: x component of relative position vector from bullet to monkey.
    l_monkey:: y component of relative position vector from bullet to monkey.
    r_monkey:: radius of monkey.
    m_bullet:: mass of bullet.
    m_monkey:: mass of monkey.
    t_land:: landing time of bullet or monkey.
    t_hit:: hitting time of bullet and monkey.
    """
    def __init__(self, calc_func, vx_bullet, vy_bullet, l_monkey,
                 h_monkey, r_monkey, m_bullet, m_monkey, dt=0.05, interval=10, t_max=6):
        self.calc_func = calc_func
        self.vx_bullet = vx_bullet
        self.vy_bullet = vy_bullet
        self.l_monkey = l_monkey
        self.h_monkey = h_monkey
        self.r_monkey = r_monkey
        self.r_bullet = 1/10*self.r_monkey
        self.m_bullet = m_bullet
        self.m_monkey = m_monkey
        self.dt = dt
        self.interval = interval
        self.t_hit = -1
        self.t_land = -1
        self.p = []
        self.t_max = t_max
        self.plot()

    def _update(self, t):
        if len(self.p) > 0:
            for i in range(2):
                self.p.pop(0).set_visible(False)
        self.t_land, self.t_hit, x_bullet, y_bullet, x_monkey, y_monkey = self.calc_func(t, self.t_land, self.t_hit,
                                                                                         self.vx_bullet, self.vy_bullet,
                                                                                         self.l_monkey, self.h_monkey,
                                                                                         self.r_monkey, self.m_bullet,
                                                                                         self.m_monkey)
        if self.hit != 2:  # update only when the bullet and the monkey is above ground.
            self.x_bullet = x_bullet
            self.y_bullet = y_bullet
            self.x_monkey = x_monkey
            self.y_monkey = y_monkey
        self.ax.plot(self.x_monkey, self.y_monkey, "o", c="red", alpha=0)[0]
        circle_bullet = patches.Circle(
            xy=(self.x_bullet, self.y_bullet), radius=self.r_bullet, color="blue", alpha=0.5)
        circle_monkey = patches.Circle(
            xy=(self.x_monkey, self.y_monkey), radius=self.r_monkey, color="orange", alpha=0.5)
        self.p.append(self.ax.add_patch(circle_bullet))
        self.p.append(self.ax.add_patch(circle_monkey))

    def plot(self):
        self.t_hit = -1
        self.hit = 0
        self.p = []
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal')
        self.anim = FuncAnimation(self.fig, self._update, np.arange(0, self.t_max, self.dt), 
                                  blit=False, interval=self.interval)  # time scale 0.01s is too slow!
        self.anim.save("monkey_hunt.gif", writer="imagemagick")
        plt.close()
