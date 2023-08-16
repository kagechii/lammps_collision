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
        if xi == D:
            xi = 0
        rhoz[xi] += 1.0/(LY*LZ*dx)
    return rhoz


def save_frame(index, rhoz):
    filename = f"frame{index:03d}.dat"
    print(filename)
    with open(filename, "w") as f:
        for i in range(len(rhoz)):
            f.write(f"{i * dx} {rhoz[i]}\n")


def save_file(filename):
    with open("test1.lammpstrj") as f:
        index = 0
        for line in f:
            if "ITEM: ATOMS" in line:
                t, x, y, z = read_atoms(f)
                rhoz = rho(t, x, y, z)
                save_frame(index, rhoz)
                index += 1
            continue
    print("Generated {}".format(filename))


LX = 40
LY = 20
LZ = 20

dx = 0.5

save_file("test1.rho")
