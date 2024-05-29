import numpy as np
import matplotlib.pyplot as plt

class Plot:
    def __init__(self,orbit_file):
        self.orbit = np.loadtxt(orbit_file)

    def plot_orbit(self):
        fig,ax = plt.subplots()
        ax.plot(self.orbit[:,1],self.orbit[:,2],label = "bullet")
        ax.plot(self.orbit[:,3],self.orbit[:,4],label = "monkey")
        ax.legend()
        ax.set_xlabel("x [m]")
        ax.set_ylabel("y [m]")
        plt.show()

    def plot_x(self):
        fig,ax = plt.subplots()
        ax.plot(self.orbit[:,0],self.orbit[:,1],label = "bullet")
        ax.plot(self.orbit[:,0],self.orbit[:,3],label = "monkey")
        ax.legend()
        ax.set_xlabel("t [ms]")
        ax.set_ylabel("x [m]")
        plt.show()

    def plot_y(self):
        fig,ax = plt.subplots()
        ax.plot(self.orbit[:,0],self.orbit[:,2],label = "bullet")
        ax.plot(self.orbit[:,0],self.orbit[:,4],label = "monkey")
        ax.legend()
        ax.set_xlabel("t [ms]")
        ax.set_ylabel("y [m]")
        plt.show()

if __name__ == "__main__":
    import sys
    file_name = sys.argv[1]
    plotter = Plot(file_name)
    print("orbit")
    plotter.plot_orbit()
    print("x")
    plotter.plot_x()
    print("y")
    plotter.plot_y()
