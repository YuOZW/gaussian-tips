import sys
import os
import glob
import subprocess
import filecmp

XTB_EXE = "xtb"
BOHR_TO_ANG = 0.529177249

layer = sys.argv[-6]
InputFile = sys.argv[-5].replace("\\", "/")
OutputFile = sys.argv[-4].replace("\\", "/")
MsgFile = sys.argv[-3].replace("\\", "/")
FChkFile = sys.argv[-2].replace("\\", "/")
MatElFile = sys.argv[-1].replace("\\", "/")
NameHead = InputFile[:-4]
keep_files = glob.glob(NameHead + '*')

label = []
coord = []
with open(InputFile, 'r') as fin:
	items = fin.readline().split()
	natom = int(items[0])
	flug_freq = int(items[1])
	charge = int(items[2])
	spin = int(items[3])
	for i in range(natom):
		items = fin.readline().split()
		label.append(int(items[0]))
		coord.append([
			float(items[1]) * BOHR_TO_ANG,
			float(items[2]) * BOHR_TO_ANG,
			float(items[3]) * BOHR_TO_ANG,
			])

with open(NameHead + ".xyz", "w") as fout:
	fout.write(str(natom) + "\n")
	fout.write(NameHead + "\n")
	for i in range(natom):
		fout.write(str(label[i]).rjust(3) + " ")
		fout.write("{:>20,.10f}  ".format(coord[i][0]))
		fout.write("{:>20,.10f}  ".format(coord[i][1]))
		fout.write("{:>20,.10f}\n".format(coord[i][2]))

command = XTB_EXE + " "
command = command + NameHead + ".xyz "
for option in sys.argv[1:-6]:
	command = command + option + " "

if flug_freq == 0:
	command = command + \
	"--norestart --nocopy " + \
	"--chrg " + str(charge) + " " + \
	"--uhf " + str(spin - 1) + " " + \
	"--namespace " + NameHead
if flug_freq >= 1:
	command = command + \
	"--grad " + \
	"--norestart --nocopy " + \
	"--chrg " + str(charge) + " " + \
	"--uhf " + str(spin - 1) + " " + \
	"--namespace " + NameHead
if flug_freq == 2:
	command = command + \
	"--hess " + \
	"--norestart --nocopy " + \
	"--chrg " + str(charge) + " " + \
	"--uhf " + str(spin - 1) + " " + \
	"--namespace " + NameHead

with open(NameHead + ".out", "w") as fout:
	subprocess.call(command.split(), stdout=fout)

with open(OutputFile, "w") as fout:
	energy = 0.0
	dipole = [0.0, 0.0, 0.0]
	with open(NameHead + ".out", "r") as fin:
		while True:
			line = fin.readline()
			if not line: break
			if "| TOTAL ENERGY" in line:
				energy = float(line.split()[3])
			if "molecular dipole" in line:
				line = fin.readline()
				line = fin.readline()
				line = fin.readline()
				dipole[0] = float(line.split()[1])
				dipole[1] = float(line.split()[2])
				dipole[2] = float(line.split()[3])
		fout.write("{:20.12E}".format(float(energy)))
		fout.write("{:20.12E}".format(dipole[0]))
		fout.write("{:20.12E}".format(dipole[1]))
		fout.write("{:20.12E}".format(dipole[2]))
		fout.write("\n")

	if flug_freq == 1 or flug_freq == 2:
		with open(NameHead + ".gradient", "r") as fin:
			fin.readline()
			fin.readline()
			for i in range(natom):
				fin.readline()
			for i in range(natom):
				line = fin.readline()
				fout.write("{:20.12E}".format(float(line[0:22])))
				fout.write("{:20.12E}".format(float(line[22:44])))
				fout.write("{:20.12E}".format(float(line[44:66])))
				fout.write("\n")
			for i in range(2):
				fout.write("{:20.12E}".format(0.0))
				fout.write("{:20.12E}".format(0.0))
				fout.write("{:20.12E}".format(0.0))
				fout.write("\n")
			for i in range(3 * natom):
				fout.write("{:20.12E}".format(0.0))
				fout.write("{:20.12E}".format(0.0))
				fout.write("{:20.12E}".format(0.0))
				fout.write("\n")

	if flug_freq == 2:
		with open(NameHead + ".hessian", "r") as fin:
			hess = np.zeros((3 * natom, 3 * natom), dtype=np.float32)
			line = fin.readline()
			row = 0
			column = 0
			for i in range(3 * natom):
				for j in range(ceil(3 * natom / 5)):
					line = fin.readline()
					for k in range(5):
						hess[row][column] = float(line[k*15+5:k*15+20])
						column += 1
						if column == 3 * natom:
							row += 1
							column = 0
							break

		count = 0
		for i in range(3 * natom):
			for j in range(i + 1):
				fout.write("{:20.12E}".format(hess[i][j]))
				count += 1
				if count % 3 == 0:
					fout.write("\n")
					count = 0

for f in glob.glob(NameHead + '*'):
	if filecmp.cmp(f, OutputFile): continue
	if os.path.isfile(f): os.remove(f)