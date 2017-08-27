#!/usr/bin/python

# Script to plot VDOS using auto-correlation function from lammps calculation

__author__ = "Woosun Jang"
__email__ = "jin890@yonsei.ac.kr"
__status__ = "Developing"
__date__ = "Aug 27, 2017"

import numpy as np


#TODO: currently only supports timestep = 0 & 1 snapshots

# Lammps dump.vel parser
def DumpParser(filename='dump.vel'):
    dic = {}

    with open(filename, 'r') as dump:
        box = []
        nesteddic = {}

        lines = dump.readlines()

        dic['timestep'] = int(lines[1])
        dic['atoms'] = int(lines[3])

        for i in range(3):
            box.append(lines[4 + i].split())

        dic['box'] = np.array(box)

        for i in range(dic['atoms']):
            temp = lines[9 + i].split()
            nesteddic = {'id': temp[0],
                         'type': temp[1],
                         'x': temp[2],
                         'y': temp[3],
                         'z': temp[4],
                         'vx': temp[5],
                         'vy': temp[6],
                         'vz': temp[7],
                         }

            # pos.append([temp[0], temp[1], temp[2], temp[3], temp[4]])
            # vel.append([temp[0], temp[1], temp[5], temp[6], temp[7]])

        dic['data'] = nesteddic

    return dic

def VDOSpost(dicdata):


    return

def Plotter(vacf):
    return

if __name__ == "__main__":
    # main()
