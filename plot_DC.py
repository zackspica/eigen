import numpy as np
import matplotlib.pyplot as plt

fig =plt.figure()
ax = fig.add_subplot(111)

file = 'SDISPR.ASC'
f = np.genfromtxt(file, skip_header=1)


nmodes = int(f[:,0][-1])
nlines = int(len(f[:,0]))

print ('nmodes: ',nmodes, 'nlines: ', nlines )

nk=0
freq, c = [], []
for i in np.arange(nlines):
    nm = int(f[i,0])
    if nm == nk:
        freq.append(float(f[i,3]))
        c.append(float(f[i,4]))
    else:
        ax.plot(freq, c)
        freq, c = [], []
        nk += 1
        

ax.set_xlabel('Freq.')
ax.set_ylabel('Phase vel.')
plt.show()
