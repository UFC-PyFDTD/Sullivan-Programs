
from Materiais import DielCond
import FDTD
import ShowPlt
d = DielCond(100, 3, 500,1)
sh = ShowPlt.showPlt(1,-1)

d.init()

method = FDTD.FDTD(sh, 500, 200,d)

method.init()
method.loopFDTDFourier()

'''
from Materiais import Cilinder
from FDTD import FDTD2D
import ShowPlt

cilindro = Cilinder(20, 0.1,50 , 15, 150, 150)

sh = ShowPlt.showPlt(1,-1)

cilindro.init()

method = FDTD2D(cilindro,sh,200,300,150,150)
method.init(20)
method.loopFDTD()
'''
'''
from Materiais import Cilinder
from FDTD import FDTD2D
import ShowPlt

cilindro = Cilinder(1, 0.1,50 , 25,25 , 50)
#cilindro2 = Cilinder(4,0.1,50, 20,20,50)
sh = ShowPlt.showPlt(1,-1)

cilindro.init()
#cilindro2.init()
method = FDTD2D(cilindro,sh,150,0,50,50)
method.init(20)
method.loopFDTD()
'''

