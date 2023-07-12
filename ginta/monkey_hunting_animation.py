import os
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
from  matplotlib.animation import ArtistAnimation


def read_file(path):
    """
    reading file obtained from initial value

    Attributes
    ----------
    data_list: output data obtained from initial value
    data_list[0]: time
    data_list[1]: x-coordidate of bullet
    data_list[2]: y-coordidate of bullet
    data_list[3]: x-coordidate of monkey
    data_list[4]: y-coordidate of monkey
    """
    data_list = []
    with open(path, "r")as f:
        for line in f:
            line_split = list(map(float, line.split()))
            data_list.append(line_split)
    return data_list


def make_list(t, x_bullet, y_bullet, x_monkey, y_monkey):
    return [t, x_bullet, y_bullet, x_monkey, y_monkey]


def axis(list):
    """
    determine the axis from the calculation results
    """
    xlist = [b[1] for b in list] + [b[3] for b in list]
    ylist = [b[2] for b in list] + [b[3] for b in list]
    xmin, xmax = math.ceil(min(xlist)), math.ceil(max(xlist))
    ymin, ymax = math.ceil(min(ylist)), math.ceil(max(ylist))

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.grid()
    return fig, ax


def make_animation(list, interval, r_monkey):
    """
    make gif-picture using matplotlib

    Attributes
    ----------
    r_monkey[m]: radius for monkey
    interval[ms]: time it takes for one picture to be replaced
    """
    fig, ax = axis(list)
    artist_list = []
    flag_legend = True

    for i in range(len(list)):
        time = list[0]
        x_bullet, y_bullet = list[i][1], list[i][2]
        x_monkey, y_monkey = list[i][3], list[i][4]
        artist1 = ax.plot(x_bullet, y_bullet, color="blue", marker="o", markersize=5, label="bullet")
        circle = patches.Circle(xy=(x_monkey, y_monkey), radius=r_monkey, color="red", label="monkey")
        artist2 = ax.add_patch(circle)
        artist_list.append(artist1 + [artist2])

        if flag_legend == True:
            ax.legend()
            flag_legend = False

    anim = ArtistAnimation(fig, artist_list, interval=interval)
    plt.show()



def check():
    """
    check code
    """
    path = os.path.abspath("monkey_hunting.txt")
    data_list = read_file(path)
    make_animation(data_list, interval=300, r_monkey=0.5)

check()