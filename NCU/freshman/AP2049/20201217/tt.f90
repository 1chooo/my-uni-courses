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