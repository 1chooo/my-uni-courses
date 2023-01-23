implicit none
real x
integer n
real p
real q

p = 0.

print*,'x = ?'
read*,x
	   
do n = 0,100
    p = p+(((-1)**n)*(x**(2*n+1)))/((2*n)+1)
enddo

q = atan(x)
	   
print*,'sum = ',p,'accurate sum =',q

stop
end