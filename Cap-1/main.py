from dieletric import dieletrico
import FDTD
import showPlt
d = dieletrico(100, 0.2, 200)
sh = showPlt.showPlt(1,-1)

d.init()

method = FDTD.FDTD(d, sh, 200, 1)
method.init()
method.loopFDTD()