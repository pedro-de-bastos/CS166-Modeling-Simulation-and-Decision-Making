import matplotlib
matplotlib.use('TkAgg')
from pylab import *
import matplotlib.pyplot as plt

n = 100 # size of space: n x n
p = 0.1 # probability of initially panicky individuals

def initialize():
    global config, nextconfig
    global density
    density = []
    config = zeros([n, n])
    for x in range(n):
        for y in range(n):
            config[x, y] = 1 if random() < p else 0
    nextconfig = zeros([n, n])
    
def observe():
    global config, nextconfig
    global density
    density.append(np.sum(config)/(n*n))
    cla()
    subplot(1, 2, 1)
    imshow(config, vmin = 0, vmax = 1, cmap = cm.binary)
    subplot(1, 2, 2)
    plot(range(len(density)), density)

def update():
    global config, nextconfig
    for x in range(n):
        for y in range(n):
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    count += config[(x + dx) % n, (y + dy) % n]
            if config[x, y] == 0 and count == 3:
                nextconfig[x, y] = 1
            elif config[x, y] == 1 and count in [2, 3]:
                nextconfig[x, y] = 1
            else:
                nextconfig[x, y] = 0
    config, nextconfig = nextconfig, config

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])