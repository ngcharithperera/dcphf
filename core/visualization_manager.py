from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as pyplot
import numpy as np
import logging
from core.config import *
#looging
logging.basicConfig(level=LOGGING_LEVEL)

def prepare_data():
    logging.debug("prepare_data")


def plot_charts(filename, x_axiz, y_axiz, z_axiz):
    logging.debug("plot_charts")
    figure_instance = pyplot.figure()
    ax = figure_instance.gca(projection='3d')
    surf = ax.plot_surface(x_axiz, y_axiz, z_axiz, rstride=1, cstride=1, cmap=cm.RdYlGn,
            linewidth=0, antialiased=False)
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    figure_instance.colorbar(surf, shrink=0.5, aspect=5)
    pyplot.savefig(filename + '.png')
