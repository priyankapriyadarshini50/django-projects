from sys import path
path.append("C:\\Users\\umesh\\PycharmProjects\\pythonProject1_module\\my_packages\\Extra.zip")
#import Extra.iota
#print(Extra.iota.funI())


from Extra.iota import funI
print(funI())

from Extra.good.best.sigma import funS
from Extra.good.best.tau import funT
import Extra.ugly.omega as ome
from Extra.good.alpha import funA
import Extra.good.beta
print(funS())
print(funT())
print(ome.funO())
print(funA())
print(Extra.good.beta.funB())
print(dir(Extra.good.beta))
print(dir(ome))
