class dieletrico():
    def __init__(self, start, epsilon, KE):
        self.start = start
        self.epsilon = epsilon
        self.KE = KE
        self.cb = []
    def init(self):
        self.cb = [.5 for i in range(self.KE)]
        for i in range(self.start,self.KE):
            self.cb[i] = self.cb[i]/self.epsilon
        