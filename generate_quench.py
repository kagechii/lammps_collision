# 完全に混ざった状態から相分離するシミュレーション
import random


class Atom:
    def __init__(self, x, y, z, t):
        self.x = x
        self.y = y
        self.z = z
        self.type = t
        r_x = random.uniform(-1, 1) * 3.0
        r_y = random.uniform(-1, 1) * 3.0
        r_z = random.uniform(-1, 1) * 3.0
        self.vx = r_x
        self.vy = r_y
        self.vz = r_z


def add_ball(atoms, r, s, x_0):
    h = 0.5 * s
    for ix in range(r):
        for iy in range(r):
            for iz in range(r):
                x = ix * s + x_0
                y = iy * s
                z = iz * s
                t = random.randint(1, 2)
                atoms.append(Atom(x, y, z, t))
                atoms.append(Atom(x, y+h, z+h, t))
                atoms.append(Atom(x+h, y, z+h, t))
                atoms.append(Atom(x+h, y+h, z, t))


def save_file(filename, atoms, r, s):
    with open(filename, "w") as f:
        f.write("Position Data\n\n")
        f.write(f"{len(atoms)} atoms\n")
        f.write("2 atom types\n\n")
        f.write(f"{box[0]} {box[1]} xlo xhi\n")
        f.write(f"{box[2]} {box[3]} ylo yhi\n")
        f.write(f"{box[4]} {box[5]} zlo zhi\n")
        f.write("\n")
        f.write("Atoms\n\n")
        for i, a in enumerate(atoms):
            f.write("{} {} {} {} {}\n".format(i+1, a.type, a.x, a.y, a.z))
        f.write("\n")
        f.write("Velocities\n\n")
        for i, a in enumerate(atoms):
            f.write("{} {} {} {}\n".format(i+1, a.vx, a.vy, a.vz))
    print("Generated {}".format(filename))


atoms = []

r = 10
s = 2.0

xlo = 0
xhi = r * s
ylo = 0
yhi = r * s
zlo = 0
zhi = r * s
box = [xlo, xhi, ylo, yhi, zlo, zhi]

add_ball(atoms, r, s, 0)

save_file("quench.atoms", atoms, r, s)
