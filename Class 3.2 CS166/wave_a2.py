# Simple CA simulator in Python
#
# *** Forest fire ***
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

# Modified to run with Python 3

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP

RD.seed()

width = 300
height = 300
initProb = 0.01
qui, excited, refrac = range(3)

def init():
    global time, config, nextConfig
    global excited_prop
    excited_prop = []

    time = 0

    config = SP.zeros([height, width])
    for x in range(width):
        for y in range(height):
            if RD.random() < initProb:
                state = excited
            else:
                state = qui
            config[y, x] = state

    nextConfig = SP.zeros([height, width])

def draw():
    PL.cla()
    PL.subplot(1, 2, 1)
    PL.pcolor(config, vmin = 0, vmax = 2, cmap = PL.cm.binary)
    PL.axis('image')
    PL.title('t = ' + str(time))

    global excited_prop
    excited_prop.append(SP.sum(config==1)/(width*height))
    PL.subplot(1, 2, 2)
    PL.plot(range(len(excited_prop)), excited_prop)
    PL.show()

def step():
    global time, config, nextConfig

    time += 1

    for x in range(width):
        for y in range(height):
            state = config[y, x]
            if state == excited:
                state = refrac
            elif state == refrac:
                state = qui
            elif state == qui:
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if config[(y+dy)%height, (x+dx)%width] == excited:
                            if RD.random() > (1/3):
                                state = excited
            nextConfig[y, x] = state

    config, nextConfig = nextConfig, config

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])