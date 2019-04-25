import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
class showPlt():
    
    def __init__(self, max_Y, min_Y):
        self.max_Y = max_Y
        self.min_Y = min_Y
    
    def saveFig(self, NSTEPS, ex, hy, *args):
        plt.plot([self.max_Y])
        plt.plot([self.min_Y])
        plt.plot(ex)
        plt.plot(hy)
        for i in args:
            plt.plot(i)
        plt.title("Ex - Green | Hy - Red | Step = "+str(NSTEPS))
        fig = plt.gcf()    
        fig.savefig(str("img"+str(NSTEPS)+".png"))
        plt.close()
    
    
    def showFig(self, ex, hy, *args):
        plt.plot([self.max_Y])
        plt.plot([self.min_Y])
        plt.plot(ex)
        plt.plot(hy)
        for i in args:
            plt.plot(i)
        plt.show()
        plt.close()
    
    def saveFigImageDemo(self, NSTEPS, value, *args):
        fig = plt.gcf()
        ax = Axes3D(fig)
        X = np.arange(0, len(value), 1)
        Z = np.array(value)
        Y = np.arange(0, len(value), 1)
        X, Y = np.meshgrid(X, Y)
        
        ax.plot_surface(X,Y,Z)
        ax.view_init(10, 300)
        #plt.show()
        plt.close()
        ax.set_zbound(-1, 1)
        
        fig.savefig(str("img" + str(NSTEPS) + ".png"))
        
        
        
        
        
        
    