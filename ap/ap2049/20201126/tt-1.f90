    implicit none
    real x
    integer n
    real p
    real q

    p = 0.

    print *, 'x = ?'
    read *, x

    do n = 0, 100
        p = p + x ** n
    enddo

    q = 1 / (1 - x)

    print *, 'sum = ', p, 'accurate sum = ', q
    stop
    end
