import numpy as np
import numpy.linalg
import ball
import itertools

class Motion:
    def __init__(self,obj_list,time_mesh,e = 1, ndim = 2):
        self.obj_list = obj_list
        self.time_mesh = time_mesh
        self.e = e
        self.ndim = ndim
    
    def calc_motion(self):
        """
        calculate ball objects motion.
        """
        positions = np.zeros([len(self.obj_list),self.time_mesh.shape[0], self.ndim]) 
        min_dist = [obj_pair[0].radius + obj_pair[1].radius for \
                    obj_pair in itertools.combinations(self.obj_list,2)]
        index_pair = list(itertools.combinations(np.arange(len(self.obj_list)),2))
        for (i,time) in enumerate(self.time_mesh):
            pos_list = np.array([obj.calc_motion(time)[0] for obj in self.obj_list])
            rel_pos = np.array([ pos_pair[0] - pos_pair[1] for pos_pair in itertools.combinations(pos_list,2)])
            rel_dist = np.linalg.norm(rel_pos,axis=1)
            #check whether crash happened.
            crash = np.arange(len(index_pair))[(rel_dist < min_dist)] 
            positions[:,i,:] = pos_list 
            if crash.shape[0] == 0:
                continue
            else:
                if crash.shape[0] > 1:
                     print("three body crash happend! but only one pair will be considered") #Fixme
                crash_pair = index_pair[crash[0]]
                self.bound_process(self.obj_list[crash_pair[0]], self.obj_list[crash_pair[1]],time ,self.e)  
        return positions, self.time_mesh

    def bound_process(self, obj1, obj2, time, e):
        self.bounce(obj1, obj2, time, e)
        print("hit!")
        print(obj1.init_vel)
        print(obj2.init_vel)
    
    def bounce(self, obj1, obj2, time, e):
        """bounce
        calculate velocity after bounce
        """
        pos1, before_vel1 = obj1.calc_motion(time)
        pos2, before_vel2 = obj2.calc_motion(time)

        vert_dir = (pos1 - pos2)/np.linalg.norm(pos1-pos2)
        vert_vel12 = np.dot(vert_dir, before_vel1 - before_vel2)*vert_dir
        M = obj1.mass + obj2.mass
        obj1.set_init_value(pos1,before_vel1 - (1+e)*obj2.mass/M*vert_vel12 ,time)
        obj2.set_init_value(pos2,before_vel2 + (1+e)*obj1.mass/M*vert_vel12 ,time)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    bullet = ball.Ball(np.zeros([2]),np.array([10,10]),mass = 1, radius = 0.1)
    monkey = ball.Ball(np.array([10,10]),np.array([0,0]),mass = 10, radius = 0.1)#np.array([50,50]), np.array([0, 0]),mass = 100)
    ball_obj_list = [bullet,monkey]
    time_mesh = np.arange(0,2,0.001)
    print(time_mesh)
    motion = Motion(ball_obj_list, time_mesh,e = 0.2)
    positions,time_mesh = motion.calc_motion()
    print(positions)
    print("bullet orbit")
    fig,ax = plt.subplots()
    ax.plot(positions[0, :, 0], positions[0, :, 1],label="bullet")
    ax.plot(positions[1, :, 0], positions[1, :, 1],label="monkey")
    ax.set_xlabel("x [m]")
    ax.set_ylabel("y [m]")
    plt.show()
    fig, ax = plt.subplots()
    ax.plot(time_mesh, positions[0, :, 0], label="bullet")
    ax.plot(time_mesh, positions[1, :, 0], label="monkey")
    ax.set_xlabel("time [sec]")
    ax.set_ylabel("x [m]")
    fig, ax = plt.subplots()
    ax.plot(time_mesh, positions[0, :, 1], label="bullet")
    ax.plot(time_mesh, positions[1, :, 1], label="monkey")
    ax.set_xlabel("time [sec]")
    ax.set_ylabel("y [m]")
    plt.show()
