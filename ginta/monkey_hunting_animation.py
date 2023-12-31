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


def axis(xmin, xmax, ymin, ymax):
    """
    determine the axis from the calculation results
    """
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
    flag_try = True
    while flag_try:
        print("determine the axis \nif you want default-axis, enter 'default' on all inputs")
        xmin = input("Minimum value on x-axis[m]:")
        xmax = input("Max value on x-axis[m]:")
        ymin = input("Minimum value on y-axis[m]:")
        ymax = input("Max value on y-axis[m]:")
        
        try:
            float(xmin), float(xmax), float(ymin), float(ymax)
            if xmin < xmax and ymin < ymax:
                print("axis is determined correctly! \n")
                flag_try = False
            else:
                print("type the numbers correctly again! \n")
        
        except:
            if xmin == "default": 
                xlist = [d[1] for d in list] + [d[3] for d in list]
                ylist = [d[2] for d in list] + [d[4] for d in list]
                xmin, xmax = math.floor(min(xlist)-r_monkey), math.ceil(max(xlist)+r_monkey)
                ymin, ymax = math.floor(min(ylist)-r_monkey), math.ceil(max(ylist)+r_monkey)
                print("axis is determined correctly! \n")
                flag_try = False
            else:
                print("type the numbers correctly again! \n")

    fig, ax = axis(float(xmin), float(xmax), float(ymin), float(ymax))
    artist_list = []
    flag_legend = True

    for i in range(len(list)):
        time = list[0]
        x_bullet, y_bullet = list[i][1], list[i][2]
        x_monkey, y_monkey = list[i][3], list[i][4]

        circle_bullet = patches.Circle(xy=(x_bullet, y_bullet), radius=r_monkey/10, color="blue", label="bullet", alpha=0.5)
        artist1 = ax.add_patch(circle_bullet)
        circle_monkey = patches.Circle(xy=(x_monkey, y_monkey), radius=r_monkey, color="red", label="monkey", alpha=0.5)
        artist2 = ax.add_patch(circle_monkey)
        artist_list.append([artist1] + [artist2])

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
    make_animation(data_list, interval=500, r_monkey=0.5)

check()