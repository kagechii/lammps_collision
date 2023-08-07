import numpy as np


def read_atoms(f):
    x = np.zeros(8000)
    y = np.zeros(8000)
    z = np.zeros(8000)
    t = np.zeros(8000)
    for line in f:
        if "ITEM:" in line:
            return t, x, y, z
        a = line.split()
        i = int(a[0]) - 1
        t_i = int(a[1])
        x_i = float(a[2]) * LX
        y_i = float(a[3]) * LY
        z_i = float(a[4]) * LZ
        t[i] = t_i
        x[i] = x_i
        y[i] = y_i
        z[i] = z_i
    return t, x, y, z


def rho(t, x, y, z):
    dx = 0.5
    D = int(LX/dx)
    rhoz = np.zeros(D)
    N = len(t)
    for i in range(N):
        if t[i] == 2:
            continue
        if x[i] < 0:
            x[i] += LX
        if x[i] > LX:
            x[i] -= LX
        xi = int(x[i]/dx)
        rhoz[xi] += 1.0/(LY*LZ*dx)
    return rhoz


def save_file(filename):
    with open(filename, "w") as F:
        with open("test1.lammpstrj") as f:
            for line in f:
                if "ITEM: ATOMS" in line:
                    t, x, y, z = read_atoms(f)
                    rhoz = rho(t, x, y, z)
                    F.write("{}\n".format(rhoz))
                continue
    print("Generated {}".format(filename))


LX = 40
LY = 20
LZ = 20


with open("test1.lammpstrj") as f:
    for line in f:
        if "ITEM: ATOMS" in line:
            t, x, y, z = read_atoms(f)
            rhoz = rho(t, x, y, z)
            print(rhoz)
        continue

save_file("test1.rho")
