import numpy as np
from scipy.constants import g
import object

class Ball(object.Move_obj):
    def __init__(self,init_pos,init_vel,init_time = 0, gravity_dir = -np.array([0,1]),radius = 1,mass = 1):
        self.init_pos = init_pos
        self.init_vel = init_vel
        self.init_time = init_time
        self.gravity_dir = g*gravity_dir
        self.radius = radius
        self.mass = mass

    def calc_motion(self,t):
        return (self.init_pos + self.init_vel*(t - self.init_time) + 1/2*self.gravity_dir*(t - self.init_time)**2,\
                self.init_vel + self.gravity_dir*(t - self.init_time))
