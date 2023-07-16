import random

class Atom:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        if x < 20:
            self.type = 1
        else :
            self.type = 2      
        r_x = random.uniform(-1, 1) * 3.0
        r_y = random.uniform(-1, 1) * 3.0
        r_z = random.uniform(-1, 1) * 3.0
        self.vx = r_x
        self.vy = r_y
        self.vz = r_z


def add_ball(atoms, xpos, ypos, zpos):
    r = 10
    s = 2.0
    h = 0.5 * s
    for ix in range(2 * r):
        for iy in range(r):
            for iz in range(r):
                x = ix * s
                y = iy * s
                z = iz * s
                x = x + xpos
                y = y + ypos
                z = z + zpos
                atoms.append(Atom(x, y, z))
                atoms.append(Atom(x, y+h, z+h))
                atoms.append(Atom(x+h, y, z+h))
                atoms.append(Atom(x+h, y+h, z))


xlo = 0
xhi = 40
ylo = 0
yhi = 20
zlo = 0
zhi = 20
box = [xlo, xhi, ylo, yhi, zlo, zhi]


def save_file(filename, atoms,):
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

add_ball(atoms, 0, 0, 0)

save_file("test1.atoms", atoms)
