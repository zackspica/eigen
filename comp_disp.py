#!/usr/bin/python
import os


model = "model_step96.in"
nmodes = 3
fmin = 0.12
fmax = 1

for mode in ['R']:#['R','L']
    # This prog create inputs for sdispt96
    print (">>> Compute input model")
    os.system("sprep96 -M %s -d distance.dat -%s -NMOD %s \
            -FMIN %s -FMAX %s" %\
             (model, mode, nmodes, fmin, fmax))

    
    print (">>> Dispersion curves : sdisp96 ...")
    print ()
    # This program computes the dc for the given earth model. 
    # Output is a binary files e.g. sdisp96.ray.
    os.system("sdisp96 -v")
    
    #This programs reads the phase velocity dc sdisp96 and expert them in txt or ASC
    print (">>> Extract disp curves : sdpsrf96 ...")
    os.system("sdpsrf96 -%s  -ASC"%mode)
    


    # The following section is made for sensitivity kernel calculation
#    if mode == 'R':
#        print ("Compute Rayleigh depth dependent values : sregn96 ...")
#        os.system("sregn96 -DER")
#    if mode == 'L':
#        print ("Compute Love depth dependent values : slegn96 ...")
#        os.system("slegn96 -DER")
#    
#    # This programs reads the depth dependent eigenfunction file created by the -DER,
#    # -DH, -DA, -DB or -DR options of slegn96 or sregn96 and expert the curves in txt
#    print ("Plot Dispersion curves (c, U, NRJ, ell) : sdpder96 ...")
#    os.system("sdpder96 -%s -TXT"%mode)


