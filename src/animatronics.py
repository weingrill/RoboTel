#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np

__author__ = "Joerg Weingrill"
__copyright__ = "Copyright 2021 Leibniz-Insitute for Astrophysics Potsdam (AIP)"
__credits__ = ["Joerg Weingrill"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Joerg Weingrill"
__email__ = "jweingrill@aip.de"
__status__ = "Development"
__date__ = "9/8/21"


def stepsim(p_current=0.0, p_new=-1.0, time=8000):
    p_steps = np.zeros(time)
    p_currents = np.zeros(time)
    p_diffs = np.zeros(time)
    p_news = np.full(time, p_new)

    k = 100.0/(np.abs(p_new-p_current)*time)
    for t in range(time):
        p_diff = p_new - p_current
        p_step = k*p_diff * t*t/(time*time)
        p_steps[t] = p_step
        p_currents[t] = p_current
        p_diffs[t] = p_diff
        p_current = p_current + p_step

    ax1.plot(np.arange(time), p_steps*1000.0, label="step")
    ax1.plot(np.arange(time), p_currents, label="current")
    ax1.plot(np.arange(time), p_diffs, label="diff")
    #plt.legend()
    #plt.grid()
    #plt.title('final difference: %f' % (p_new - p_current))


if __name__ == "__main__":
    # using the variable axs for multiple Axes
    #fig, axs = plt.subplots(3, 3)
    v = 0
    for p0 in [-1.0, 90.0]:
        for p1 in [-2.0, 360.0]:
            for times in [1000, 2000, 4000]:
                v = v + 1
                ax1 = plt.subplot(3, 4, v)
                stepsim(p0, p1, times)

    plt.tight_layout()
    plt.savefig('animatronics.png')
    plt.close()