# -*- coding: utf-8 -*-

R=0.01097

for m in range(1,4):
    for n in range(m+1,m+6):
        ℷ=1/(R*((1/m**2)-(1/n**2)))
        print(m,n,ℷ)
        
