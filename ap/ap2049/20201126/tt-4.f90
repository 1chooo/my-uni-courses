implicit none

real x
integer n
real p
real q

p = 0.

print*,'x = ?'
read*,x

do n = 0,100
    p =p+((x**(2*n+1))/(2*n+1))
enddo

p = 2*p
q = log((1+x)/(1-x))
	   
print*,'sum = ',p,'accurate sum =',q

stop
end