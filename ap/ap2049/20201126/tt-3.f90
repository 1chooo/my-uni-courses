implicit none

real x
integer n
real p
real q

p = 0.

print*,'x = ?'
read*,x
	   
do n = 1,100
    p = p+(((-1)**(n-1))*(x**n))/n
enddo

q = log(1+x)
   
print*,'sum = ',p,'accurate sum =',q

stop
end