#!/usr/bin/python

#The following statements are used to import numpy and matplotlib.
import numpy as np
import matplotlib.pyplot as plt


# TODO fill in this function
def integrate(y, dxx):
    return np.trapz(y,dx=dxx)
    pass

def plotTest():
    x = np.arange(0,np.pi,0.01)
    y = sin(x)
    plt.plot(x,y)


# TODO write code here to setup arrays x and y = sin(x) and then plot them.
# fter this is done implement your integrate function above integrate y
