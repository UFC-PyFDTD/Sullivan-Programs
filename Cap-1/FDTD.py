import math
import dieletric

class FDTD():
    def __init__(self, dieletrico, showGraphic, KE, NSTEPS):
        self.dieletrico = dieletrico
        self.showGraphic = showGraphic
        self.KE = KE
        self.NSTEPS = NSTEPS
        self.ex = []
        self.hy = []
        self.dic = dict()
    
    def init(self):
        self.ex = [0. for i in range(self.KE)]
        self.hy = [0. for i in range(self.KE)]
        self.dic['ddx'] = .0
        self.dic['dt'] = .0
        self.dic['t0'] = 40.
        self.dic['spread'] = 12.
        self.dic['pulse'] = .0
        self.dic['T'] = 0
        self.dic['ex_low_m1'] = .0
        self.dic['ex_low_m2'] = .0
        self.dic['ex_high_m1'] = .0
        self.dic['ex_high_m2'] = .0
        
    
    def loopFDTD(self):
        while(self.NSTEPS < 10):
            for i in range(1,self.NSTEPS+1,1):
                self.dic['T'] += 1
                for j in range(1,self.KE,1):
                    self.ex[j] = self.ex[j] + self.dieletrico.cb[j]*(self.hy[j-1] - self.hy[j])
                self.dic['pulse'] = math.exp(-.5*(math.pow((self.dic['t0'] - self.dic['T'])/self.dic['spread'],2.0)))
                self.ex[5] = self.ex[5] + self.dic['pulse']
        
                self.ex[0] = self.dic['ex_low_m2']
                self.dic['ex_low_m2'] = self.dic['ex_low_m1']
                self.dic['ex_low_m1'] = self.ex[1]
        
                self.ex[self.KE - 1] = self.dic['ex_high_m2']
                self.dic['ex_high_m2'] = self.dic['ex_high_m1']
                self.dic['ex_high_m1'] = self.ex[self.KE - 2]
                for j in range(0,self.KE-1,1):
                    self.hy[j] = self.hy[j] + .5*(self.ex[j] - self.ex[j+1])
            
            self.showGraphic.saveFig(self.NSTEPS, self.ex, self.hy, self.dieletrico.cb)
            #self.showGraphic.saveFig(self.ex, self.hy, self.dieletrico.cb)
            self.NSTEPS += 1