'''
from Materiais import DielCond
import FDTD
import ShowPlt
d = DielCond(100, 1, 200,1)
sh = ShowPlt.showPlt(1,-1)

d.init()

method = FDTD.FDTD(d, sh, 200, 20)

method.init()
method.loopFDTD()
'''
from Materiais import Cilinder
from FDTD import FDTD2D
import ShowPlt

cilindro = Cilinder(15, 0.3, 50, 15, 60, 60)

sh = ShowPlt.showPlt(1,-1)

cilindro.init()

method = FDTD2D(cilindro,sh,200,100,60,60)
method.init(20)
method.loopFDTD()