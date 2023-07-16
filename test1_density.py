import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("test1.lammpstrj", skiprows = 9, unpack = True)
print(data)

def make_graph(r, s, n):
    x = np.linspace(0, r * s, 100)
    density = n / (r * s)**2
    plt.plot(x, density)
    plt.show()

r = 10
s = 2.0

make_graph(r, s, n)