implicit none

real x
integer n
real p    ! right
real q    ! left
real n1   !
integer j ! 

p = 0.
x = 0.1
n1 = 1.
   
do n = 1,4
    do j = 1,n
        n1 = n1*float(j)
    enddo
    p = p + x**n/n1
enddo

p = p + 1.
q = exp(x)

print*,'x = ',x 
print*,'p = ',p,'q = ',q
	   
stop 
end