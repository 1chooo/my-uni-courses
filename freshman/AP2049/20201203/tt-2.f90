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
    do j = 1,2*(n-1)+1
        n1 = n1*float(j)
    enddo
    p = p + ((-1)**(n-1)*(x**(2*(n-1)+1)))/n1
enddo

q = sin(x)

print*,'x = ',x 
print*,'p = ',p,'q = ',q
   
stop 
end