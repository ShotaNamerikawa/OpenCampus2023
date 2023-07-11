import numpy as np

class Move_obj:
    """Move_obj 
    Class to calculate object motion.
    """
    def __init__(self,init_pos,init_vel,init_time = 0, gravity_dir = -np.array([0,1])):
        self.set_init_value(init_pos, init_vel, init_time)
        self.gravity_dir = gravity_dir

    def calc_motion(self,t):
        """
        return (pos,vec)
        """
        print("not implemented!")

    def set_init_value(self,init_pos,init_vel,init_time):
        self.init_pos = init_pos
        self.init_vel = init_vel
        self.init_time = init_time