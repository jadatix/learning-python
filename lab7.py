from itertools import count
from math import sin
import matplotlib.pyplot as plt
import numpy as np
import re


if __name__ == "__main__":
    # x = np.linspace(-3,3,100)
    # y = (np.power(2,x))*np.sin(10*x)
    # plt.plot(x, y)
    # plt.savefig('graph.png', dpi=200)

    # ------------------------------

    # str = "abcdeasdwsda"
    # l = list(str)
    # plt.hist(l, bins=len(set(l)), edgecolor='black', histtype='bar',color='red')
    # plt.savefig('barchart_letters.png', dpi=200)

    #-------------------------------

    str = "U're crazy. R u shure about that? Sure! Oh, u stupid asf... U 2."
    dots = str.count("...")
    mod = str.replace("..."," ")
    mod = re.sub("[A-Z a-z2',]",'',mod)
    bins = list(mod)
    for i in range(0,dots):
        bins.append("...")
    plt.hist(bins,bins=len(bins)-1, edgecolor='black', histtype='bar')
    plt.savefig('sentences.png', dpi=200)
