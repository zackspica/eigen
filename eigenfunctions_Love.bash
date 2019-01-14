#!/bin/bash

dir=LOVE_EIGENFUNCTIONS
mkdir $dir
nlayer=198

eigenfile="SLDER.TXT"
for mode in 0 1
#for mode in 0 
do
grep -n "LOVE WAVE        MODE #  ${mode}" ${eigenfile} |awk -F":" '{print $1}' > lines_L${mode}.dat

while read line
do
let "tline = $line + 1"
#        T = 0.1000E+00 C =    0.1948E+00 U   = 0.1787E+00
perioda=`sed -n "${tline}p" ${eigenfile} |awk -F"C" '{print $1}' | awk -F"=" '{print $2}'`
periodb=${perioda/E-0/*10^-}
period=${periodb/E+0/*10^}
freqa=`echo "1./ ($period )" |bc -l `
freq=`awk "BEGIN {OFMT = \"%0.3f\" ; print $freqa}"`
echo L$mode $freq ...

fileT=${dir}/UT_L${mode}_f${freq}.dat

let "dline = $line + 4"
let "fline = $dline + $nlayer"
sed -n "${dline},${fline}p" ${eigenfile} | awk '{print $2}' > UT.dat

paste -d " " UT.dat depth.dat  > $fileT

done < lines_L${mode}.dat
done
