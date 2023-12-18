import math
import numpy as np
from matplotlib import pyplot as plt

plt.style.use('dark_background')

#plt.rcParams["figure.figsize"] = [7.50, 3.50]
#plt.rcParams["figure.autolayout"] = True

def f(x):
   return 20 * math.exp(-0.045 * x)

myFn = np.vectorize(f)
x = np.linspace(0, 100, 1000)

plt.xlabel("Schritt") 
plt.ylabel("Temperatur") 
plt.plot(x, myFn(x))

#plt.show()
plt.tight_layout()
plt.savefig("/Users/nunkesser/repos/work/images/ai/simanntemp.svg")