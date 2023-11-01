#!bin/bash

obsfiles=($(ls 16*.obs))

for obsfile in ${obsfiles[*]}
do
    egrep '01\+' $obsfile > "1to8_$obsfile"
    egrep '09\+' $obsfile > "9to11_$obsfile"
    paste -d ' ' "1to8_$obsfile" "9to11_$obsfile" | sed 's/\r//g' | sed s'/[01][0-9]\+//g' | sed s'/  / /g' >> "all_1601.obs"
#    paste -d ' ' "1to8_$obsfile" "9to11_$obsfile" | sed 's/\r//g' | sed 's/[0-9]\+|1[01]\+//g' | sed 's/  / /g' >> "all_1601.obs"
done

rm 1to8*
rm 9to11*
