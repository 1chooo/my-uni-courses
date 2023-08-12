program error
    implicit none

    integer i
    real sum1, sum2, x1, x2
    double Precision sum3, x3

    sum1 = 0
    sum2 = 0
    sum3 = 0
    x1 = 1.
    x2 = 1.e-5
    x3 = 1.d-5

    do i = 1, 100000
        sum1 = sum1 + x1
        sum2 = sum2 + x2
        sum3 = sum3 + x3
    end do

    print *, sum1
    print *, sum2
    print *, sum3
    
    stop
    
end program error

! 100000.000    
! 1.00099015    
! 0.99999999999808376 