import math
import Materiais

class FDTD():
    def __init__(self, showGraphic, KE, NSTEPS, *material):
        self.material = material
        self.showGraphic = showGraphic
        self.KE = KE
        self.NSTEPS = NSTEPS
        self.ex = []
        self.hy = []
        self.dx = []
        self.ix = []
        self.mag = []
        self.freq = []
        self.arg = []
        self.real_in = []
        self.imag_in = []
        self.amp_in = []
        self.phase_in = []
        self.real_pt = []
        self.imag_pt = []
        self.ampn = []
        self.phasen = []
        self.dic = dict()
        self.dic['ddx'] = .0
        self.dic['dt'] = .0
        self.dic['t0'] = 0.
        self.dic['spread'] = 0.
        self.dic['pulse'] = .0
        self.dic['T'] = 0
        self.dic['ex_low_m1'] = .0
        self.dic['ex_low_m2'] = .0
        self.dic['ex_high_m1'] = .0
        self.dic['ex_high_m2'] = .0
        self.dic['kc'] = 0
    
    def init(self):
        self.ex = [0. for i in range(self.KE)]
        self.hy = [0. for i in range(self.KE)]

        self.dx = [0. for i in range(self.KE)]
        self.ix = [0. for i in range(self.KE)]
        self.mag = [0. for i in range(0,self.KE,1)]
        self.freq = [0. for i in range(0,5,1)]
        self.arg = [.0 for i in range(0,5,1)]
        self.real_in = [0. for i in range(0,5,1)]
        self.imag_in = [0. for i in range(0,5,1)]
        self.amp_in = [0. for i in range(0,5,1)]
        self.phase_in = [0. for i in range(0,5,1)]
        self.real_pt = [[.0 for j in range (0,self.KE,1)] for i in range(0,5,1)]
        self.imag_pt = [[.0 for j in range (0,self.KE,1)] for i in range(0,5,1)]
        self.ampn = [[.0 for j in range (0,self.KE,1)] for i in range(0,5,1)]
        self.phasen = [[.0 for j in range (0,self.KE,1)] for i in range(0,5,1)]
        
        
        self.dic['ddx'] = .0
        self.dic['dt'] = .0
        self.dic['t0'] = 50.
        self.dic['spread'] = 20.
        self.dic['pulse'] = .0
        self.dic['T'] = 0
        self.dic['ex_low_m1'] = .0
        self.dic['ex_low_m2'] = .0
        self.dic['ex_high_m1'] = .0
        self.dic['ex_high_m2'] = .0
        self.dic['kc'] = 25
        for m in range(0, 3, 1):
            self.real_in[m] = self.real_in[m] + math.cos(self.arg[m] * self.dic['T']) * self.ex[10]
            self.imag_in[m] = self.imag_in[m] - math.sin(self.arg[m] * self.dic['T']) * self.ex[10]
    
    def loopFDTD(self):
        loop = 0
        while(loop < self.NSTEPS ):
            for i in range(1,self.NSTEPS+1,1):
                self.dic['T'] += 1
                for j in range(1,self.KE,1):
                    self.dx[j] = self.dx[j] + 0.5*(self.hy[j-1] - self.hy[j])
                self.dic['pulse'] = math.exp(-.5*(math.pow((self.dic['t0'] - (self.dic['T'] - self.dic['t0']))/self.dic['spread'],2.0)))
                self.dx[self.dic['kc']] = self.dx[self.dic['kc']] + self.dic['pulse']
                
                for k in range(1,self.KE-1):
                    self.ex[k] = (self.dx[k] - self.ix[k])
                    for m in self.material:
                        if(m.ga[k] != 1):
                            self.ex[k] = m.ga[k]*(self.dx[k] - self.ix[k])
                            self.ix[k] = self.ix[k] + m.gb[k]*self.ex[k]
                            break
                self.ex[0] = self.dic['ex_low_m2']
                self.dic['ex_low_m2'] = self.dic['ex_low_m1']
                self.dic['ex_low_m1'] = self.ex[1]
        
                self.ex[self.KE - 1] = self.dic['ex_high_m2']
                self.dic['ex_high_m2'] = self.dic['ex_high_m1']
                self.dic['ex_high_m1'] = self.ex[self.KE - 2]
                for j in range(0,self.KE-1,1):
                    self.hy[j] = self.hy[j] + .5*(self.ex[j] - self.ex[j+1])
            
            self.showGraphic.saveFig(loop, self.ex, self.hy, self.material)
            #self.showGraphic.saveFig(self.ex, self.hy, self.material.cb)
            loop += 1
    def loopFDTDFourier(self):
        for i in range(1,self.NSTEPS+1,1):
            self.dic['T'] += 1
            for j in range(1,self.KE,1):
                self.dx[j] = self.dx[j] + 0.5*(self.hy[j-1] - self.hy[j])
            self.dic['pulse'] = math.exp(-.5*(math.pow((self.dic['t0'] - (self.dic['T'] - self.dic['t0']))/self.dic['spread'],2.0)))
            self.dx[25] = self.dx[25] + self.dic['pulse']
            
            for k in range(1,self.KE-1):
                self.ex[k] = (self.dx[k] - self.ix[k])
                for m in self.material:
                    if(m.ga[k] != 1):
                        self.ex[k] = m.ga[k]*(self.dx[k] - self.ix[k])
                        self.ix[k] = self.ix[k] + m.gb[k]*self.ex[k]
                        break
            for k in range(self.KE):
                self.mag[k] = self.mag[k] + math.pow(self.ex[k],2.)
                for m in range(0,5,1):
                    self.real_pt[m][k] = self.real_pt[m][k] + math.cos(self.arg[m]*self.dic['T'])*self.ex[k]
                    self.imag_pt[m][k] = self.imag_pt[m][k] - math.sin(self.arg[m]*self.dic['T'])*self.ex[k]
            if(self.dic['T'] < 100):
                for m in range(0, 3, 1):
                    self.real_in[m] = self.real_in[m] + math.cos(self.arg[m] * self.dic['T']) * self.ex[10]
                    self.imag_in[m] = self.imag_in[m] - math.sin(self.arg[m] * self.dic['T']) * self.ex[10]
            self.ex[0] = self.dic['ex_low_m2']
            self.dic['ex_low_m2'] = self.dic['ex_low_m1']
            self.dic['ex_low_m1'] = self.ex[1]
    
            self.ex[self.KE - 1] = self.dic['ex_high_m2']
            self.dic['ex_high_m2'] = self.dic['ex_high_m1']
            self.dic['ex_high_m1'] = self.ex[self.KE - 2]
            for j in range(0,self.KE-1,1):
                self.hy[j] = self.hy[j] + .5*(self.ex[j] - self.ex[j+1])
            
            self.showGraphic.saveFig(self.NSTEPS, self.ex, self.hy, [i.gb for i in self.material])
        
