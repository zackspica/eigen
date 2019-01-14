import numpy as np
import matplotlib.pyplot as plt

d = np.loadtxt('depth.dat')
mod = np.loadtxt('model.info', dtype={'names': ('vs','d'),'formats': ('f4', 'f4')})




fig = plt.figure()
ax = fig.add_subplot(121)
tempo = np.genfromtxt('RAYLEIGH_EIGENFUNCTIONS/UZ_R0_f0.332.dat', dtype={'names': ('UZ', 'depth'),'formats': ('f4', 'f4')},skip_footer=1)
UR0 = tempo['UZ']
UR0 /= max(UR0)
depth = tempo['depth']
nlay = len(UR0)
ax.plot(UR0,-depth,lw=2,label='3s')
tempo = np.genfromtxt('RAYLEIGH_EIGENFUNCTIONS/UZ_R0_f0.201.dat', dtype={'names': ('UZ', 'depth'),'formats': ('f4', 'f4')},skip_footer=1)
UR0 = tempo['UZ']
UR0 /= max(UR0)
depth = tempo['depth']
nlay = len(UR0)
ax.plot(UR0,-depth,lw=2,label='5s')
tempo = np.genfromtxt('RAYLEIGH_EIGENFUNCTIONS/UZ_R0_f0.100.dat', dtype={'names': ('UZ', 'depth'),'formats': ('f4', 'f4')},skip_footer=1)
UR0 = tempo['UZ']
UR0 /= max(UR0)
depth = tempo['depth']
ax.plot(UR0,-depth,lw=2,label='10s')
tempo = np.genfromtxt('RAYLEIGH_EIGENFUNCTIONS/UZ_R0_f0.066.dat', dtype={'names': ('UZ', 'depth'),'formats': ('f4', 'f4')},skip_footer=1)
UR0 = tempo['UZ']
UR0 /= max(UR0)
depth = tempo['depth']
ax.plot(UR0,-depth,lw=2,label='15s')
tempo = np.genfromtxt('RAYLEIGH_EIGENFUNCTIONS/UZ_R0_f0.051.dat', dtype={'names': ('UZ', 'depth'),'formats': ('f4', 'f4')},skip_footer=1)
UR0 = tempo['UZ']
UR0 /= max(UR0)
depth = tempo['depth']
ax.plot(UR0,-depth,lw=2,label='20s')
tempo = np.genfromtxt('RAYLEIGH_EIGENFUNCTIONS/UZ_R0_f0.041.dat', dtype={'names': ('UZ', 'depth'),'formats': ('f4', 'f4')},skip_footer=1)
UR0 = tempo['UZ']
UR0 /= max(UR0)
depth = tempo['depth']
ax.plot(UR0,-depth,lw=2,label='25s')

for d in mod['d']:
    ax.axhline(-d,c='k',ls='--',lw=0.6)

ax.set_ylim(-60,0)
ax.set_title('Rayleigh Waves Eigenfunctions')
ax.set_xlabel('Normalized Displacement')
ax.set_ylabel('Depth (km)')
plt.legend(loc=0)
ax2 = fig.add_subplot(122)
vs, d = mod['vs'],-mod['d']
ax2.plot(vs, d) 
ax2.set_title('Velocity model')
ax2.set_xlabel('Vs [km/s]')
ax2.set_ylim(-60,0)

plt.savefig('UZ.com_camara.pdf',dpi=300, format='pdf')
plt.show()

