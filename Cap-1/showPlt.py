import matplotlib.pyplot as plt
class showPlt():
    
    def __init__(self, max_Y, min_Y):
        self.max_Y = max_Y
        self.min_Y = min_Y
    
    def saveFig(self, NSTEPS, ex, hy, cb):
        plt.plot([self.max_Y])
        plt.plot([self.min_Y])
        plt.plot(ex)
        plt.plot(hy)
        plt.plot(cb)
        plt.title("Ex - Green | Hy - Red | Dieletric Blue | Step = "+str(NSTEPS))
        fig = plt.gcf()    
        fig.savefig(str("img"+str(NSTEPS)+".png"))
        plt.close()
    
    def showFig(self, ex, hy, cb):
        plt.plot([self.max_Y])
        plt.plot([self.min_Y])
        plt.plot(ex)
        plt.plot(hy)
        plt.plot(cb)
        plt.show()
        plt.close()