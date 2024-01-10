# [AP2049] Computer Programming and Graphics Ⅰ

Programming Language: `Fortran`


```f90
program HelloWorld
    implicit none

    print *, "Hello world"
end program HelloWorld
```

### 20201126

```f90
! tt-1.f90
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
```

```f90
! tt-2.f90
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
```

```f90
! tt-3.f90
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
    do j = 1,2*(n)
        n1 = n1*float(j)
    enddo
    p = p + ((-1)**(n)*(x**(2*n)))/n1
enddo

p = p + 1.
q = cos(x)

print*,'x = ',x 
print*,'p = ',p,'q = ',q

stop 
end
```

### 20201203

```f90
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
```

```f90
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
```

```f90
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
    do j = 1,2*(n)
        n1 = n1*float(j)
    enddo
    p = p + ((-1)**(n)*(x**(2*n)))/n1
enddo

p = p + 1.
q = cos(x)

print*,'x = ',x 
print*,'p = ',p,'q = ',q

stop 
end
```

### 20201210

```f90
implicit none
!------------------------------------------
!20201210: To process sounding data;
!------------------------------------------

! integer i
! integer j
! integer k
! integer hght ! height;
! integer relh ! relative humidity;
! integer drct ! wind direction;
! integer sknt ! wind speed in knot;
integer ilinein
integer len_trim
! real pres ! pressure;
! real temp ! temperature;
! real dwdt ! dew point temperature;
! real mixr ! mixing ratio for water vapor;
! real thta ! potential temperature;
! real thte ! equivalent potential temperature;
! real thtr ! virtual equivalent temperature;
character*100 linein! name string long 100 -> linein

!-------------------------------------------

open(1, file = '47918.txt', form = 'formatted') ! open, name 47918.txt -> 1 by formatted form;
10 continue
read(1, '(a)', end = 20) linein ! read 1 by form(a) -> linein;
ilinein = len_trim(linein) ! 
print *, 'ilinein=', ilinein
print *, linein(1:ilinein)
goto 10
20 continue
close(1)

stop
end
```

### 20201217

```f90
implicit none

!-------------------------------------------------------

! integer i
integer j
! integer k
integer len_trim   ! find line length;
integer ilinein    ! line length;
integer ifilein    ! filein length
character*200 linein ! readin character data;
character*200 filein ! file to be processewd;
!
!Arguments for data;
!
integer hght
integer relh
integer drct
integer sknt
real pres
real temp
real dwpt
real mixr
real thta
real thte
real thtv
!-------------------------------------------------------------
open(1 , file = "file_list" , form = "formatted") 

10 continue
read(1 , "(a)" , end = 20) filein
ifilein = len_trim(filein)

print*,'processing'//filein(1:ifilein)

open(2 , file = filein(1:ifilein) , form = "formatted")

! skip data header

do j = 1,6
     read(2 , "(a)" , end = 40)linein
     ilinein = len_trim(linein)
     print*,linein(1:ilinein)
enddo

! read data;
read(2,*) pres, hght, temp, dwpt, relh, mixr, drct, sknt, thta, thte, thtv
print 2020, pres, hght, temp, dwpt, relh, mixr, drct, sknt, thta, thte, thtv
2020 format(f6.1, 2x, i5, 2x, f5.1, 2x, f5.1, 2x, i2, 2x, f4.2, 2x, i3, 2x, i2, 3(2x, f5.1))
! stop

40 continue

close(2)

goto 10
20 continue
close(1)

stop
end
```
