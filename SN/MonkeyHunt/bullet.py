import numpy as np
from scipy.constans import g
import object

class Ball(Move_obj):
    def __init__(self,init_pos,init_vel,gravity_dir = np.array([0,1]),radius = 1):
        self.init_pos = init_pos
        self.init_vel = init_vel
        self.gravity_dir = gravity_dir

    def calc_motion(self,t):
        return self.init_vel*t + 1/2*g*t**2*gravity_dir