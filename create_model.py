import numpy as np
import os, time, sys
""" This script create the model96 file
    based on a simple model with some layers
    the script discretize the model with a
    specific "step".
    input : start_model.dat
    -----------------------
    H(KM)  VP(KM/S)  VS(KM/S)  RHO(GM/CC)  QP  QS  ETAP  ETAS  FREFP  FREFS
    0.7813   2.34      1.35      1518.2   500  250  0.0  0.0   1.0   1.0
    0.9957   2.42      1.40      1545.9   500  250  0.0  0.0   1.0   1.0
    1.2132   4.59      2.65      2238.7   500  250  0.0  0.0   1.0   1.0
    ...      ...       ..        .        
"""


def cumula():
    """ create 'cumul_depths.dat' all the cumulate depths 
        of the initial model
        /!\ the last depth isn't counted (inifinit half space)
    """
    f = open('cumul_depths.tmp','w+')
    model = np.loadtxt('start_model.dat',dtype={'names': ('H'),'formats': \
                    ('f4')}, skiprows=1,usecols=[0])
    
    cumul = 0
    for i, d in enumerate(model['H'][:-1]): 
    # le dernier est souvent le semi espace donc pas besoin (tres prof)
        cumul +=d
        print "layer ", i, " - depth: ", cumul
        f.write("%s\n" % cumul)
    f.close()


def model_input(step=0.1):
    """ This function create the discret velocity 
        model_step96.in thanks to the mkmod96 function
        There is a limitation of 200 layes (why?)
        so the step don't have to be too small
        otherwise you shoud constrain the max depth of 
        the start_model.dat; default : penultima capa
        
        input : start_model.dat
        -----------------------
        H(KM)  VP(KM/S)  VS(KM/S)  RHO(GM/CC)  QP  QS  ETAP  ETAS  FREFP  FREFS
        0.7813   2.34      1.35      1518.2   500  250  0.0  0.0   1.0   1.0
        0.9957   2.42      1.40      1545.9   500  250  0.0  0.0   1.0   1.0
        1.2132   4.59      2.65      2238.7   500  250  0.0  0.0   1.0   1.0
        ...      ...       ..        .        
    
    
    """
    model = np.loadtxt('start_model.dat',dtype={'names': ('H', 'VP','VS','RHO','QP','QS',\
                    'ETAP','ETAS','FREFP','FREFS'),'formats': ('f4', 'f4','f4','f4',\
                    'f4','f4','f4','f4','f4','f4')}, skiprows=1)
   
    f = open('model96_input.tmp', 'w+')
    f.write('model_step96.in\nIsotropic model\n0\n')
    d = np.loadtxt('cumul_depths.tmp')
    for i in np.arange(len(d)):
        for k, s in enumerate(np.arange(0,d[-1],step)):
            if s < d[i] and i==0:
                f.write('%s %s %s %s %s %s %s %s %s %s\n'
                    %(step, model['VP'][i], model['VS'][i], model['RHO'][i],\
                    model['QP'][i], model['QS'][i], model['ETAP'][i], model['ETAS'][i],\
                    model['FREFP'][i], model['FREFS'][i]))
            if i > 0:
                if s < d[i] and s > d[i-1]:
                    f.write('%s %s %s %s %s %s %s %s %s %s\n'
                        %(step, model['VP'][i], model['VS'][i], model['RHO'][i],\
                        model['QP'][i], model['QS'][i], model['ETAP'][i], model['ETAS'][i],\
                        model['FREFP'][i], model['FREFS'][i]))
    f.close()
    os.system("mkmod96 < model96_input.tmp")
    print ">>  Model_step96.in is ready... next step is comp_disp.bash"
    print '>>  nlayers =', k
    print ">>  Change nlayer in eigenfucntion_*.bash!!!!"
    print ">>  mkmod96"

def check(step=1.):
    model = np.loadtxt('cumul_depths.tmp',dtype={'names': ('H'),'formats': \
                    ('f4')}, skiprows=1,usecols=[0])
    depth = model['H'][-1]
    n = depth/step
    if n >200:
        print ">>  Too many layers for mkmod96 (max=200)\n>>  You must change the step size or refine the start_model.dat\n>>  (must be shalower)"
        print "Exit"
        sys.exit()
    else:
        print ">>  Step size Ok"
        pass


def depthfile(step):
    """create depth.dat"""
    model = np.loadtxt('cumul_depths.tmp',dtype={'names': ('H'),'formats': \
                    ('f4')}, skiprows=1,usecols=[0])
    maxdepth = model['H'][-1]
    f = open('depth.dat','w+')
    for d in np.arange(step,maxdepth,step):
        f.write('%s\n'%d) 
    f.close()
    print ">>  depth.dat up to date"

def minfo():
    """ create model.info for easy plot"""
    model = np.loadtxt('cumul_depths.tmp',dtype={'names': ('H'),'formats': \
                    ('f4')}, usecols=[0])
    d = model['H']
    model = np.loadtxt('start_model.dat',dtype={'names': ("S"),'formats': \
                    ('f4')}, skiprows=1,usecols=[2])
    vs = model['S']

    A = np.repeat(vs,2)
    B = np.repeat(d,2)
    B = np.insert(B,[0],0.0)[:-1] 
    out = zip(A, B)
    
    f = open('model.info','w+')
    for line in out:
        print " ".join(str(x) for x in line)
        f.write(" ".join(str(x) for x in line) + "\n") 
    f.close()



if __name__=="__main__":
    step = input("Enter the step size (km) :")
    cumula()
    check(step=step)
    depthfile(step)
    minfo()
    model_input(step=step)
    #os.system("rm *tmp")