class FDTD2D(FDTD):
    def __init__(self, material, showGraphic, NSTEPS, kc, IE, JE):
        super().__init__(material, showGraphic, JE, NSTEPS)
        self.IE = IE
        self.JE = JE
        self.ez = []
        self.iz = []
        self.hx = []
        self.ihx = []
        self.ihy = []
        self.gi2 = []
        self.gi3 = []
        self.gj2 = []
        self.gj3 = []
        self.fi1 = []
        self.fi2 = []
        self.fi3 = []
        self.fj1 = []
        self.fj2 = []
        self.fj3 = []
        self.dic['ez_inc_low_m1'] = 0
        self.dic['ez_inc_low_m2'] = 0
        self.dic['ez_inc_high_m1'] = 0
        self.dic['ez_inc_high_m2'] = 0
        self.dic['ic'] = 0
        self.dic['jc'] = 0
        self.dic['ia'] = 0
        self.dic['ib'] = 0
        self.dic['ja'] = 0
        self.dic['jb'] = 0
        self.dic['kc'] = kc
        
                
    def init(self, npml):
        self.dz = [ [0.0 for j in range(self.JE)] for i in range(self.IE)]
        self.ez = [ [0.0 for j in range(self.JE)] for i in range(self.IE)]
        self.iz = [ [0.0 for j in range(self.JE)] for i in range(self.IE)]
        
        self.hx = [ [0.0 for j in range(self.JE)] for i in range(self.IE)]
        self.hy = [ [0.0 for j in range(self.JE)] for i in range(self.IE)]
        
        self.ihx = [ [0.0 for j in range(self.JE)] for i in range(self.IE)]
        self.ihy = [ [0.0 for j in range(self.JE)] for i in range(self.IE)]
        
        self.gi2 = [ 1.0 for i in range(self.IE)]
        self.gi3 = [ 1.0 for i in range(self.IE)]
        
        self.gj2 = [ 1.0 for i in range(self.JE)]
        self.gj3 = [ 1.0 for i in range(self.JE)]
        
        self.fi1 = [ 0.0 for i in range(self.IE)]
        self.fi2 = [ 1.0 for i in range(self.IE)]
        self.fi3 = [ 1.0 for i in range(self.IE)]
        
        self.fj1 = [ 0.0 for i in range(self.JE)]
        self.fj2 = [ 1.0 for i in range(self.JE)]
        self.fj3 = [ 1.0 for i in range(self.JE)]
        
        self.ez_inc = [ 0.0 for i in range(self.JE)]
        self.hx_inc = [ 0.0 for i in range(self.JE)]
        
        self.dic['t0'] = 20.
        self.dic['T'] = 0
        self.dic['spread'] = 8.
        self.dic['ic'] = self.IE//2
        self.dic['jc'] = self.JE//2
        self.dic['ia'] = 6
        self.dic['ib'] = self.IE - self.dic['ia'] - 1
        self.dic['ja'] = 6
        self.dic['jb'] = self.JE - self.dic['ja'] - 1
        for i in range(npml+1):
            xnum = npml - i
            xd = npml
            xxn = xnum / xd
            xn = 0.25 * pow(xxn, 3.0)
            self.gi2[i] = 1.0 / (1.0 + xn)
            self.gi2[self.IE - 1 - i] = 1.0 / (1.0 + xn)
            self.gi3[i] = (1.0 - xn) / (1.0 + xn)
            self.gi3[self.IE - i - 1] = (1.0 - xn) / (1.0 + xn)
            xxn = (xnum - .5) / xd
            xn = 0.25 * pow(xxn, 3.0)
            self.fi1[i] = xn
            self.fi1[self.IE - 2 - i] = xn
            self.fi2[i] = 1.0 / (1.0 + xn)
            self.fi2[self.IE - 2 - i] = 1.0 / (1.0 + xn)
            self.fi3[i] = (1.0 - xn) / (1.0 + xn)
            self.fi3[self.IE - 2 - i] = (1.0 - xn) / (1.0 + xn)
        for j in range(npml+1):
            xnum = npml - j
            xd = npml
            xxn = xnum / xd
            xn = 0.25 * pow(xxn, 3.0)
            self.gj2[j] = 1.0 / (1.0 + xn)
            self.gj2[self.JE - 1 - j] = 1.0 / (1.0 + xn)
            self.gj3[j] = (1.0 - xn) / (1.0 + xn)
            self.gj3[self.JE - j - 1] = (1.0 - xn) / (1.0 + xn)
            xxn = (xnum - .5) / xd
            xn = 0.25 * pow(xxn, 3.0)
            self.fj1[j] = xn
            self.fj1[self.JE - 2 - j] = xn
            self.fj2[j] = 1.0 / (1.0 + xn)
            self.fj2[self.JE - 2 - j] = 1.0 / (1.0 + xn)
            self.fj3[j] = (1.0 - xn) / (1.0 + xn)
            self.fj3[self.JE - 2 - j] = (1.0 - xn) / (1.0 + xn)
    
    
    
    def loopFDTD(self):
        loop = True
        while(loop):
            for n in range(1,self.NSTEPS+1):
                self.dic['T'] += 1
                for j in range(1,self.JE):
                    self.ez_inc[j] = self.ez_inc[j] + .5 * (self.hx_inc[j - 1] - self.hx_inc[j])

                self.ez_inc[0] = self.dic['ez_inc_low_m2']
                self.dic['ez_inc_low_m2'] = self.dic['ez_inc_low_m1']
                self.dic['ez_inc_low_m1'] = self.ez_inc[1]
                self.ez_inc[self.JE - 1] = self.dic['ez_inc_high_m2']
                self.dic['ez_inc_high_m2'] = self.dic['ez_inc_high_m1']
                self.dic['ez_inc_high_m1'] = self.ez_inc[self.JE - 2]
        
                for j in range(1,self.IE):
                    for i in range(1,self.IE):
                        self.dz[i][j] = self.gi3[i] * self.gj3[j] * self.dz[i][j] + self.gi2[i] * self.gj2[j] * .5 * (self.hy[i][j] - self.hy[i - 1][j] - self.hx[i][j] + self.hx[i][j - 1])
        
                self.dic['pulse'] = math.exp(-.5 * pow((self.dic['T'] - self.dic['t0']) / self.dic['spread'], 2.))
                self.ez_inc[self.dic['kc']] = self.dic['pulse']
        
                for i in range(self.dic['ia'],self.dic['ib']+1):
                    self.dz[i][self.dic['ja']] = self.dz[i][self.dic['ja']] + 0.5 * self.hx_inc[self.dic['ja'] - 1]
                    self.dz[i][self.dic['jb']] = self.dz[i][self.dic['jb']] - 0.5 * self.hx_inc[self.dic['jb']]
        
               # for j in range(1,self.IE):
                #    for i in range(1,self.IE):
                 #       self.ez[i][j] = self.material.ga[i][j] * (self.dz[i][j] - self.iz[i][j])
                  #      self.iz[i][j] = self.iz[i][j] + self.material.gb[i][j] * self.ez[i][j]
                for j in range(1,self.IE):
                    for i in range(1,self.JE):
                        self.ez[i][j] = float(self.material.ga[i][j] * self.dz[i][j])

                for j in range(self.JE-1):
                    self.hx_inc[j] = self.hx_inc[j] + .5 * (self.ez_inc[j] - self.ez_inc[j + 1])
        
                for j in range(self.JE-1):
                    for i in range(self.IE):
                        curl_e = self.ez[i][j] - self.ez[i][j + 1]
                        self.ihx[i][j] = self.ihx[i][j] + self.fi1[i] * curl_e
                        self.hx[i][j] = self.fj3[j] * self.hx[i][j] + self.fj2[j] * .5 * (curl_e + self.ihx[i][j])
        
                for i in range(self.dic['ia'],self.dic['ib']+1):
                    self.hx[i][self.dic['ja'] - 1] = self.hx[i][self.dic['ja'] - 1] + (.5 * self.ez_inc[self.dic['ja']])
                    self.hx[i][self.dic['jb']] = self.hx[i][self.dic['jb']] - (.5 * self.ez_inc[self.dic['jb']])
        
                for j in range(self.JE-1):
                    for i in range(self.IE-1):
                        curl_e = self.ez[i + 1][j] - self.ez[i][j]
                        self.ihy[i][j] = self.ihy[i][j] + self.fj1[j] * curl_e
                        self.hy[i][j] = self.fi3[i] * self.hy[i][j] + self.fi2[i] * .5 * (curl_e + self.ihy[i][j])
                for j in range(self.dic['ja'],self.dic['jb']+1):
                    self.hy[self.dic['ia'] - 1][j] = self.hy[self.dic['ia'] - 1][j] - (.5 * self.ez_inc[j])
                    self.hy[self.dic['ib']][j] = self.hy[self.dic['ib']][j] + (.5 * self.ez_inc[j])
                
                
                self.showGraphic.saveFigColor(self.dic['T'],self.ez,[])
            loop = False
    def loopFDTD2(self, materiais):
        print(len(materiais))
        for n in range(self.NSTEPS+1):
            self.dic['T'] += 1
            for j in range(1,self.JE):
                self.ez_inc[j] = self.ez_inc[j] + .5 * (self.hx_inc[j - 1] - self.hx_inc[j])
    
            self.ez_inc[0] = self.dic['ez_inc_low_m2']
            self.dic['ez_inc_low_m2'] = self.dic['ez_inc_low_m1']
            self.dic['ez_inc_low_m1'] = self.ez_inc[1]
            self.ez_inc[self.JE - 1] = self.dic['ez_inc_high_m2']
            self.dic['ez_inc_high_m2'] = self.dic['ez_inc_high_m1']
            self.dic['ez_inc_high_m1'] = self.ez_inc[self.JE - 2]
    
            for j in range(1,self.IE):
                for i in range(1,self.IE):
                    self.dz[i][j] = self.gi3[i] * self.gj3[j] * self.dz[i][j] + self.gi2[i] * self.gj2[j] * .5 * (self.hy[i][j] - self.hy[i - 1][j] - self.hx[i][j] + self.hx[i][j - 1])
    
            self.dic['pulse'] = math.exp(-.5 * pow((self.dic['T'] - self.dic['t0']) / self.dic['spread'], 2.))
            self.ez_inc[self.dic['kc']] = self.dic['pulse']
    
            for i in range(self.dic['ia'],self.dic['ib']+1):
                self.dz[i][self.dic['ja']] = self.dz[i][self.dic['ja']] + 0.5 * self.hx_inc[self.dic['ja'] - 1]
                self.dz[i][self.dic['jb']] = self.dz[i][self.dic['jb']] - 0.5 * self.hx_inc[self.dic['jb']]
            
            for i in range(1,self.IE):
                for j in range(1,self.JE):
                    for k in materiais:
                        if(k.ga[i][j] != 1):
                            self.ez[i][j] = float(k.ga[i][j] * self.dz[i][j])
                        
            for j in range(self.JE - 1):
                self.hx_inc[j] = self.hx_inc[j] + .5 * (self.ez_inc[j] - self.ez_inc[j + 1])
    
            for j in range(self.JE-1):
                for i in range(self.IE):
                    curl_e = self.ez[i][j] - self.ez[i][j + 1]
                    self.ihx[i][j] = self.ihx[i][j] + self.fi1[i] * curl_e
                    self.hx[i][j] = self.fj3[j] * self.hx[i][j] + self.fj2[j] * .5 * (curl_e + self.ihx[i][j])
    
            for i in range(self.dic['ia'],self.dic['ib']+1):
                self.hx[i][self.dic['ja'] - 1] = self.hx[i][self.dic['ja'] - 1] + .5 * self.ez_inc[self.dic['ja']]
                self.hx[i][self.dic['jb']] = self.hx[i][self.dic['jb']] - .5 * self.ez_inc[self.dic['jb']]
    
            for j in range(self.JE-1):
                for i in range(self.IE-1):
                    curl_e = self.ez[i + 1][j] - self.ez[i][j]
                    self.ihy[i][j] = self.ihy[i][j] + self.fj1[j] * curl_e
                    self.hy[i][j] = self.fi3[i] * self.hy[i][j] + self.fi2[i] * .5 * (curl_e + self.ihy[i][j])
            for j in range(self.dic['ja'],self.dic['jb']+1):
                self.hy[self.dic['ia'] - 1][j] = self.hy[self.dic['ia'] - 1][j] - .5 * self.ez_inc[j]
                self.hy[self.dic['ib']][j] = self.hy[self.dic['ib']][j] + .5 * self.ez_inc[j]
            
            self.showGraphic.saveFigColor(self.dic['T'],self.ez,[])
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        