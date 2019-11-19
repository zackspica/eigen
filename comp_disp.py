#!/usr/bin/python
import os


model = "model_step96.in"
nmodes = 1

for mode in ['R']:#['R','L']
    print ("sprep96 -M modele.dat -d distance.dat -$mode -NMOD $nbranche0\
          -FACR 10")
    os.system("sprep96 -M %s -d distance.dat -%s -NMOD %s -FACR 10" %\
             (model, mode, nmodes))

    
    print ("Dispersion curves : sdisp96 ...")
    os.system("sdisp96 -v")

    if mode == 'R':
        print ("Compute Rayleigh depth dependent values : sregn96 ...")
        os.system("sregn96 -DER")
    if mode == 'L':
        print ("Compute Love depth dependent values : slegn96 ...")
        os.system("slegn96 -DER")

    print ("Plot Dispersion curves (c, U, NRJ, ell) : sdpder96 ...")
    os.system("sdpder96 -%s -TXT"%mode)
#

