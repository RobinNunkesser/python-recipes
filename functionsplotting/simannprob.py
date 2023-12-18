import math
import numpy as np
from matplotlib import pyplot as plt

plt.style.use('dark_background')

#plt.rcParams["figure.figsize"] = [7.50, 3.50]
#plt.rcParams["figure.autolayout"] = True

def t(x):
   return 20 * math.exp(-0.045 * x)

def p(d,x):
   return math.exp(-d / t(x))

myFn = np.vectorize(p)
x = np.linspace(0, 100, 1000)

fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x, myFn(1,x), '-', label="1")
ax.plot(x, myFn(2,x), '-', label="2")
ax.plot(x, myFn(3,x), '-', label="3")
ax.plot(x, myFn(5,x), '-', label="5")
ax.plot(x, myFn(8,x), '-', label="8")
ax.plot(x, myFn(13,x), '-', label="13")
ax.plot(x, myFn(21,x), '-', label="21")
ax.plot(x, myFn(34,x), '-', label="34")
ax.plot(x, myFn(55,x), '-', label="55")
legend = ax.legend(loc="best")
plt.xlabel("Schritt") 
plt.ylabel("Wahrscheinlichkeit") 

#plt.show()
plt.tight_layout()
plt.savefig("/Users/nunkesser/repos/work/images/ai/simannprob.svg")